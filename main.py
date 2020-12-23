import json
import difflib
from difflib import get_close_matches 
from difflib import SequenceMatcher
data = json.load(open("data.json"))


def query_func(word):
  if word in data:
    return data[word]
  
  elif len(get_close_matches(word, data.keys())) > 0 :
    yn = input(f"'{word}' is dosen't exits. Do you mean '%s'. y/n?: "% get_close_matches(word, data.keys())[0])

    if yn == 'y':
      return data[get_close_matches(word, data.keys())[0]]
    
    elif yn == 'n':
      return "The word doesn't exists."
    else:
      return "Sorry, we didn't understand your entry."


  elif word == "0000":
    print("You are now quiting.. \n ***THANKS FOR USING MY APPLICATION***")
    quit()
    
  else:
    return "The word doesn't exists. Please try again!"



    
i = 0
while True:
  if i == 0:
    print("***/This is a word queris application. By typing a word you will able to know something about the word/***\n -----THIS APPLICATION PROGRAMMED BY RAYHAN MAHMUD-----\n #####To exit type '0000'")
    i = i + 1
  word = input("Enter The Word: ")
  word_capitaliza = word.lower()
  print(query_func(word_capitaliza))
 












  # # elif word in data:
  # #   return data[word]
  
  # elif len(get_close_matches(word, data.keys())) > 0 :
  #   print(f"{word} is dosen't exits. Do you mean %s "  % get_close_matches(word, data.keys())[0])
  # elif word == "0000":
  #   print("You are now quiting.. \n ***THANKS FOR USING MY APPLICATION***")
  #   quit()
    
  # else:
  #   print("The word doesn't exists. Please try again!")

 
 