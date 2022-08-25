from pynput.keyboard import Key, Listener
from mss import mss
import time
import random
import csv


keys = []
header = ["BAD WORDS"]

#this loop is very slow and freezes the PC, hopefully faster when the program is executable
def check_csv(final_word):
    with open("trap_words.csv", "r") as f:
        reader = csv.reader(f)
        for i in reader:
            if final_word.lower() in i:
                return True




#this will read all keyboard input
def on_press(key):
    global keys
    if len((str(key))) == 3: # this will only add letters to the variable we will use to save words, might behave unexpectedly in languages like russian

        keys.append(str(key).strip("'"))
    #this checks if a symbol has been pressed, will react everytime space, enter, backspace is pressed
    elif len((str(key))) == 9:

        final_word = ''.join(keys) #this will create a word from all the characters we have collected
        if final_word == "": #this will make it so we dont check empty space which would always result in a screenshot
            pass
        else:
            if check_csv(final_word):   #this will check if the word is in the csv and screenshot
                with mss() as sct:
                    num1 = random.randint(0, 100000)
                    filename = sct.shot(mon=-1, output=f'fullscreen{num1}.png')

                    time.sleep(20)
                    filename = sct.shot(mon=-1, output=f'fullscreen{num1}.png')

            keys = [] #this resets the list after screenshotting

#this will stop the word checking after the insert button is pressed
def on_release(key):
    if key == Key.insert:
        print("owari da")
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
