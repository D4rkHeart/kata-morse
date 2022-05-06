#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import argparse
morse = {
    "a":".-",
    "b":"-...",
    "c":"-.-.",
    "d":"-..",
    "e":".",
    "é":"..-..",
    "f":"..-.",
    "g":"--.",
    "h":"....",
    "i":"..",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "n":"-.",
    "o":"---",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "s":"...",
    "t":"-",
    "u":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "y":"-.--",
    "z":"--..",
    "0":"-----",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    " ":"  ",
}

def userInput():
  parser = argparse.ArgumentParser()
  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument('-d', '--decode', action="store_true", help='Specify to decode')
  group.add_argument('-e', '--encode', action="store_true", help='Specify to encode')
  args = parser.parse_args()
  return args

#Encypt the ascii entries in morse languages
def encrypt(sentence):
  result = ""
  for char in list(sentence):
    result += morse[char] + " " 
  return result 

def decryptSingleWord(word):
  result = ""
  for char in word.split(" "):
    for keyAscii,valMorse in morse.items():  
      if char == valMorse:
        result += keyAscii 
  return result.rstrip()

def decrypt(sentence):
  result = ""
  words = sentence.split("   ") 
  for word in words:
    result += decryptSingleWord(word) + " "
  return result.rstrip()  

def main():
  result = ""
  argsUsed = userInput() 
  userInputString = input("Enter the text you want to translate: ")
  if argsUsed.encode is True:
    result = encrypt(userInputString)
  else:
    result = decrypt(userInputString)
  print("There is the translation: " + result)

# Executes the main function
if __name__ == '__main__':
  main()