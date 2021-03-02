from dadjoke import dadjoke

def chatbot(text):
    if "tell" in text and "joke" in text:
        return dadjoke()
    else:
        return "Some response"