import pywhatkit


def googleSearch(query):
    try:
        pywhatkit.search(query)
    except Exception as e:
        return e

def YoutubeSearch(query):
    try:
        pywhatkit.playonyt(query)
    except Exception as e:
        return e