import importlib
import os
from multiprocessing import Process

from data.LoadedPlugin import LoadedPlugin
from data.Plugins import plugins
from utils.logging import log


def load_plugins():
    log("Loading plugins...")
    importlib.invalidate_caches()
    for file in os.listdir("plugins"):
        if file.endswith(".py"):
            plugin_name = file[:-3]

            plugin_module = importlib.import_module(f"plugins.{plugin_name}", ".")
            plugin_class = getattr(plugin_module, "Plugin")
            LoadedPlugin(plugin_class())

    log(f"Loaded {len(plugins)} plugin{multiple()} successfully.")


def execute_plugin(plugins: list, execute_all: bool = False, name: str = None):
    processes = []
    if not execute_all and name is None:
        log("Failed to execute plugins: No name provided.")
        return

    if execute_all:
        for plugin in plugins.values():
            processes.append(Process(target=plugin.get_executor()))
    elif name in plugins:
        processes.append(Process(target=plugins[name].get_executor()))

    for process in processes:
        process.start()

    log(f"Executed {len(plugins)} plugin{multiple()} successfully.")


def multiple():
    return 's' if len(plugins) != 1 else ''
