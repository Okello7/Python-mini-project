import json

#opening the dictionary data.json file in read mode
fin = open("data.json", "r")
#reading the content of the json file to the cont  object
cont = json.load(fin)

#function 1 Display the word that begin with a specific letter
def dispwords():
    letter = input("Enter the letter to display the words with which it  begins with: ").lower()
    for i in cont:
        if i.startswith(letter):
            print(i)

#function 2 to find a word and display if it is in the dictionary or not
def findword():
    word = input("Enter the word to check in the Dictionary: ").lower()
    found = False
    for i in cont:
        if i == word:
            found = True
    if found == False:
        print("No such word in the dictionary!")
    else:
        print("It is there in the dictionary!")

#function 3 to display the meaning of the specific word.
def dispm():
    word = input("Enter word to check the meaning of: ").lower()
    found = False
    for key, value in cont.items():
        if key == word:
            found = True
            print("{} word has meaning {}".format(key, value))
    if found == False:
        print("No such  word exists.")
    else:
        print("Word has meaning.")

#function 4 to Display the word-meanings for the specific word that is there in the meaning
def dispsm():
    word = input("Enter word to check word-meaning: ").lower()
    found = False
    for key, value in cont.items():
        if key == word or word in value:
            found = True
            print("{} - meaning - {}".format(key, value))
    if found == False:
        print("No such word exists.")

#function 5 to search words by number of letters
def lettersearch():
    num = int(input("Enter number of letters or length of the word: "))
    found = False
    for key  in cont:
        if len(key) == num:
            print(key)
            found = True
    if found == False:
        print("No word with the specific length.")
    

#menu for the interactive dictionary

while True:
    try:
        print("""
        I N T E R A C T I V E  D I C T I O N A R Y
        ==========================================
        1.Display the word that begin with a specific letter.
        2.Find a specific word.
        3.Display the meaning of the specific word.
        4.Display the word-meanings for the specific word that is there in the meaning
        5.Search and display words by number of letters
        6.Exit program


        """)
        choice = int(input("Enter your choice of operation(1-6): "))
        if choice == 1:
            dispwords()
        elif choice == 2:
            findword()
        elif choice == 3:
            dispm()
        elif choice == 4:
            dispsm()
        elif choice == 5:
            lettersearch()
        elif choice == 6:
            break
        else:
            print("Invalid number!. Enter a number between 1 to 6.")

    except:
        print("Invalid input!")    
