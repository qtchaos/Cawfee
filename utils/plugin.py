import importlib
import os
from multiprocessing import Process
from typing import Optional

from data import LoadedPlugin, plugins
from utils.logging import Logger

LOGGER = Logger("PluginLoader")


def choose_plugins(state: str = "choose") -> None:
    if state == "choose":
        LOGGER.log("Please choose a plugin to execute:")
        for plugin in plugins.values():
            LOGGER.log(f"└──▷ {plugin.get_name()}")  # type: ignore
        LOGGER.log("└──▷ All")

    try:
        input_name = input("> ")
    except KeyboardInterrupt:
        print("")
        LOGGER.log("Exiting...")
        exit(0)

    if input_name in plugins:
        execute_plugin(plugins, name=input_name)
    elif input_name.lower() == "all":
        execute_plugin(plugins, execute_all=True)
    else:
        LOGGER.log("Failed to execute plugin: Invalid name.")
        choose_plugins(state="invalid_input")


def load_plugins() -> None:
    LOGGER.log("Loading plugins...")
    importlib.invalidate_caches()
    for file in os.listdir("plugins"):
        if file.endswith(".py"):
            plugin_name = file[:-3]

            plugin_module = importlib.import_module(f"plugins.{plugin_name}",
                                                    ".")
            plugin_class = getattr(plugin_module, "Plugin")
            LoadedPlugin(plugin_class())

    LOGGER.log(f"Loaded {len(plugins)} plugin{multiple()} successfully.")


def execute_plugin(plugins_l: dict[str, LoadedPlugin],
                   execute_all: bool = False,
                   name: Optional[str] = None) -> None:
    processes = []
    process_len = 1
    if not execute_all and name is None:
        LOGGER.log("Failed to execute plugins: No name provided.")
        return

    if execute_all:
        for plugin in plugins_l.values():
            processes.append(Process(target=plugin.get_executor()))
            process_len = len(plugins_l)
    elif name in plugins_l:
        processes.append(Process(target=plugins_l[name].get_executor()))

    for process in processes:
        process.start()

    LOGGER.log(f"Executed {process_len} plugin{multiple()} successfully.")


def multiple() -> str:
    return 's' if len(plugins) != 1 else ''
