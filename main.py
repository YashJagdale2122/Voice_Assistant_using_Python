import speech_recognition as sr
import time
import webbrowser
import playsound
import os
import random
from gtts import gTTS
r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            alexa(ask)

        audio = r.listen(source)
        audio_data = ''
        try:
            audio_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alexa('sorry i didnt understand it')
        except sr.RequestError:
            alexa('sorry currently not available')
        return audio_data


def alexa(audio_string):
    tts = gTTS(text=audio_string,lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-'+str(r)+'.mp4'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(data):
    if 'what is your name' in data:
        alexa('My name is Yash')
    if 'what is the time' in data:
        alexa(time.ctime())
    if 'search' in data:
        search = record_audio('What you want to search?')
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        alexa('here is what i found for '+ search)
    if 'find location' in data:
        location = record_audio('which location you want?')
        url = 'https://www.google.nl/maps/place/'+location+'/&amp;'
        webbrowser.get().open(url)
        alexa('here is the location of '+location)
    if 'exit' in data:
        exit()


time.sleep(1)
alexa('How May I help you?')
while 1:
    data = record_audio()
    respond(data)
