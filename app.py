from features import Assistant
from feature_files.natural_language import talk
import json
import inspect


try:
    with open("feature_files/data/userdata.json", "r+") as d:
        data = dict(json.load(d))
        d.close()
    write = open("feature_files/data/userdata.json", "w")


    if data.get("signedin") == 0:
        username = input("Enter your name: ")
        data["signedin"] = 1

    if data.get("botname") == "":
        name = input("Enter bot's name: ")
        data['botname'] = name
    else:
        name = data.get("botname")

    json.dump(data, write)

    write.close()

    print("The data you enter here is stored on your device and not sent anywhere else.")
    print()

    bot = Assistant(name)
except:
    bot = Assistant("Zen")

while True:
    text = input("Enter message: ").lower()
    x = talk(text)
    if x[1] == "function":
        a = inspect.getmembers(Assistant)
        y = getattr(bot, x[0])
        result = y()
        if isinstance(result, dict):
            parameter = input(result.get("error"))
            print(y(parameter, reqs_confirm=False))
        else:
            print(result)
    else:
        print(x[0])
