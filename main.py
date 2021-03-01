import pyttsx3
import speech_recognition


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.setProperty("rate", 150)
    engine.runAndWait()

for index, name in enumerate(speech_recognition.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

def get_audio():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        audio = r.listen(source)
        said = ""
        said = r.recognize_google(audio)
        print(said)
    return said

text = get_audio()

if "hello " in text:
    print("sfsdfg")


