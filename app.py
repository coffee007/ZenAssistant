from features import Assistant
from feature_files.natural_language import talk
import inspect

name = input("Enter bot's name: ")

bot = Assistant(name)

while True:
    text = input("Enter message: ").lower()
    x = talk(text)
    if x[1] == "function":
        a = inspect.getmembers(Assistant)
        y = getattr(bot, x[0])
        result = y()
        if isinstance(result, dict):
            parameter = input(result.get("error"))
            print(y(parameter, False))
        else:
            print(result)
    else:
        print(x[0])
