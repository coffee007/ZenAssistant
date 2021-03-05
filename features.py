from feature_files.dadjoke import dadjoke
from feature_files.WebSearch import googleSearch
from feature_files.text_summarizer import summary
from feature_files.OpenApps import OpenAPP
from feature_files.Dictionary import GiveAntonym, GiveSynonym, GiveMeaning
from feature_files.RandomFacts import RandomFacts
from feature_files.Weather import Weather


class Assistant():
    def __init__(self, name):
        self.name = name

    def dadjoke(self, reqs_confirm=False):
        return dadjoke()

    def GoogleSearch(self, query='', reqs_confirm=True):
        if reqs_confirm:
            return dict({"error": "Please enter what you wish to search for: "})
        return googleSearch(query)

    def summarize_text(self, text='', reqs_confirm=True):
        if reqs_confirm:
            return dict({"error": "Please enter a paragraph you want to summarize. It should have more than 5 sentences. "})
        return summary(text)

    def RandomFacts(self, reqs_confirm=False):
        return RandomFacts()

    def OpenApp(self, text='', reqs_confirm=True):
        if reqs_confirm:
            return dict({"error": "Which app do you want to open? "})
        OpenAPP(text)
        return "App opened"

    def GiveMeaning(self, query='', reqs_confirm=True):
        if reqs_confirm:
            return dict({"error": "Which word's meaning should I show? "})
        return GiveMeaning(query)

    def GiveSynonym(self, query='', reqs_confirm=True):
        if reqs_confirm:
            return dict({"error": "Which word's synonyms should I show? "})
        return GiveSynonym(query)

    def GiveAntonym(self, query='', reqs_confirm=True):
        if reqs_confirm:
            return dict({"error": "Which word's antonyms should I tell you? "})
        return GiveAntonym(query)

    def Weather(self, reqs_confirm=False):
        Weather()
        return "Showing weather"
