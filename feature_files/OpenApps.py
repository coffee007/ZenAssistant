import os

file_added = False
try:
    if not file_added:
        directory = os.path.join("userapps")
        os.mkdir(directory)
        print("File added")
        file_added = True
    else:
        print("File added already")
except OSError as e:
    print(e)


# find the file that needs to be opened
def find(name):
    # searches the folders
    for root, dirs, files in os.walk("C://ZEN"):
        # if it finds it, it prints the path and returns it
        if str(name.lower() + ".lnk") in str(files).lower():
            path = str((root + "\\" + name + ".lnk"))
            print(path)
            # else it does this
        else:
            error = ("File not found , make sure the shortcut is added to " + directory)
            print(error)
            path = None

        return path


def OpenAPP(name):
    app_to_be_opened = find(str(name))
    try:
        os.startfile(str(app_to_be_opened))
    except Exception as e:
        print("")



