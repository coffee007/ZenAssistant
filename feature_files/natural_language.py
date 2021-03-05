from fuzzywuzzy import fuzz
import nltk
import json

file = open("data/intents.json", 'r+')
intents = json.load(file)