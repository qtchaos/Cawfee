import importlib
import os
from multiprocessing import Process

from data.LoadedPlugin import LoadedPlugin
from data.Plugins import plugins
from utils.logging import log


def choose_plugins(state: str = "choose"):
    if state == "choose":
        log("Please choose a plugin to execute:")
        for plugin in plugins.values():
            log(f"└──▷ {plugin.get_name()}")
        log("└──▷ All")

    input_name = input("> ")
    if input_name in plugins:
        execute_plugin(plugins, name=input_name)
    elif input_name.lower() == "all":
        execute_plugin(plugins, execute_all=True)
    else:
        log("Failed to execute plugin: Invalid name.")
        choose_plugins(state="invalid_input")


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


def execute_plugin(plugins_l: list, execute_all: bool = False, name: str = None):
    processes = []
    if not execute_all and name is None:
        log("Failed to execute plugins: No name provided.")
        return

    if execute_all:
        for plugin in plugins_l.values():
            processes.append(Process(target=plugin.get_executor()))
    elif name in plugins_l:
        processes.append(Process(target=plugins_l[name].get_executor()))

    for process in processes:
        process.start()

    log(f"Executed {len(plugins_l)} plugin{multiple()} successfully.")


def multiple():
    return 's' if len(plugins) != 1 else ''
