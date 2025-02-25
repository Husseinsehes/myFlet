















import speech_recognition as sr
import sounddevice as sd

rec = sr.Recognizer()
with sr.Microphone() as src:
    print("say something....")
    audio=rec.listen(src)
    text=rec.recognize_google(audio)
print(text)