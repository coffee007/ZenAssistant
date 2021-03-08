import pywhatkit


def googleSearch(query):
    try:
        pywhatkit.search(query)
    except Exception as e:
        print(e)

def YoutubeSearch(query):
    try:
        pywhatkit.playonyt(query)
    except Exception as e:
        print(e)