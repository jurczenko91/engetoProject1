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

registeredUsers = {
    'bob': '123', 
    'ann': 'pass123', 
    'mike': 'password123', 
    'liz': 'pass123',
    #'1': '1' #delete it
}

n = 40 #separator line --- length
import time

#checking if user is registered
userName = input('Username: ')
userPass = input('Password: ')
for (userCheck, passCheck) in (registeredUsers.items()):
    if userName == userCheck and userPass == passCheck:
        break
else:
    while True:
        print('Unregistered user, terminating the program...')
        time.sleep(3) #delay before terminating in sec
        quit()

print('-' * n)
print('Welcome to the app,', userName)
print('We have', len(TEXTS), 'texts to be analyzed.')
print('-' * n)

#texts chosing 
print('Enter a number btw. 1 and', len(TEXTS), end=' ')
textNumber = int(input('to select: '))
print('-' * n)
if 1 <= textNumber <= len(TEXTS):
    pass
else:
    print('Invalid value. Terminating the program...')
    time.sleep(3) #delay before terminating in sec
    quit()

#creating list from selected text
selText = TEXTS[textNumber - 1] #because we count from 0
formatText = [] #selText is just letters, we create an empty list for filling with words
slovo = ''
for el in selText:
    if el.isalnum():
        slovo = slovo + el
    else:
        formatText.append(slovo)
        slovo = str()        

#tasks to analyse
#1: amount of words
allWordsAmount = 0
for el1 in formatText:
    if el1.isalpha() or el1.isdigit():  #delete el1.isdigit() for counting only words
        allWordsAmount = allWordsAmount + 1

#2: words starting with capital letter
capWords = 0
for el2 in formatText:
    if el2.istitle():
        capWords = capWords + 1

#3: capsed words
wholeCapWords = 0
for el3 in formatText:
    if el3.isupper():
        wholeCapWords = wholeCapWords + 1

#4: amount of lowercase words
lowerWords = 0
for el4 in formatText:
    if el4.islower():
        lowerWords = lowerWords + 1

#5 and 6: amount of numeric strings and their sum
numStr = 0  #amount of numeric strings
sumStr = 0  #sum of numbers
for el5 in formatText:
    if el5.isdigit():
        numStr = numStr + 1
        sumStr = sumStr + int(el5)

#displaying summarise info
print('There are', allWordsAmount, 'words in the selected text.')
print('There are', capWords, 'titlecase words.')
print('There are', wholeCapWords, 'uppercase words.')
print('There are', lowerWords, 'lowercase words.')
print('There are', numStr, 'numeric strings.')
print('The sum of all the numbers', sumStr, end='.\n')

#separator
print('-' * n)
print('LEN|', '     OCCURENCES    ', '|NR.')
print('-' * n)

#words length statistics
lenStat = dict()
lenValue = 0
for el6 in formatText:
    if el6.isalpha() or el6.isdigit():  #check that the word is not a spacebar. Delete el6.isdigit() condition for counting only words without numbers
        lenKey = str(len(el6))      #add to variable stringified length of word in el6
        for el7 in lenStat.keys(): 
            if el7 == lenKey:       #if the key is already in dict lenStat
                break               #exit the cycle    
        else:
            lenStat[lenKey] = 0     #if the key is not in the dict, write that key length as key with value 0
        lenValue = lenStat[lenKey] + 1
        lenStat[lenKey] = lenValue  

#sorting dictionary so that keys (numbers of letters) are in ascending order
sortedDict = dict(sorted(lenStat.items()))  #first sorting, but it returns 1, 10, 11, 2, 20 etc
sortedStat = dict()     #for 1 to 9
sortedStat2 = dict()    #for >10
for j in sortedDict:
    if int(j) <= 9:
        sortedStat[j] = sortedDict.get(j)
    else:
        sortedStat2[j] = sortedDict.get(j)
sortedStat.update(sortedStat2)

#showing the stats and grafs
for i in sortedStat:
    print(i.rjust(3) + '|', '*' * sortedStat.get(i), ' ' * (20 - sortedStat.get(i)), sortedStat.get(i))
print('-' * n)
while True:
    input('Press Enter to exit')
    break