"""
TODO
"""

import pytest
from cppython.plugins.test.data import default_pyproject
from cppython.plugins.test.pytest import InterfaceIntegrationTests

from cppython_pdm.plugin import PDMInterface


class TestCPPythonInterface(InterfaceIntegrationTests):
    """
    The tests for the PDM interface
    """

    @pytest.fixture(name="interface")
    def fixture_interface(self) -> PDMInterface:
        """
        Override of the plugin provided interface fixture.

        Returns:
            ConsoleInterface -- The Interface object to use for the CPPython defined tests
        """
        return PDMInterface(default_pyproject)
