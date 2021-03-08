from quoters import Quote


def give_quote(type):
    global quote
    if type == "normal":
        quote = Quote.print()
    if type == "anime":
        quote = Quote.print_anime_quote()

    return quote


if __name__ == '__main__':
    print(give_quote("anime"))
