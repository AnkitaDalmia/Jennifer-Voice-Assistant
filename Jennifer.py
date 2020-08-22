import pyttsx3  # text to speech library
import datetime
import speech_recognition as sr
import wikipedia
import getpass
import random
import os
import webbrowser
import smtplib

webbrowser.register('chrome',
                    None,
                    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')  # getting details of current voice

engine.setProperty('voice', voices[1].id)

'''speaks whatever text given to the speak function in string converts it into voice '''


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def sendEmail(to, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    email = ''  # give your own email
    password = ''  # give your own email app password
    server.login(email, password)  # login will be done
    msg = "Subject: "+subject+'\n'+content  # adding subject and content
    from_address = 'ankitadalmia2010@gmail.com'  # filling the from with the email
    # sending email to the mail passed as argument
    server.sendmail(from_address, to, msg)
    server.close()  # closing the server


''' wishes morning,afternoon,evening,night based on the time'''


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon!")
    elif hour >= 16 and hour < 19:
        speak("Good Evening!")
    else:
        speak("Good Night!")

    speak("I am Jennifer Sir. What can I help you with?")


'''It takes microphone i/p from the user and return string o/p'''


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Go ahead Listening....")
        # so that if user takes pause of 1 sec while speaking it doesnot complete its listening it will wait for a sec
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing query told by user
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia ")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get('chrome').open("youtube.com")

        elif 'open google' in query:
            webbrowser.get('chrome').open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open("stackoverflow.com")

        elif 'open 2 7' in query:
            webbrowser.get('chrome').open("twoseven.xyz")

        elif 'open amazonprime' in query:
            webbrowser.get('chrome').open("primevideo.com")

        elif 'open netflix' in query:
            webbrowser.get('chrome').open("netflix.com")

        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            n = random.randint(0, len(songs))
            os.startfile(os.path.join(music_dir, songs[n]))

        elif 'play songs' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            n = random.randint(0, 10)
            os.startfile(os.path.join(music_dir, songs[n]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")

        elif 'open vscode' in query:
            codePath = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("What should I keep the subject?")
                subject = takeCommand()
                speak("What should I say?")
                content = takeCommand()
                #speak("Tell me the email id sir")
                # to=takeCommand().lower()
                to = '1705928@kiit.ac.in'
                sendEmail(to, subject, content)
                speak("Email has been sent!")

            except Exception as e:
                # print(e)
                speak("Sorry I am not able to send the email ")

        elif 'quit' in query:
            speak("Okay bye-bye sir have a good day")
            exit(0)
