# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 06:47:16 2018

@author: hp
"""

import os,time
import random
import sys
#for conversion of text to speech in windows
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")


#now lets craete this words for listening
nameIn=['what is your name','whats your name','what is your name?','whats your name?']
greetIn=['hello','hi','hi there','hello there']
birth=['what is your date of birth','what is your date of birt?','what is your DOB','what is your DOB?']
botmaster=['who is your botmaster','who is your botmaster?','who is your father','who is your father?']
abouti=['how are you','how are you?','whats up','whats up?']



#will also need to outgoing
greetOut=['hi there','hello','hi my name is ultron','hello there']
nameOut=['I am called ultron','my name is ultron','im called ultron']
aboutO=['I am fine','Im fine']


print("Hello there!!")
print(speak.Speak("What can i help you sir"))

while True:
    H=input(('You :').strip())
    Hlower=H.lower()
    
    if H == 'Bye':
        print('Bot : Thanks meeting you')
        #speak.Speak("thanks meeting you")

        break
    elif Hlower in nameIn:
        print('Bot :' + (random.choice(nameOut)))
        #speak.Speak(random.choice(nameOut))
    elif Hlower in greetIn:
        print('Bot :' + (random.choice(greetOut)))
        #speak.Speak(random.choice(greetOut))
    elif Hlower in botmaster:
        print('Bot : my botmaster is Manish')
        #speak.Speak("my creator is manish")
    elif Hlower in birth:
        print('Bot : I was activated in the 3rd june 2018')
        #speak.Speak("I was activated in the 3rd june 2018")
    elif Hlower in nameIn:
        print('Bot :' + (random.choice(aboutO)))