"""
TODO
"""
import pytest
from pdm import Core
from pdm.cli.commands.run import run_script_if_present
from pytest_cppython.plugin import InterfaceUnitTests

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

        return CPPythonPlugin(Core())

    def test_install(self, interface: CPPythonPlugin):
        """
        TODO
        """

        runner = run_script_if_present("post_install")
        runner()
        # signals.post_install.connect(, weak=False)

        # interface.on_post_install(project=Project(Core(), None), candidates={}, dry_run=False)
