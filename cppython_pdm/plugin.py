"""
TODO
"""

import logging
from typing import Type

from cppython.project import Project as CPPythonProject
from cppython.project import ProjectConfiguration
from cppython_core.schema import GeneratorDataT, Interface, InterfaceConfiguration
from pdm import Core, Project
from pdm.models.candidates import Candidate
from pdm.signals import post_install


class CPPythonPlugin(Interface):
    """
    TODO
    """

    def __init__(self, core: Core) -> None:

        # NOTE: Verbosity is not filled by PDM
        self.project_configuration = ProjectConfiguration()
        self.project_configuration.verbosity = core.ui.verbosity
        self.project = None

        self.logger = logging.getLogger("cppython")

        post_install.connect(self.on_post_install, weak=False)

        interface_configuration = InterfaceConfiguration()
        super().__init__(interface_configuration)

    @staticmethod
    def name() -> str:
        """
        TODO
        """
        return "pdm"

    def read_generator_data(self, generator_data_type: Type[GeneratorDataT]) -> GeneratorDataT:
        """
        TODO
        """
        return generator_data_type()

    def write_pyproject(self) -> None:
        """
        TODO:
        """

    def on_post_install(self, project: Project, candidates: dict[str, Candidate], dry_run: bool):
        """
        TODO
        """

        # Attach configuration for CPPythonPlugin callbacks
        self.project = project
        self.project_configuration.verbosity = bool(project.core.ui.verbosity)

        self.logger.info("CPPython: Entered 'on_post_install'")

        pdm_pyproject = project.pyproject

        if pdm_pyproject is None:
            self.logger.info("CPPython: Project data was not available")
            return

        cppython_project = CPPythonProject(self.project_configuration, self, pdm_pyproject)

        cppython_project.install()
