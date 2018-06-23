# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 21:38:43 2018

@author: hp
"""
#chatterbot is a python library used for chatting
from chatterbot import ChatBot
#from chatterbot library import ListTrainer 
#which is used to train chatbot by giving data which contain conversation
from chatterbot.trainers import ListTrainer
#'os' python module used to access operating system contain
import os
#for converting 'text to speech 'only for windows 
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

bot=ChatBot('Bot')
#to set the chatbot for training by listing giving data contain category of different possible conversation
bot.set_trainer(ListTrainer)

#os.listdir: which list the directory contain conversation
for files in os.listdir(r"C:/Users/hp\Downloads\forsk ml project\mAI-real chatbot with api\Data\english/"):
   #to open that folder contain conversation
    data=open(r"C:/Users/hp\Downloads\forsk ml project\mAI-real chatbot with api\Data\english/" + files,'r').readlines()
    #to train the chatbot by giving data contain English folder 
    #which contain different list of possible category of conversation
    #finally train the data
    bot.train(data)
    
print("what can I help you sir!!")
speak.Speak("what can I help you sir")

#for looping infinite until 'Bye'
while True:
    message=input("you :")
    if message.strip() !='Bye':
        reply=bot.get_response(message)
        print("ChatBot :",reply)
        speak.Speak(reply)
    
   
    if message.strip()=='Bye':
        print("ChatBot  : Bye")
        print("Thanks for chatting!! ")
        speak.Speak("Thanks for chatting")
        speak.Speak("Bye")
        
        break