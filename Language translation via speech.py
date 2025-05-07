import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound
import os

# Initialize recognizer, translator
recognizer = sr.Recognizer()
translator = Translator()

# Capture audio
with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source)

try:
    # Speech to Text
    text = recognizer.recognize_google(audio)
    print("You said:", text)

    # Translate text
    translated = translator.translate(text, dest='es')  # Change 'es' to any target language code
    print("Translated:", translated.text)

    # Text to Speech
    tts = gTTS(text=translated.text, lang='es')
    filename = "translated.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

except Exception as e:
    print("Error:", e)
