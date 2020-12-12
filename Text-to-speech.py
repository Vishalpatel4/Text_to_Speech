# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 19:05:32 2020

@author: Lenovo
"""

from gtts import gTTS
import os 
mytext = input('Write what u have to listern = ')

language = "hi"

myobj = gTTS(text= mytext, lang = language)

myobj.save('welcome.mp3')
os.system('welcome.mp3')
