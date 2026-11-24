# Write a program that generates a random password with a length from 8 to 15 characters.
# Use the RandomLetter() function you have already created.

import random 
import string

characters = random.randint(8, 15)

def RandomLetter():
        return random.choice(string.ascii_letters)

def RandomNumber():
        return str(random.randint(0, 9))

password = ""

for x in range(characters):
    type = random.randint(1,2)
    if type == 1:
        password += RandomLetter()
    elif type == 2:
        password += RandomNumber()

print(password)
