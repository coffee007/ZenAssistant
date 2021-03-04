import PyDictionary


# returns meaning of a word
def GiveMeaning(query):
    meaning = PyDictionary.PyDictionary.meaning("morning")
    if meaning is None:
        return "No meanings found. Please try again."
    else:
        x = []
        for i in meaning.get(list(meaning.keys())[0]):
            x.append(str(i).capitalize())
        return str('\n'.join(x))


print(GiveMeaning("morning"))