#! /usr/bin/python3

import time
import os
import subprocess

print('Time to unpack all this mess')

answer = None
while answer not in ("Y", "N", "n", "y"):
    answer = input("Dependencies are: \nPandoc and Transcrypt \nAre they installed?\n Y/N: ")
    if answer == "N" or answer == "n":
        installAnswer = None
        while installAnswer not in ("Y", "N", "n", "y"):
            istallAnswer == input("Do you want them to? Y/N: ")
            if installAnswer == "Y" or installAnswer == "y":
                os.system("sudo apt install pandoc")
                os.system("git clone https://github.com/elasticdog/transcrypt.git")           
                os.system("cd transcrypt")           
                os.system("sudo ln -s ${PWD}/transcrypt /usr/local/bin/transcrypt")           
                os.system("cd ..")           
                print("Installed!")
            elif installAnswer == "N" or installAnswer == "n":
                print("Too bad. \nTerminating.")
                time.sleep(2)
                quit()
            else: 
                print("I don't know how to do what you just asked me to...")
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
os.system("cd docs && sh lint.sh")
print("Completed!")
time.sleep(2)
quit()
