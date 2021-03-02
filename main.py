import pyttsx3
import speech_recognition


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.setProperty("rate", 150)
    engine.runAndWait()



def get_audio():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=3)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("end")
    return said

text = get_audio()

if "hello " in text:
    print("sfsdfg")


