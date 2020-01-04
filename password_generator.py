import string 
from random import *

#add together string characters from string library 
chars = string.ascii_letters + string.punctuation + string.digits

#combine an empty string with a random choice from chars
#the password length can be from 8 to 16 characters 
password = "".join(choice(chars)for x in range(randint(8,16)))


print("Here is your password " + password) 