import randfacts


def RandomFacts():
    try:
        x = randfacts.getFact()
        return x
    except Exception as e:
        print(e)
        return e
        
    

