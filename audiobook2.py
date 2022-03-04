'''
gTTS - Google Text-To-Speech, is a python library 
that coverts text to speech, 
interacting with Google Translate text-to-speech API

'''
#importing gTTS
#importing os that it will open automatically on running
from gtts import gTTS
import os

#the text written in the file named audiobooktext.txt is opened
audio_text = open('audiobooktext.txt')

#read the file
text = audio_text.read()

language = 'en'

#gTTS converting the text to audio
audiobook = gTTS(text = text,lang = language,slow = False)
audiobook.save("comfortaudio.mp3")


os.system("comfortaudio.mp3")
