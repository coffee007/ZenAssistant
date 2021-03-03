from features import Assistant

bot = Assistant("Zen")

joke = ["joke", "laugh", "funny"]
name = ["name", "who are you"]
google = ["google", "search"]
summary = ["summary"]

while True:
    text = input("Enter message: ").lower()
    if any(word in joke for word in text.split()):
        print(bot.dadjoke())
    elif any(word in name for word in text.split()):
        print("My name is {}".format(bot.name))
    elif any(word in google for word in text.split()):
        print(bot.GoogleSearch(text))
    elif any(word in summary for word in text.split()):
        print(bot.summarize_text(text))
