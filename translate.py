"""."""

import time

import pyperclip
from googletrans import Translator
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer


def copyText():
    """Text tlanslate and copy."""
    text = ""
    with open("tool.txt", encoding="utf-8_sig") as f:
        for x in f:
            x = x.replace('\r\n', '\n')
            x = x.replace('\n', ' ')
            x = x.replace(' .', ', ')
            x = x.replace('. ', '.')
            x = x.replace('.', '.\n')
            x = x.replace('{', '(')
            x = x.replace('}', ')')
            x = x.replace('\\', ' ')
            x = x.replace('􀀀', '')
            text += x[:-1]
    text = translateText(text)
    pyperclip.copy(text)
    print(text)


def translateText(text):
    """Text tlanslate."""
    return Translator().translate(text, dest='ja').text


class ChangeHandler(PatternMatchingEventHandler):
    """."""

    def __init__(self):
        """."""
        super(ChangeHandler, self).__init__(patterns=["*tool.txt*"])

    def on_modified(self, event):
        """."""
        copyText()
        # print("\n\n\n\n\n")


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
