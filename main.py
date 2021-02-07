#Note: Please install all the modules given below due to run this programme. You can run this Programme without 'pyttsx3' module installed but in that case you will be unable enjoy the audio feature. 

import json
import difflib
from difflib import get_close_matches
from difflib import SequenceMatcher
import pyttsx3
data = json.load(open("data.json"))



try:
  engine = pyttsx3.init('sapi5')
  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[1].id)


  def speak(audio):
    engine.say(audio)
    engine.runAndWait()


  def query_func(word):
    word = word.lower()

    if word in data:
        output = data[word]
        if type(output) == list:
            for items in output:
                speak(items)
                return (items)
        else:
            speak(output)
            return (output)

    elif word.upper() in data:  # In case of UPPERCASE words like USA,UK
        output = data[word.upper()]
        if type(output) == list:
            for items in output:
                speak(items)
                return (items)
        else:
            speak(output)
            return (output)

    elif word.title() in data:  # In case of words like London, Delhi, Dhaka etc
        output = data[word.title()]
        if type(output) == list:
            for items in output:
                speak(items)
                return (items)
        else:
            speak(output)
            return (output)

    elif len(get_close_matches(word, data.keys())) > 0:
        speak(f"'{word}' is dosen't exists. Do you mean '%s'. Type y if it yes , type n if it no" %
              get_close_matches(word, data.keys())[0])
        yn = input(f"'{word}' is dosen't exists. Do you mean '%s'. y/n?: " %
                   get_close_matches(word, data.keys())[0])

        if yn == 'y':
            output = data[get_close_matches(word, data.keys())[0]]
            if type(output) == list:
                for item in output:
                    speak(item)
                    print(item)
            else:
                speak(output)
                print(output)

        elif yn == 'n':
            speak("the word doesn't exists")
            return "The word doesn't exists."

        else:
            speak("Sorry, we didn't understand your entry")
            return "Sorry, we didn't understand your entry."

    elif word == "0000":
        speak("You are now quiting..THANKS FOR USING MY APPLICATION")
        print("You are now quiting.. \n ***THANKS FOR USING MY APPLICATION***")
        quit()

    else:
        speak("The word doesn't exists. Please Please double check it.")
        return "The word doesn't exists. Please Please double check it."


  i = 0
  while True:
    if i == 0:
        speak("This is a word queris application. By typing a word you will able to know something about the word")
        print("***/This is a word queris application. By typing a word you will able to know something about the word/***\n -----THIS APPLICATION PROGRAMMED BY RAYHAN MAHMUD-----\n #####To exit type '0000'")
        speak("THIS APPLICATION PROGRAMMED BY RAYHAN MAHMUD")
        speak("To exit type 0000")

        i = i + 1
    speak("Enter the word")
    word = input("Enter The Word: ")
    names = ["mahmud", "rezwan", "rayhan"]
    if word != "0000" and word != "rezwan" and word != "rayhan" and word != "mahmud":
        speak("The meanings of the word")
        speak(word)
    print(query_func(word))


# without_audio
# please install "pyttsx3" module for audio

except Exception as e:


  def query_func(word):
    word = word.lower()

    if word in data:
        output = data[word]
        if type(output) == list:
            for items in output:
                return (items)
        else:
            return (output)

    elif word.upper() in data:  # In case of UPPERCASE words like USA,UK
        output = data[word.upper()]
        if type(output) == list:
            for items in output:
                return (items)
        else:
            return (output)

    elif word.title() in data:  # In case of words like London, Delhi, Dhaka etc
        output = data[word.title()]
        if type(output) == list:
            for items in output:
                return (items)
        else:
            return (output)

    elif len(get_close_matches(word, data.keys())) > 0:

        yn = input(f"'{word}' is dosen't exists. Do you mean '%s'. y/n?: " %
                   get_close_matches(word, data.keys())[0])

        if yn == 'y':
            output = data[get_close_matches(word, data.keys())[0]]
            if type(output) == list:
                for item in output:
                    print(item)
            else:
                print(output)

        elif yn == 'n':
            return "The word doesn't exists."

        else:
            return "Sorry, we didn't understand your entry."

    elif word == "0000":
        print("You are now quiting.. \n ***THANKS FOR USING MY APPLICATION***")
        quit()

    else:
        return "The word doesn't exists. Please Please double check it."


  i = 0
  while True:
    if i == 0:
        print("***/This is a word queris application. By typing a word you will able to know something about the word/***\n -----THIS APPLICATION PROGRAMMED BY RAYHAN MAHMUD-----\n #####To exit type '0000'")

        i = i + 1
    word = input("Enter The Word: ")
    names = ["mahmud", "rezwan", "rayhan"]
    if word != "0000" and word != "rezwan" and word != "rayhan" and word != "mahmud":
        print(f"The meanings of the word '{word}'...")
    print(query_func(word))

