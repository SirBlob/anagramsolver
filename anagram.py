import itertools #fast library of tools
import enchant #word spell checker

letter = input("Enter the letters to use\n")
length = input("Enter the length of each word\n")

words = list(itertools.permutations(letter.lower(), int(length)))
spcheck = enchant.Dict("en_US") #Spell Checker using the an english dictionary

#Initialize 
allwords = []
realwords = [] 

for i in range(0, len(words)):
    #(words[i]) #each letter in list example: ('t', 'a', 'p')
    #(''.join(words[i])) #joins each letter to become the word
    allwords.append(''.join(words[i])) #add the words to a list
for w in range(0, len(allwords)):
    if spcheck.check(allwords[w]): #check if the word is an english word if true add to new list
        realwords.append(allwords[w]) #add to list2

if len(letter) >= int(length): #Check if amount of letters is greater then or equal to length
    realwords = list(set(realwords)) #to remove duplicates and keep type as list
    print(realwords) 
else:
    print("The length must be less than the amount of letters.")
