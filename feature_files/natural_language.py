from fuzzywuzzy import fuzz
import json
import random

file = open("feature_files/data/intents.json", 'r+')
file2 = open("feature_files/data/commands_and_intents.json", "r+")
intents = list(dict(json.load(file)).get("intents"))
commands = list(dict(json.load(file2)).get("commands"))


def talk(text, chat_history = ''):
    text = text.lower()
    max_match = {"intent": "Sorry, I didn't get that.", "match": 50}
    for command in commands:
        command = dict(command)
        for j in list(command.get("patterns")):
            n = fuzz.ratio(text, j)
            if n > max_match.get("match"):
                max_match["match"] = n
                max_match["intent"] = list(command.get("commands"))[0]
    if max_match["match"] > 80:
        return [max_match.get("intent"), "function"]
    max_match = {"intent": "Sorry, I didn't get that.", "match": 50}
    for intent in intents:
        intent = dict(intent)
        for i in list(intent.get("patterns")):
            m = fuzz.ratio(text, i)
            if m > max_match.get("match"):
                max_match["match"] = m
                max_match["intent"] = random.choice(list(intent.get("responses")))

    return [max_match.get("intent"), "response"]



