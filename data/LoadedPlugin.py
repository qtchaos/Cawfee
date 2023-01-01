import zlib

from data import Plugins
from utils.parsing import parse_docstring


class LoadedPlugin:
    """ Plugin's data and execute object. """

    def __init__(self, plugin: object):
        doc_data = parse_docstring(str(plugin.__doc__))
        self.name = doc_data["Name"]
        self.author = doc_data["Author"]
        self.version = doc_data["Version"]
        self.execute = plugin.execute  # type: ignore
        Plugins.plugins[self.name] = self

    def get_executor(self):
        return self.execute

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    def get_version(self):
        return self.version

    def get_crc32(self):
        concat_string = f"{self.name}{self.author}{self.version}"
        hex_hash = hex(zlib.crc32(concat_string.encode("utf-8")) & 0xffffffff)
        return str(hex_hash[2:])
