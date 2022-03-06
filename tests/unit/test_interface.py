"""
TODO
"""

import pdm
import pytest
from cppython.plugins.test.data import default_pyproject
from cppython.plugins.test.pytest import InterfaceUnitTests
from cppython.schema import API
from pytest_mock import MockerFixture

from cppython_pdm.plugin import CPPythonPlugin


class TestCPPythonInterface(InterfaceUnitTests):
    """
    The tests for the PDM interface
    """

    @pytest.fixture(name="interface")
    def fixture_interface(self) -> CPPythonPlugin:
        """
        Override of the plugin provided interface fixture.

        Returns:
            ConsoleInterface -- The Interface object to use for the CPPython defined tests
        """

        return CPPythonPlugin(pdm.Core())

    def test_install(self, interface: CPPythonPlugin, mocker: MockerFixture):
        """
        _summary_

        Arguments:
            command {str} -- The CLI command with the same name as the CPPython API call
            mocker {MockerFixture} -- pytest-mock fixture
        """
        # Patch the project initialization
        mocker.patch("cppython.project.Project.__init__", return_value=None)

        interface.on_post_install

        # Patch the reading of data
        mocker.patch("cppython.plugins.interface.console._create_pyproject", return_value=default_pyproject)

        # Patch out the implementation
        mocked_command = mocker.patch("cppython.project.Project.install")
        mocked_command.assert_called_once()
