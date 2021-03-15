import os
import re
import win32api



def find_file(root_folder, rex):
    found = False
    for root, dirs, files in os.walk(root_folder):
        for f in files:
            result = rex.search(f)
            if not found:
                output = "file not found"
                if result:
                    print(str(os.path.join(root, f)))
                    return os.path.join(root, f)
                    found = True


def find_file_in_all_drives(file_name):
    # create a regular expression for the file
    rex = re.compile(file_name + '.exe')
    print(file_name + '.exe')
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        a = find_file(drive, rex)
    return a


def openApp(app_name):
    try:
        os.startfile(str(find_file_in_all_drives(str(app_name))))
        result = "succesfull"
        print (result)
    except OSError as e:
        result = "failed,cannot find the app on ur device"
        print(e,result)
        return result

if __name__ == "__main__":
    openApp("Spotify") # <- app name goes here, this is an example