#This python library converts text to speech
import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker!")
    print("Developed by Vipashana :)")

    while(True):
        x = input("Enter whatever you want the Robo to speak & type stop to end: ")
        if x=='stop':
            break
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        #Controld the speed of speaking
        engine.setProperty('rate', rate + 10)
        #Allows talking given texts
        engine.say(x)
        #keeps further execution on hold until the loop ends
        engine.runAndWait()