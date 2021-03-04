import PyDictionary
import random


# returns meaning of a word
def GiveMeaning(query):
    meaning = PyDictionary.PyDictionary.meaning(str(query))
    return meaning[0]


# returns synonym of a word
def GiveSynonym(query):
    synonym = PyDictionary.PyDictionary.synonym(str(query))
    return synonym[0]


# returns antonym of a word
def GiveAntonym(query):
    antonym = PyDictionary.PyDictionary.antonym(str(query))
    return antonym[0]



