#! /usr/bin/python3

import time
import os

print('Time to unpack all this mess')

password = input("Enter password: ")
print("Password typed is: " + password)

answer = None
while answer not in ("Y", "N", "n", "y"):
    answer = input("Correct? Y/N: ")
    if answer == "N":
        print("Terminating")
        print("...")
        time.sleep(2)
        quit()
    elif answer == "Y":
        os.system('transcrypt -c aes-256-cbc -p ' + password)
        print("uncrypted")
    else:
        print ("Please input Y or N, I am not smart enough to program these kinds of exceptions.") 

print("Now, for the linting..")
print("UNDER CONSTRUCTION \n ...")
time.sleep(2)
quit()
