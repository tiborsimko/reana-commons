# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2021, 2022, 2024 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""REANA Snakemake Workflow utils."""

import os
import sys
from itertools import filterfalse, chain
from typing import Any, Dict, List, Optional
from pathlib import Path

if sys.version_info >= (3, 11):
    from snakemake.api import SnakemakeApi
    from snakemake.settings.types import (
        ResourceSettings,
        WorkflowSettings,
        ConfigSettings,
        OutputSettings,
        StorageSettings,
        DeploymentSettings,
    )
else:
    from snakemake import snakemake
    from snakemake.dag import DAG
    from snakemake.io import load_configfile
    from snakemake.jobs import Job
    from snakemake.persistence import Persistence
    from snakemake.rules import Rule
    from snakemake.workflow import Workflow

from reana_commons.errors import REANAValidationError
from reana_commons.config import SNAKEMAKE_MAX_PARALLEL_JOBS


def snakemake_validate(
    workflow_file: str, configfiles: List[str], workdir: Optional[str] = None
):
    """Validate Snakemake workflow."""
    if sys.version_info >= (3, 11):
        snakemake_validate_v8(workflow_file, configfiles, workdir)
    else:
        snakemake_validate_v7(workflow_file, configfiles, workdir)


def snakemake_load(workflow_file: str, **kwargs: Any):
    """Load Snakemake specification."""
    if sys.version_info >= (3, 11):
        return snakemake_load_v8(workflow_file, **kwargs)
    else:
        return snakemake_load_v7(workflow_file, **kwargs)


def snakemake_validate_v7(
    workflow_file: str, configfiles: List[str], workdir: Optional[str] = None
):
    """Snakemake 7 workflow validation function, necessary for Python versions < 3.11.

    :param workflow_file: A specification file compliant with
        `snakemake` workflow specification.
    :type workflow_file: string
    :param configfiles: List of config files paths.
    :type configfiles: List
    :param workdir: Path to working directory.
    :type workdir: string or None
    """
    valid = snakemake(
        snakefile=workflow_file,
        configfiles=configfiles,
        workdir=workdir,
        dryrun=True,
        quiet=True,
    )
    if not valid:
        raise REANAValidationError("Snakemake specification is invalid.")


def snakemake_validate_v8(
    workflow_file: str, configfiles: List[str], workdir: Optional[str] = None
):
    """Snakemake 8 workflow validation function for Python versions >= 3.11.

    Note that we may move to using snakemake --dry-run when the validation process will be fully moved to the server side.

    :param workflow_file: A specification file compliant with
        `snakemake` workflow specification.
    :type workflow_file: string
    :param configfiles: List of config files paths.
    :type configfiles: List
    :param workdir: Path to working directory.
    :type workdir: string or None
    """
    with SnakemakeApi(
        OutputSettings(
            quiet=True,
        )
    ) as snakemake_api:
        try:
            workflow_api = snakemake_api.workflow(
                resource_settings=ResourceSettings(nodes=SNAKEMAKE_MAX_PARALLEL_JOBS),
                config_settings=ConfigSettings(configfiles=configfiles),
                storage_settings=StorageSettings(),
                storage_provider_settings=dict(),
                workflow_settings=WorkflowSettings(),
                deployment_settings=DeploymentSettings(),
                snakefile=workflow_file,
                workdir=workdir,
            )

            workflow_api.dag()

        except Exception as e:
            snakemake_api.print_exception(e)
            raise REANAValidationError("Snakemake specification is invalid.")


def snakemake_load_v7(workflow_file: str, **kwargs: Any):
    """Load Snakemake workflow specification into an internal representation. Used for python <3.11 and it is needed since snakemake8 dropped support for python 3.11.

    :param workflow_file: A specification file compliant with
        `snakemake` workflow specification.
    :type workflow_file: string

    :returns: Dictonary containing relevant workflow metadata.
    """

    def _create_snakemake_dag(
        snakefile: str, configfiles: Optional[List[str]] = None, **kwargs: Any
    ) -> DAG:
        """Create ``snakemake.dag.DAG`` instance.

        The code of this function comes from the Snakemake codebase and is adapted
        to fullfil REANA purposes of getting the needed metadata.

        If `workdir` is passed as a keyword argument, then this function will change the
        CWD to `workdir`.

        :param snakefile: Path to Snakefile.
        :type snakefile: string
        :param configfiles: List of config files paths.
        :type configfiles: List
        :param kwargs: Snakemake args.
        :type kwargs: Any
        """
        overwrite_config = dict()
        if configfiles is None:
            configfiles = []
        for f in configfiles:
            # get values to override. Later configfiles override earlier ones.
            overwrite_config.update(load_configfile(f))
        # convert provided paths to absolute paths
        configfiles = list(map(os.path.abspath, configfiles))
        workflow = Workflow(
            snakefile=snakefile,
            overwrite_configfiles=configfiles,
            overwrite_config=overwrite_config,
        )

        workdir = kwargs.get("workdir")
        if workdir:
            workflow.workdir(workdir)

        workflow.include(snakefile=snakefile, overwrite_default_target=True)
        workflow.check()

        # code copied and adapted from `snakemake.workflow.Workflow.execute()`
        # in order to build the DAG and calculate the job dependencies.
        # https://github.com/snakemake/snakemake/blob/75a544ba528b30b43b861abc0ad464db4d6ae16f/snakemake/workflow.py#L525
        def rules(items):
            return map(
                workflow._rules.__getitem__,
                filter(workflow.is_rule, items),
            )

        if kwargs.get("keep_target_files"):

            def files(items):
                return filterfalse(workflow.is_rule, items)

        else:

            def files(items):
                def relpath(f):
                    return (
                        f
                        if os.path.isabs(f) or f.startswith("root://")
                        else os.path.relpath(f)
                    )

                return map(relpath, filterfalse(workflow.is_rule, items))

        if not kwargs.get("targets"):
            targets = (
                [workflow.default_target]
                if workflow.default_target is not None
                else list()
            )

        prioritytargets = kwargs.get("prioritytargets", [])
        forcerun = kwargs.get("forcerun", [])
        until = kwargs.get("until", [])
        omit_from = kwargs.get("omit_from", [])

        priorityrules = set(rules(prioritytargets))
        priorityfiles = set(files(prioritytargets))
        forcerules = set(rules(forcerun))
        forcefiles = set(files(forcerun))
        untilrules = set(rules(until))
        untilfiles = set(files(until))
        omitrules = set(rules(omit_from))
        omitfiles = set(files(omit_from))

        targetrules = set(
            chain(
                rules(targets),
                filterfalse(Rule.has_wildcards, priorityrules),
                filterfalse(Rule.has_wildcards, forcerules),
                filterfalse(Rule.has_wildcards, untilrules),
            )
        )
        targetfiles = set(chain(files(targets), priorityfiles, forcefiles, untilfiles))
        dag = DAG(
            workflow,
            workflow.rules,
            targetrules=targetrules,
            targetfiles=targetfiles,
            omitfiles=omitfiles,
            omitrules=omitrules,
        )

        if hasattr(workflow, "_persistence"):
            workflow._persistence = Persistence(dag=dag)
        else:
            # for backwards compatibility (Snakemake < 7 for Python 3.6)
            workflow.persistence = Persistence(dag=dag)
        dag.init()
        dag.update_checkpoint_dependencies()
        dag.check_dynamic()
        return dag

    workdir = kwargs.get("workdir")
    if workdir:
        workflow_file = os.path.join(workdir, workflow_file)

    configfiles = [kwargs.get("input")] if kwargs.get("input") else []

    snakemake_validate(
        workflow_file=workflow_file, configfiles=configfiles, workdir=workdir
    )

    # save the cwd to restore it after _create_snakemake_dag, because this function
    # changes the cwd if `workdir` is in `kwargs`
    prev_cwd = os.getcwd()
    try:
        snakemake_dag = _create_snakemake_dag(
            workflow_file, configfiles=configfiles, **kwargs
        )
    finally:
        os.chdir(prev_cwd)

    job_dependencies = {
        str(job): list(map(str, deps.keys()))
        for job, deps in snakemake_dag.dependencies.items()
    }

    return {
        "job_dependencies": job_dependencies,
        "steps": [
            {
                "name": rule.name,
                "environment": (rule._container_img or "").replace("docker://", ""),
                "inputs": dict(rule._input),
                "params": dict(rule._params),
                "outputs": dict(rule._output),
                "commands": [rule.shellcmd],
                "compute_backend": rule.resources.get("compute_backend"),
                "kubernetes_memory_limit": rule.resources.get(
                    "kubernetes_memory_limit"
                ),
                "kubernetes_uid": rule.resources.get("kubernetes_uid"),
            }
            for rule in snakemake_dag.rules
            if not rule.norun
        ],
    }


def snakemake_load_v8(workflow_file: str, **kwargs: Any):
    """Load Snakemake workflow specification into an internal representation.

    :param workflow_file: A specification file compliant with
        `snakemake` workflow specification.
    :type workflow_file: string

    :returns: Dictonary containing relevant workflow metadata.
    """
    workdir = kwargs.get("workdir")
    if workdir:
        workflow_file = os.path.join(workdir, workflow_file)

    workflow_file = Path(workflow_file)  # convert str to Path
    configfiles = [Path(kwargs.get("input"))] if kwargs.get("input") else []

    snakemake_validate(
        workflow_file=workflow_file, configfiles=configfiles, workdir=workdir
    )

    return {
        "job_dependencies": {},
        "steps": [],
    }
