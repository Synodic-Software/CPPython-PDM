"""Implementation of the PDM Interface Plugin
"""

from cppython.project import Project as CPPythonProject
from cppython_core.schema import (
    Interface,
    InterfaceConfiguration,
    ProjectConfiguration,
    ProviderDataT,
)
from pdm.core import Core
from pdm.models.candidates import Candidate
from pdm.project.core import Project
from pdm.signals import post_install


class CPPythonPlugin(Interface):
    """Implementation of the PDM Interface Plugin"""

    def __init__(self, interface_configuration: InterfaceConfiguration) -> None:
        post_install.connect(self.on_post_install, weak=False)

        super().__init__(interface_configuration)

    @staticmethod
    def name() -> str:
        """Name of the plugin

        Returns:
            The name
        """
        return "pdm"

    def read_provider_data(self, provider_data_type: type[ProviderDataT]) -> ProviderDataT:
        """Constructs type

        Args:
            provider_data_type: The type to construct

        Returns:
            Provider data type constructed
        """
        return provider_data_type()

    def write_pyproject(self) -> None:
        """Write to file"""

    def on_post_install(self, project: Project, candidates: dict[str, Candidate], dry_run: bool) -> None:
        """Called after a pdm install command is called

        Args:
            project: The input PDM project
            candidates: The candidates installed
            dry_run: If true, won't perform any actions
        """

        pyproject_file = project.pyproject_file.absolute()

        # Attach configuration for CPPythonPlugin callbacks
        project_configuration = ProjectConfiguration(pyproject_file=pyproject_file, version=project.core.version)
        project_configuration.verbosity = project.core.ui.verbosity

        logger = self.logger()
        logger.info("CPPython: Entered 'on_post_install'")

        if (pdm_pyproject := project.pyproject) is None:
            logger.info("CPPython: Project data was not available")
            return

        cppython_project = CPPythonProject(project_configuration, self, pdm_pyproject)

        if not dry_run:
            cppython_project.install()


def pdm_entry_point(core: Core) -> None:
    """_summary_

    Args:
        core: _description_
    """
    core.version
    interface_configuration = InterfaceConfiguration()

    CPPythonPlugin(interface_configuration)
