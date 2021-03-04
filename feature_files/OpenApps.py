import os


# find the file that needs to be opened
def find(name):
    # searches the folders
    for root, dirs, files in os.walk("C:\\Users\\raju srinivasan\\Desktop"):
        # if it finds it, it prints the path and returns it
        if str(name + ".lnk") in files:
            path = str((root + "\\" + name + ".lnk"))
            print(path)
        # else it does this
        else:
            error = "File not found , make sure the shortcut is in ur desktop"
            print(error)
            path = None

        return path


def OpenAPP(name):
    O = find(str(name))
    os.startfile(str(O))

OpenAPP("Spotify")