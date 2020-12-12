
from gtts import gTTS
import os 
mytext = input('Write what u have to listern = ')

language = 'en'

myobj = gTTS(text= mytext, lang = language)

myobj.save('welcome.mp3')
os.system('welcome.mp3')
