import pyttsx3
import pyttsx3
engine = pyttsx3.init()
def voice_mode(md):
    if "male" in md:
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[0].id)

    elif "female" in md:
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[1].id)

    else:
        print("Invalid mode")

def speak(text):
    engine.say(text)
    engine.runAndWait()