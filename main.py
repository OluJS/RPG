import sys
import time
from titleText import *

text_delay = 0.07


def titleScreenSelect():
    userOption = input("> ")
    if userOption.lower() == ("play"):
        startGame()
    elif userOption.lower() == ("about"):
        about()
    elif userOption.lower() == ("help"):
        helpMenu()
    elif userOption.lower() == ("quit"):
        quitGame()
    while userOption.lower() not in ["play", "about", "help", "quit"]:
        print("Please choose one of the given options")
        userOption = input("> ")
        if userOption.lower() == ("play"):
            startGame()
        elif userOption.lower() == ("about"):
            about()
        elif userOption.lower() == ("help"):
            helpMenu()
        elif userOption.lower() == ("quit"):
            quitGame()


def titleScreen():
    print("================================")
    print("=            Welcome           =")
    print("================================")
    print("=            _Play_            =")
    print("=            _About_           =")
    print("=            _Help_            =")
    print("=            _Quit_            =")
    print("================================")
    titleScreenSelect()


def startGame():
    print("Hello world")


def about():
    print("\n")
    print("=================================================")
    print("=                    About                      =")
    print("=================================================")

    for i in range(0, 1):
        for character in about_text1:
            sys.stdout.write(character)
            time.sleep(text_delay)
        print(sep="")
        for character in about_text2:
            sys.stdout.write(character)
            time.sleep(text_delay)
        print(sep="")
        for character in about_text3:
            sys.stdout.write(character)
            time.sleep(text_delay)
        print(sep="")
        for character in about_text4:
            sys.stdout.write(character)
            time.sleep(text_delay)
    print("\n")
    titleScreen()


def helpMenu():
    print("\n")
    print("=================================================")
    print("=                     Help                      =")
    print("=================================================")
    for i in range(0, 1):
        for character in help_text1:
            sys.stdout.write(character)
            time.sleep(text_delay)
        print(sep="")
        for character in help_text2:
            sys.stdout.write(character)
            time.sleep(text_delay)
        print(sep="")
        for character in help_text3:
            sys.stdout.write(character)
            time.sleep(text_delay)
        print(sep="")
    print("\n")
    titleScreen()


def quitGame():
    reply = str(input("Are you sure you want to quit?" + ' (Y/N): ')).lower().strip()
    if reply == 'y':
        return True
    elif reply == 'n':
        titleScreen()
    else:
        print("Please choose a valid option: ")
        quitGame()


titleScreen()
