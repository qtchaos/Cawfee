import time
from typing import Optional


class Logger:

    def __init__(self, identifier: str = "*"):
        self.identifier = identifier

    def log(self, message: str) -> None:
        if len(message) == 0:
            return

        t = time.time()
        time_string = time.strftime("%H:%M:%S", time.localtime(t))
        print(f"{time_string} [{self.identifier}] {message}")
