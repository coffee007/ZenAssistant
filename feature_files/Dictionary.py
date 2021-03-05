import PyDictionary


# returns meaning of a word
def GiveMeaning(query):
    try:
        meaning = PyDictionary.PyDictionary(str(query)).getMeanings()
        return [dict(meaning.get(str(query))).get(x)[0] for x in list(dict(meaning.get(str(query))).keys())][0].capitalize()
    except Exception as e:
        print(e)
        return "No meaning found."


# returns synonym of a word
def GiveSynonym(query):
    try:
        synonym = PyDictionary.PyDictionary.synonym(str(query))
        return synonym[0].capitzalize()
    except:
        return "No synonyms found."

# returns antonym of a word
def GiveAntonym(query):
    try:
        antonym = PyDictionary.PyDictionary.antonym(str(query))
        return antonym[0].capitalize()
    except:
        return "No antonym found."

