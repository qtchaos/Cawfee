from utils.io import read_key, register_key, update_key
from utils.logging import Logger


class Plugin:
    """
    Name: Example Plugin
    Author: Example Author
    Version: 1.0.0
    """

    def __init__(self):
        """ Registers values in the config file. """
        register_key({"key": "value"}, "ExamplePlugin",
                     "This is an example alert message.")

    @staticmethod
    def execute():
        """ Runs when the plugin is executed. """
        main()


LOGGER = Logger("ExamplePlugin")


def main():
    KEY_FROM_CONFIG = read_key("key", "ExamplePlugin")
    LOGGER.log("Hello from Example Plugin")
    if KEY_FROM_CONFIG == "value":
        update_key("key", "new value", "ExamplePlugin")
