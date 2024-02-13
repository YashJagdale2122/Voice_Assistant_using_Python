import speech_recognition as sr                                                 # used for recognition of voice
import time                                                                     # to get date and time
import webbrowser                                                               # to access web browser
import playsound                                                                # to play audio file
import os                                                                       # to remove extra files
import random
from gtts import gTTS                                                           # to convert text to audio

r = sr.Recognizer()


def record_audio(ask=False):                                                    # function to recognize audio

    with sr.Microphone() as source:                                             # access microphone for audio
        if ask:
            alexa(ask)

        audio = r.listen(source)                                                # store the audio input
        audio_data = ''
        try:
            audio_data = r.recognize_google(audio)                              # recognize and store the voice data

        except sr.UnknownValueError:
            alexa('Sorry I did not understand it!')

        except sr.RequestError:
            alexa('Sorry currently not available!')

        return audio_data


def alexa(audio_string):                                                        # function to play the audio file

    tts = gTTS(text=audio_string, lang='en')                                    # convert text into audio
    name = random.randint(1, 1000000)
    audio_file = 'audio-' + str(name) + '.mp4'                                         # name the audio file
    tts.save(audio_file)                                                        # save the file
    playsound.playsound(audio_file)                                             # play the file
    print(audio_string)
    os.remove(audio_file)                                                       # remove the file


def respond(audio_data):                                                              # function to answer the questions

    if 'what is your name' in audio_data:
        alexa('My name is Assistant')

    if 'what is the time' in audio_data:
        alexa(time.ctime())

    if 'search' in audio_data:
        search = record_audio('What you want to search?')
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)                                              # access the browser
        alexa('Here is what i found for '+search)

    if 'find location' in audio_data:
        location = record_audio('which location you want?')
        url = 'https://www.google.nl/maps/place/'+location+'/&amp;'             # access map using browser
        webbrowser.get().open(url)
        alexa('Here is the location of '+location)

    if 'exit' in audio_data:
        exit()                                                                  # exit from the loop


time.sleep(1)                                                                   # the continuous running the code
alexa('How May I help you?')

while 1:                                                                        # loop for repeatedly functions
    data = record_audio()
    respond(data)
