import requests

from utils.io import read_key, register_key, save_line
from utils.logging import Logger


class Plugin:
    """
    Name: PortScan
    Author: qtchaos
    Version: 1.0.0
    """

    @staticmethod
    def execute():
        """ Runs when the plugin is executed. """
        main()


LOGGER = Logger("PortScan")


def main():
    url = "https://leakix.net/search?page=0&q=%2Bplugin%3AMongoOpenPlugin&scope=leak"

    headers = {
        "cookie":
        "LEAKIX_FLASH=; LEAKIX_SESSION=b64050dd256cc0896ca03e44ceeae196513ba095-%2500_TS%253A1671581828"
        "%2500%2500csrf_token%253AKw%252FBeR96HGH0%252FFLmllPDcFHVEB7mcD%252FSg0cOJ%252BxS5L8%253D%2500",
        "Accept":
        "application/json"
    }

    response = requests.request("GET", url, headers=headers)
    print(response.text)
    for i in response.json():
        try:
            LOGGER.log(
                f"{i['ip']} {i['geoip']['country_name']} {i['summary']}")
        except KeyError:
            LOGGER.log(f"{i['ip']} {i['geoip']['country_name']}")
