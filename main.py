import win32com.client as wincom


if __name__ == '__main__':
    speak = wincom.Dispatch("SAPI.SpVoice")
    speak.Speak("Welcome To RoboSpeaker 1.1. Created by Aryan")
    print("Welcome To RoboSpeaker 1.1. Created by Aryan")
    while True:
        text = input("Enter What You Want Me To Speak: ")
        if text == "q":
            speak.Speak('bye bye ')
            break
        speak.Speak(text)