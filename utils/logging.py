import time


class Logger:
    def __init__(self, identifier: str = "*"):
        self.identifier = identifier

    def log(self, message: str):
        if len(message) == 0:
            return

        t = time.time()
        log_time = time.ctime(t).split(" ")[3]

        print(f"{log_time} [{self.identifier}] {message}")
