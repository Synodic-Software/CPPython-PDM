from cppython.schema import Interface
from pdm.cli.commands.base import BaseCommand
from pdm.project.config import ConfigItem


class HelloCommand(BaseCommand):
    """Say hello to the specified person.
    If none is given, will read from "hello.name" config.
    """

    def add_arguments(self, parser):
        parser.add_argument("-n", "--name", help="the person's name to whom you greet")

    def handle(self, project, options):
        if not options.name:
            name = project.config["hello.name"]
        else:
            name = options.name
        print(f"Hello, {name}")


def cppython_plugin(core):
    core.register_command(HelloCommand, "hello")
    core.add_config("hello.name", ConfigItem("The person's name", "John"))


class PDMInterface(Interface):
    pass
