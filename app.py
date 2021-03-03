from features import Assistant

bot = Assistant("Zen")

joke = ["joke", "laugh", "funny"]

while True:
    text = input("Enter message: ")
    for word in joke:
        if word in text:
            print(bot.dadjoke())