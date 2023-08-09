from audioop import add
from platform import uname
import pyttsx3
from pywhatkit import search #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import time
import wikipedia #pip install wikipedia
import webbrowser
import webbrowser as web
from wikipedia.wikipedia import random
import wolframalpha 
import os
import os.path
import sys
from datetime import date
import requests
import pyjokes
from requests import get
import qrcode
from PIL import Image
import pyautogui
import random
from pygame import mixer
import pywhatkit
from pywikihow import WikiHow, search_wikihow
from os import link, replace, startfile
from pyautogui import click 
# from keyboard import press
from keyboard import write
from time import sleep
import flask
import pyaudio


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
# print(voices[0].id)
# print(voices[2].id)
# print(voices[3].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()
    



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!") 

    else:
        speak("Good Evening!")
        
         
    speak("Please tell me how can I help you.") 

def takecommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source,5) #timeout=5,phrase_time_limit=8

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query  

def qr_code():
    speak("say the text:")
    qd=takecommand().lower()
    speak(f"you said {qd}")
    speak("do u want me to change?")
    gg=takecommand().lower()
    if 'no' in gg or 'continue' in gg:
        img=qrcode.make(qd)
        img.save("sample1.jpg")
        im=Image.open(r"C:\\Users\\anant\\Downloads\\FOP\\sample1.jpg")
        speak("Generating QR code.")
        im.show()
    elif 'yes' in gg or 'yeah' in gg:
        qr_code()
        
def gsearch(cm):
    webbrowser.open(f"{cm}")
def utube(search):

    
    link=f"https://www.youtube.com/results?search_query={search}"  
    pywhatkit.playonyt(search)
    web.open(link) 

def wolfram(query):
    api_key="HTVXUL-QEH6X76E4X"
    requester=wolframalpha.Client(api_key)
    requested=requester.query(query)
    speak("one moment please")

    try:
        answer=next(requested.results).text

        return answer

    except:
        speak("try again.")    

def whatsapp(name,message):
    startfile("C:\\Users\\anant\\AppData\\Local\\WhatsApp\\app-2.2134.10\\WhatsApp.exe")
    sleep(7)
    click(x=210,y=167)
    sleep(1)
    write(name)
    sleep(1)
    click(x=239,y=369)
    sleep(0.5)
    click(x=944,y=973)
    write(f"{message}\n",0.1)            

def democlasstst():
    link="https://meet.google.com/ndh-kgkj-spe"
    return link

def DMS():
    link="https://meet.google.com/cvi-fxqc-bwg"  
    return link

def CTPY():
    link="https://meet.google.com/hfm-whfw-tvh"   
    return link

def DS():
    link="https://meet.google.com/qum-khue-ebs"
    return link   

def DBMS():
    link="https://meet.google.com/sdk-duhj-say"    
    return link

def ME():
    link="https://meet.google.com/qth-oeym-gsz" 
    return link   

def DELD():
    link="https://meet.google.com/ufu-ummh-jma"    
    return link

def Agile():
    link="https://meet.google.com/swg-usox-cat" 
    return link   



if __name__ == "__main__":
    # takename()
    os.system('cls')
    speak("Initialising System")
    speak("wait a second.")
    wishMe()
    while True:
    # if 1:
        os.system("cls")
        query = takecommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "").replace("on","").replace("search","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia, ")
            #print(results)
            speak(results)

        elif 'temperature' in query or 'weather' in query:#query = what's the weather in bangalore
            tw=wolfram(query) 
            q01=query.replace("what's the","")
            speak(f'{q01} is {tw}')
        

        elif 'plus' in query or '+' in query:
            s=query.replace("+ ","") #{2+4+6}-->{2 4 6}
            s=s.split() 
            s1 = list(map(int, s))
            sum=0
            for i in range(0,len(s1)):
                sum=sum+s1[i]
        
            print(s)
            print(s1)
            speak(f'sum is {sum}')

        elif 'times' in query or '*' in query or 'x' in query or 'into' in query:
            s=query.replace("*","").replace("times","").replace("x","").replace("into","")
            s=s.split()
            s1 = list(map(int, s))
            multi=1
            for i in range(0,len(s1)):
                multi=multi*s1[i]
        
            print(s)
            print(s1)
            speak(f'answer is {multi}')    

        elif 'hi' in query or 'hello' in query or 'hey' in query or 'hai' in query:
            listsmpl=['hi','hello','hello there','hey',"Hola that's hello in Spanish"]         
            speak(random.choice(listsmpl) +", is there anything that i can do?")

        elif 'who are you' in query:
            speak("i am Tina , your assistant.")    

        elif "what's your name" in query or "what is your name" in query:
            
            speak("My name is Tina ")    
            
        elif 'how are you' in query:
            speak("I am doing Good!, how about you?")
            hu=takecommand().lower()
            speak("nice")

        elif 'increase voulme' in query or 'volume up' in query:
            pyautogui.press('volumeup')    
            pyautogui.press('volumeup')  

        elif 'decrease volume' in query or 'volume down' in query:
            pyautogui.press('volumedown')      
            pyautogui.press('volumedown')      
        
        elif 'mute' in query:
            pyautogui.press('volumemute')
        elif 'open notepad' in query:
            os.system('C:\\Windows\\system32\\notepad')
        elif 'close notepad' in query:
            os.system('taskkill /im notepad.exe')
        elif 'to dms class' in query or 'dms class' in query or 'dms' in query:#query = join DMS class or take me to DMS class
            list2=['Taking you to DMS class','OK ','Sure, Opening DMS class link']
            speak(random.choice(list2))
            # web.open(DMS()) 
            pyautogui.press("winleft")  # press windows left button
            sleep(0.5) 
            pyautogui.typewrite("microsoft edge\n",0.1) # \n is enter button
            sleep(4) 
            pyautogui.typewrite(f"{DMS()}\n")  
            sleep(7)
            click(x=546,y=819)
            sleep(2)
            click(x=664,y=819)
            sleep(1)
            click(x=1414,y=614)
            speak("anything else???")

        elif 'to Ds class' in query or 'ds class' in query or 'ds' in query or 'data structures' in query:
            list3=['Taking you to DS class','OK ','Sure, Opening DS class link']
            speak(random.choice(list3))
            web.open(DS())    
            sleep(3)
            click(x=546,y=819)
            sleep(2)
            click(x=664,y=819)
            sleep(1)
            click(x=1414,y=614)

        elif 'to dbms class' in query or 'dbms class' in query or 'dbms' in query or 'data base management' in query:
            list4=['Taking you to DBMS class','OK ','Sure, Opening DBMS class link']
            speak(random.choice(list4))
            web.open(DBMS())    
            sleep(3)
            click(x=546,y=819)
            sleep(2)
            click(x=664,y=819)
            sleep(1)
            click(x=1414,y=614)

        elif 'to ctpy class' in query or 'python review class' in query or 'ctpy' in query or 'python class' in query:
            list5=['Taking you to python class','OK ','Sure, Opening python class link']
            speak(random.choice(list5))
            # web.open(DMS()) 
            pyautogui.press("winleft")  # press windows left button
            sleep(0.5) 
            pyautogui.typewrite("microsoft edge\n",0.1) # \n is enter button
            sleep(4) 
            pyautogui.typewrite(f"{CTPY()}\n")  
            sleep(7)
            click(x=546,y=819)
            sleep(2)
            click(x=664,y=819)
            sleep(1)
            click(x=1414,y=614)
            speak("anything else???")

        # elif 'to me class' == query or 'me class' == query or 'me' == query:
        #     list6=['Taking you to ME class','OK ','Sure, Opening ME class link']
        #     speak(random.choice(list6))
        #     web.open(ME())    
        #     sleep(3)
        #     click(x=546,y=819)
        #     sleep(2)
        #     click(x=664,y=819)
        #     sleep(1)
        #     click(x=1414,y=614) 

        elif 'to deld class' in query or 'deld class' in query or 'deld' in query or 'digital electronics and logic design' in query:
            list7=['Taking you to DELD class','OK ','Sure, Opening Deld class link']
            speak(random.choice(list7))
            web.open(DELD())    
            sleep(3)
            click(x=546,y=819)
            sleep(2)
            click(x=664,y=819)
            sleep(1)
            click(x=1414,y=614)

        elif 'to agile class' in query or 'agile class' in query or 'agile' in query:
            list8=['Taking you to AGILE class','OK ','Sure, Opening AGILE class link']
            speak(random.choice(list8))
            web.open(Agile())    
            sleep(3)
            click(x=546,y=819)
            sleep(2)
            click(x=664,y=819)
            sleep(1)
            click(x=1414,y=614)

        elif 'open demo link' in query:
            list9=['Taking you to demo link','OK ','Sure, Opening demo link']
            speak(random.choice(list9))
            web.open(democlasstst())    
            sleep(3)
            click(x=546,y=819)
            sleep(2)
            click(x=664,y=819)
            sleep(1)
            click(x=1414,y=614)                        
  

        elif 'classroom' in query:
            speak("Opening Classroom.")
            web.open("https://classroom.google.com/u/0/h")
            # startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
            # sleep(2)
            # pyautogui.typewrite("classroom\n",0.1)
            pyautogui.press("browserrefresh\n")    

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif ' youtube' in query:
            query=query.replace("youtube","")
            if 'search' in query:
                query=query.replace("search","")
            elif 'play' in query:
                query=query.replace("play","")
                     
            query=query.replace("on","")
            speak(f"searching{query} on youtube")           
            utube(query)

        elif 'open google' in query:
            speak("what should i search on google")
            cm=takecommand().lower()
            gsearch(cm)

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
                
        elif 'play music' in query:
             # Starting the mixer
            mixer.init()
              
            # Loading the song
            list10=["C:\\Users\\anant\\Desktop\\songs\\Barso re Megha song.Mp3","C:\\Users\\anant\\Desktop\\songs\\Chikni Chameli Hindi Song Lyrics from Agneepath.mp3","C:\\Users\\anant\\Desktop\\songs\\Counting Stars' - OneRepublic (Alex Goot, Kurt Schneider, and Chrissy Costanza C_256k.Mp3"]
            mixer.music.load(random.choice(list10))
            speak("playing Music")
              
            # Setting the volume
            mixer.music.set_volume(0.9)
              
            # Start playing the song
            mixer.music.play()
              
            # infinite loop
            
                  
            print("say 'p' to pause, 'r' to resume")
            print("say 'e' to exit the program")
            query = takecommand().lower()
                  
        elif 'pause' in query or 'hold up' in query:
        
            # Pausing the music
            speak("OK")
            mixer.music.pause() 
        elif 'increase voulme' in query or 'volume up' in query:
            pyautogui.press('volumeup')    
            pyautogui.press('volumeup')
            speak("OK")

        elif 'resume' in query:
        
            # Resuming the music
            speak("OK")
            mixer.music.unpause()
        elif 'stop music' in query:
        
            # Stop the mixer

            mixer.music.stop()
            speak("music stopped.")
                
            # from pluginfeaturesfrproj import music
            # music()
            # music_dir = 'C:\\Users\\anant\\Desktop\\songs'
            # songs = os.listdir(music_dir)
            # print(songs)    
            # os.startfile(os.path.join(music_dir, songs[0]))
            # os.system("taskkill /im wmplayer.exe")    
            
        elif 'generate qr code' in query:
            qr_code()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"the time is {strTime}")

        elif "ip address" in query:
            ip=get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif 'timer' in query or 'stopwatch' in query:
            speak("For how many minutes?")
            timing = takecommand()
            timing =timing.replace('minutes', '')
            timing = timing.replace('minute', '')
            timing = timing.replace('for', '')
            timing = float(timing)
            timing = timing * 60
            speak(f'I will remind you in {timing} seconds')
            time.sleep(timing)
            speak('Your time has been finished')

        elif 'set alarm for' in query:
            from pluginfeaturesfrproj import alarm
            alarm(query)    


        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
            jk=takecommand()
            if 'nice joke' in jk:
                speak("Glad you like it!!!")

        elif 'the date' in query:
            d2=datetime.datetime.today().strftime("%B %d, %Y")
            speak(f"today is {d2}")   
        elif 'your age' in query:
            speak("I am too young! haha.")
        elif 'will you be my friend' in query:
            speak("I always try to be Friend of you :)")
        elif 'i love you' in query:
            speak("oh! Really?")
            iu=takecommand().lower()
            if 'yes' in iu or 'yeah' in iu:
                speak("Love you too Dear")
            else:
                speak("haha you are joking")

        elif 'thank you' in query:
            speak("I am always at your service")

        elif 'my name' in query:
            speak(F"Your name is")

        elif 'repeat my words' in query:
            speak("What would you like me to Repeat")
            rw=takecommand()
            speak(f"you said, {rw}")

        elif 'who are you' in query:
            speak("I am your Assistant")  

        elif 'what is your name' in query or 'what\'s your name' in query:
            speak("i don't have any name yet.")  
        
        elif 'open whatsapp' in query:
            startfile("C:\\Users\\anant\\AppData\\Local\\WhatsApp\\app-2.2134.10\\WhatsApp.exe")
            speak("opening Whatsapp")

        elif 'whatsapp' in query:
            speak("To whom do you want to send message???")      
            nme=takecommand().lower()
            nme=nme.replace("to","")
            while True:

                speak("What's the message???")
                msg=takecommand().lower()
                speak(f"you said {msg}.\n Shall i send it or change it??")
                yn=takecommand().lower()
                if 'send' in yn or 'send it' in query or 'yash' in query:
                    whatsapp(nme,msg)
                    speak(f"sending message to {nme}")
                    speak("is there anything else?")
                    break
                elif 'change it' in query:
                    speak("Ok")
                    continue
                    

            
        elif 'sleep' in query:
            speak("As you wish, Have a good day!!!!")
            sys.exit()    
