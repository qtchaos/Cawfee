import os

from utils.io import initialize_config, register_key

from utils.logging import log
from utils.plugin import load_plugins, choose_plugins


def main():
    log("Brewing a fresh cup of coffee...")
    if not os.path.exists("config.json"):
        initialize_config()
    load_plugins()
    choose_plugins()


if __name__ == '__main__':
    main()

