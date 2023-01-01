import os

from utils.io import initialize_config
from utils.logging import Logger
from utils.plugin import choose_plugins, load_plugins

LOGGER = Logger()

x = {  "a": "b"      }
def main():
    LOGGER.log("Brewing a fresh cup of coffee...")
    if not os.path.exists("config.json"):
        initialize_config()
    load_plugins()
    choose_plugins()


if __name__ == '__main__':
    main()
