import time

import pyperclip


def copy(text: str, ttl_secs: int = 10):
    pyperclip.copy(text)
    try:
        time.sleep(ttl_secs)
    except KeyboardInterrupt:
        pass
    finally:
        pyperclip.copy("")
