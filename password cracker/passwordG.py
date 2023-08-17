# importing modules.
import string, random

# taking input.
password = input("\nEnter your password : ")

# all characters.
chracter = string.printable

# generating random passwords until the random password match with the input password. 
while True:
    pGuess = random.choices(chracter, k=len(password))
    pGuess = ''.join(pGuess)
    print(pGuess)
    if password == pGuess:
        print(f"\nMatched password is : {pGuess}")
    break