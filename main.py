"""
main.py: první projekt do Engeto Online Python Akademie

The algorythm counts numbers as words, too. 
author: Anton Yurchenko
email: jurczenko91@gmail.com
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

registeredUsers = { #list (dict) of users, who are currently registered, 'user name': 'password'
    'bob': '123', 
    'ann': 'pass123', 
    'mike': 'password123', 
    'liz': 'pass123',
    #'1': '1' #delete it
}

n = 40 #separator line --- length
import time #importing library for implementing the delay before terminating the program

#checking if user is registered
userName = input('Username: ') #getting user name from user
userPass = input('Password: ') #getting password from user
for (userCheck, passCheck) in (registeredUsers.items()): #userCheck and passCheck are user name and corresponding password taken from registeredUsers dict
    if userName.lower() == userCheck.lower() and userPass == passCheck:  #we compare user name and password we've got from user with ones we have (user name isn't case sensitive)
        break
else:
    while True:
        print('Unregistered user, terminating the program...')
        time.sleep(3) #delay before terminating in sec
        quit()

print('-' * n)
print('Welcome to the app,', userName.lower())
print('We have', len(TEXTS), 'texts to be analyzed.')
print('-' * n)

#texts chosing 
print('Enter a number btw. 1 and', len(TEXTS), end=' ')
textNumber = input('to select: ') #getting text number from user
print('-' * n)
if textNumber.isdigit() and 1 <= int(textNumber) <= len(TEXTS): #check if data from user is digit and in existing texts range
    pass
else:
    print('Invalid value. Terminating the program...')
    time.sleep(3) #delay before terminating in sec
    quit()

#preparing selected text for analyse
#as now the selected text is just one big string, let's divide it by words, then word by word add it to the list
formatText = [] #creating an empty list to fill, formatted text
slovo = '' #creating something like a box, to fill it with letters or numbers, when the word is ready, we transfer it to the formatText list as new element
for el in TEXTS[int(textNumber) - 1]: #starting to grab every el - element of the string in the selected text
    if el.isalnum():                  #if the element is digit or letter
        slovo = slovo + el            #add it to the 'box' slovo 
    else:
        formatText.append(slovo)      #if the next element is something else, then it was the end of the word, so we transfer it from the box to the list formatText
        slovo = str()                 #and clear the box

#tasks to analyse
allWordsAmount = 0 #1: amount of words in text
capWords = 0       #2: words starting with the capital letter
upperCaseWords = 0 #3: amount of uppercase words
lowerCaseWords = 0 #4: amount of lowercase words
numStr = 0         #5: amount of numeric strings
sumStr = 0         #6: sum of numbers

for word in formatText: #associating variable word with element from formatText and analysing it
    if word.isalpha() or word.isdigit():  #if it's a word or number
        allWordsAmount = allWordsAmount + 1 #increase the counter by 1 and
        if word.istitle():                   #in case it's in titlecase
            capWords = capWords + 1          #insrease the titlecase counter by 1
        elif word.isupper():                 
            upperCaseWords = upperCaseWords + 1
        elif word.islower():
            lowerCaseWords = lowerCaseWords + 1
        elif word.isdigit():                 #in case it's a number
            numStr = numStr + 1              #increase numbers counter by 1
            sumStr = sumStr + int(word)      #add the number to the previous found number value to get the sum

#displaying summarise info
print('There are', allWordsAmount, 'words in the selected text.')
print('There are', capWords, 'titlecase words.')
print('There are', upperCaseWords, 'uppercase words.')
print('There are', lowerCaseWords, 'lowercase words.')
print('There are', numStr, 'numeric strings.')
print('The sum of all the numbers', sumStr, end='.\n')

#words length statistics
print('-' * n)
print('LEN|', '     OCCURENCES    ', '|NR.')
print('-' * n)

#we need to find out the lengths of the words in text, how many kinds of them exist and how many words of each kind are present in the selected text.
#we'll use the previous generated list formatText as it contains all the data we need
#the idea is to create the dict, where the keys would be the lengths presented in the text, and corresponded values would be amounts of words of that length
lenStat = dict() #create empty dict we later fill with lengths and amounts
lenValue = 0     #this variable is amount of corresponding word length, later to be written as dict value, set as 0 for now
for word in formatText:                   #associate the element from formatText list (word in this case) to variable word and check it
    if word.isalpha() or word.isdigit():   #if it is word or number
        lenKey = int(len(word))             #count the number of characters in the word and associate to the variable. This is a key name we work with.
        for key in lenStat.keys():          #then we need to check, if the key name we've just got is already exists in lenStat
            if key == lenKey:                #if the key is already in the dict
                break                          #exit the cycle (without adding a key)   
        else:                               #if the key is not present in the dict
            lenStat[lenKey] = 0              #write that key with value 0 to the dict lenStat
        lenValue = lenStat[lenKey] + 1      #increase the value corresponded to lenKey (the key we currently work with) by 1
        lenStat[lenKey] = lenValue          #add the value we've got to the key we currently work with to the lenStat

#so that we have a dict with presented lengths and corresponded amounts, we need to sort the data by keys
sortedStat = dict(sorted(lenStat.items())) #create a new dict with data sorted by keys in ascending order using function sorted()

#showing the stats and grafs
for i in sortedStat:
    print(str(i).rjust(3) + '|', '*' * sortedStat.get(i), ' ' * (20 - sortedStat.get(i)), sortedStat.get(i))
print('-' * n)
while True:
    input('Press Enter to exit')
    break 