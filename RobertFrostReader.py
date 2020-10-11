import pyttsx3
from pyttsx3 import engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
filename = ["Robertfrost.txt"]
b=[]
david = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+-20)
for files in filename:
    f=open(files,'r')
    contents=f.read()
    contents=contents.split('\n')
    b.append(contents[-1])
    f.close()
count1=0
for element in b:
    count1=count1+1
    if b.count(element)>1:
        print(element)
        print(filename[count1-1])
for voice in voices:
    engine.setProperty('voice', david)
    engine.say(contents)
engine.runAndWait()


