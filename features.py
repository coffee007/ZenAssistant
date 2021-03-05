from feature_files.dadjoke import dadjoke
from feature_files.WebSearch import googleSearch
from feature_files.text_summarizer import summary
from feature_files.OpenApps import OpenAPP
from feature_files.Dictionary import GiveAntonym ,GiveSynonym,GiveMeaning


class Assistant():
    def __init__(self, name):
        self.name = name

    def dadjoke(self):
        return dadjoke()

    def GoogleSearch(self, query):
        return googleSearch(query)

    def summarize_text(self, text):
        return summary(text)

    def OpenApp(self,text):
        OpenAPP(text)

    def GiveMeaning(self, query):
        GiveMeaning(query)

    def GiveSynonym(self, query):
        GiveSynonym(query)

    def GiveAntonym(self, query):
        GiveAntonym(query)
