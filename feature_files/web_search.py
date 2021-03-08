import pywhatkit


def googleSearch(query):
    try:
        pywhatkit.search(query)
    except Exception as e:
        print(e)
    return "Searching Google"

def YoutubeSearch(query):
    try:
        pywhatkit.playonyt(query)
    except Exception as e:
        print(e)