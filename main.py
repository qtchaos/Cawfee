from data.Plugins import plugins

from utils.logging import log
from utils.plugin import execute_plugin, load_plugins


def main():
    log("Brewing a fresh cup of coffee...")
    load_plugins()
    execute_plugin(plugins, True)


if __name__ == '__main__':
    main()

