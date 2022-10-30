import pyaudio
#mic at index 1
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    r.adjust_for_ambient_noise(source)
    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("fail")
        print("I heard " + text)