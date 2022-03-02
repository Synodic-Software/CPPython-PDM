"""
TODO
"""

from typing import Type

from cppython.project import Project as CPPythonProject
from cppython.schema import GeneratorDataType, Interface, PyProject
from pdm import Core, Project
from pdm.models.candidates import Candidate
from pdm.signals import post_install


class PDMInterface(Interface):
    """
    TODO
    """

    def read_generator_data(self, generator_data_type: Type[GeneratorDataType]) -> GeneratorDataType:
        return generator_data_type()

    def write_pyproject(self) -> None:
        pass


def on_post_install(project: Project, candidates: dict[str, Candidate], dry_run: bool):
    """
    TODO
    """

    # Don't operate on the plugin project
    if project.meta.name == "cppython-pdm":
        return

    pyproject = PyProject(**project.config)
    interface = PDMInterface(pyproject)
    cppython_project = CPPythonProject(interface)


def cppython_plugin(core: Core):
    """
    TODO
    """
    post_install.connect(on_post_install)
