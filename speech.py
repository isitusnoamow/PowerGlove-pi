import pyaudio
#mic at index 1
import speech_recognition as sr

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

r = sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    r.adjust_for_ambient_noise(source)
    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("fail")
        print(text)
        if "start" in text or "test" in text:
            write_report(NULL_CHAR*2+chr(6)+NULL_CHAR*5)