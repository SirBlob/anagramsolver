from itertools import *  #fast library of tools
import enchant #word spell checker
from termcolor import colored as clrd #color to output

while True:
    letter = input("Enter the words or letters to use.\n")
    if letter.isalpha(): #Checks for valid characters
        length = input("Enter the length of word to stop at.\nFor Example: If length = 3 then words will be created up to 3 length.\n")
        if length.isdigit(): #Checks for valid digits
            if len(letter) >= int(length): #Check if amount of letters is greater then or equal to length
                break
            else:
                print(clrd("The length must be less than the amount of letters.", "red"))
        else:
            print(clrd("Please enter a valid integer.\n", "red"))
    else:
        print(clrd("Please enter valid characters from A-Z.\n", "red"))

#Initialize 
allwords = []
realwords = [] 

#words = list(permutations(letter.lower(), int(length))) #Single Length so if 5 is chosen then only words of 5 length will be created
words = list(chain.from_iterable(permutations(letter.lower(), i) for i in range (1, int(length)))) #Length of words up to input length
spcheck = enchant.Dict("en_US") #Spell Checker using the an english dictionary

for i in range(0, len(words)):
    #(words[i]) #each letter in list example: ('t', 'a', 'p')
    #(''.join(words[i])) #joins each letter to become the word
    allwords.append(''.join(words[i])) #add the words to a list
for w in range(0, len(allwords)):
    if spcheck.check(allwords[w]): #check if the word is an english word if true add to new list
        realwords.append(allwords[w]) #add to list2

realwords = list(set(realwords)) #to remove duplicates and keep type as list

while True:
    fullreal = input("Which list would you like?\nPlease enter 1 for the full list or 2 for the valid words.\n")
    if fullreal.isdigit():
        if fullreal == "1":
            print(allwords)
            break
        elif fullreal == "2":
            print(realwords)
            break
        else:
            print(clrd("Please enter only 1 or 2.\n", "red"))
    else:
        print(clrd("Please enter only 1 or 2.\n", "red"))

    
