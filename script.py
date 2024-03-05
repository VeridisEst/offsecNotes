#! /usr/bin/python3

import time
import os

print('Time to unpack all this mess')

answer = None
while answer not in ("Y", "N", "n", "y"):
    answer = input("Dependencies are: \nPandoc and Transcrypt \nAre they installed?\n Y/N: ")
    if answer == "N" or answer == "n":
        print("Terminating\n...")
        time.sleep(2)
        quit()
    elif answer == "Y" or answer == "y":
        print("Cool. Proceeding.")
    else:
        print ("Please input Y or N, I am not smart enough to program these kinds of exceptions.") 


password = input("Enter password: ")
print("Password typed is: " + password)
answer = None
while answer not in ("Y", "N", "n", "y"):
    answer = input("Correct? Y/N: ")
    if answer == "N" or answer == "n":
        print("Terminating")
        print("...")
        time.sleep(2)
        quit()
    elif answer == "Y" or answer == "y":
        os.system('transcrypt -c aes-256-cbc -p ' + password)
        print("uncrypted")
    else:
        print ("Please input Y or N, I am not smart enough to program these kinds of exceptions.") 

print("Now, for the linting..")
print("UNDER CONSTRUCTION \n ...")
time.sleep(2)
quit()
