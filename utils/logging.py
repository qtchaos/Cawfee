import time


def log(message: str):
    if len(message) == 0:
        return

    t = time.time()
    log_time = time.ctime(t).split(" ")[3]

    print(f"{log_time} [*] {message}")



