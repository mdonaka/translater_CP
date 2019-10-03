"""."""

import time

import pyperclip
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer
from google_trans import trans 


def copyText():
    """Text tlanslate and copy."""
    text = ""
    with open("english.txt", encoding="utf-8_sig") as f:
        for x in f:
            x = x.replace('\r\n', '\n')
            x = x.replace('\n', ' ')
            x = x.replace(' .', ', ')
            x = x.replace('. ', '.')
            x = x.replace('i.e.', 'ie')
            x = x.replace('.', '.\n')
            x = x.replace('{', '(')
            x = x.replace('}', ')')
            x = x.replace('\\', ' ')
            x = x.replace('􀀀', '')
            x = x[:-2] if x[-2:] == "- " else x
            text += x
    print(text)
    text = translateText(text)
    pyperclip.copy(text)
    print(text)


def translateText(text):
    """Text tlanslate."""
    return trans(text)


class ChangeHandler(PatternMatchingEventHandler):
    """."""

    def __init__(self):
        """."""
        super(ChangeHandler, self).__init__(patterns=["*english.txt*"])

    def on_modified(self, event):
        """."""
        copyText()
        print("\n")


if __name__ == "__main__":
    e = ChangeHandler()
    observer = Observer()
    observer.schedule(e, "./", recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
