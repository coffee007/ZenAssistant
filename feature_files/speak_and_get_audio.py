import pyttsx3
import speech_recognition


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.setProperty("rate", 150)
    try:
        engine.runAndWait()
    except RuntimeError:
        return


def get_audio():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source, duration=5)
        said = ""
        try:
            said = r.recognize_google(audio)
        except Exception as e:
            said = "lol"
    return said