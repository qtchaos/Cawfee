import json
import os
from typing import Optional

from utils.logging import Logger

config_file = "config.json"
LOGGER = Logger("IO")


def initialize_config():
    with open(config_file, "w") as file:
        file.write(json.dumps({"plugins": {}}, indent=2))


def register_key(key: dict,
                 plugin_name: str,
                 alert_message: Optional[str] = None) -> None:
    """
    Registers a key value pair in the config file, an alert message can be provided to be displayed to the user.
    If the key already exists, nothing will happen.
    """
    with open(config_file, "r+") as file:
        data = json.loads(file.read())
        if plugin_name not in data["plugins"]:
            data["plugins"][plugin_name] = json.loads(json.dumps({}, indent=2))

        if list(key)[0] not in data["plugins"][plugin_name]:
            data["plugins"][plugin_name].update(key)
            file.seek(0)
            file.write(json.dumps(data, indent=2))
            file.truncate()

        if data["plugins"][plugin_name].get(list(key.keys())[0]) == key[list(
                key.keys())[0]]:
            if alert_message is not None:
                LOGGER.log(f"{plugin_name}: {alert_message}")


def update_key(key: str, value: str, plugin_name: str) -> None:
    """
    Updates a key value pair in the config file.
    """
    with open(config_file, "r+") as file:
        data = json.loads(file.read())
        data["plugins"][plugin_name][key] = value
        file.seek(0)
        file.write(json.dumps(data, indent=2))
        file.truncate()


def read_key(key: str, plugin_name: str) -> str:
    """
    Reads a key value pair from the config file.
    """
    with open(config_file, "r") as file:
        data = json.loads(file.read())
        return data["plugins"][plugin_name][key]


def save_line(line: str, plugin_name: str) -> None:
    if not os.path.exists("loot"):
        os.mkdir("loot")

    with open(f"loot/{plugin_name}.txt", "a") as file:
        file.writelines(f"{line}\n")
