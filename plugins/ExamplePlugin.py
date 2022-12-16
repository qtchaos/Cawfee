from utils.logging import log


class Plugin:
    """
    Name: Example Plugin
    Author: Example Author
    Version: 1.0.0
    """

    @staticmethod
    def execute():
        """ Runs when the plugin is executed. """
        main()


def main():
    log("Hello from Example Plugin")
