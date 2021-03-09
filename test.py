import threading
from feature_files.speak_and_get_audio import get_audio


def mainLoop():
    said = get_audio()


def start():
    AudioInputThread = threading.Thread(target=mainLoop, name="t1", daemon=True)
    AudioInputThread.start()

start()