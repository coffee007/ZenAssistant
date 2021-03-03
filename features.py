from dadjoke import dadjoke
import GoogleSearch


class Assistant():
    def __init__(self, name):
        self.name = name

    def dadjoke(self):
        dadjoke()

    def GoogleSearch(self, query):
        GoogleSearch.GoogleSearch(query)
