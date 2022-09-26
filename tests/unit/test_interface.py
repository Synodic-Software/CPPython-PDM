"""Unit tests for the interface
"""

from pathlib import Path

import pytest
from cppython_core.schema import PEP621, CPPythonData, PyProject, TargetEnum, ToolData
from pdm.core import Core
from pytest_cppython.plugin import InterfaceUnitTests
from pytest_mock.plugin import MockerFixture

from cppython_pdm.plugin import CPPythonPlugin

default_pep621 = PEP621(name="test_name", version="1.0")
default_cppython_data = CPPythonData(target=TargetEnum.EXE)
default_tool_data = ToolData(cppython=default_cppython_data)
default_pyproject = PyProject(project=default_pep621, tool=default_tool_data)


class TestCPPythonInterface(InterfaceUnitTests[CPPythonPlugin]):
    """The tests for the PDM interface"""

    @pytest.fixture(name="interface_type")
    def fixture_interface_type(self) -> type[CPPythonPlugin]:
        """A required testing hook that allows type generation

        Returns:
            The plugin type
        """

        return CPPythonPlugin

    @pytest.fixture(name="interface")
    def fixture_interface(self, interface_type: type[CPPythonPlugin]) -> CPPythonPlugin:
        """A hook allowing implementations to override the fixture

        Args:
            interface_type: An input interface type

        Returns:
            A newly constructed interface
        """
        return interface_type(Core())

    def test_install(self, interface: CPPythonPlugin, mocker: MockerFixture) -> None:
        """Tests the post install path

        Args:
            interface: The constructed plugin
            mocker: Mocker fixture for project mocking
        """

        pdm_project = mocker.MagicMock()
        pdm_project.core.ui.verbosity = 0
        pdm_project.core.version = "1.0.0"
        pdm_project.pyproject_file = Path("pyproject.toml")
        pdm_project.pyproject = dict(default_pyproject)

        interface.on_post_install(project=pdm_project, candidates={}, dry_run=False)
