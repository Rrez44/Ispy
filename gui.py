import threading
from tkinter import *
import csv
import customtkinter
import os


# this imports the entire main function and runs it when called
def run_program():
    os.system('python main.py')


# main window properties
window = Tk()
window.title("iSpy")
window.configure(bg="#36393f", border=True, borderwidth=2, takefocus=True)
window.resizable(False, False)
w = 280 # width for the Tk root
h = 350 # height for the Tk root
#getting screen info and dividing it by two so it appears in the middle of the screen
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/3) - (h/3)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))

#the icon that will appear when u open the window
photo = PhotoImage(file="icon.png")
window.iconphoto(False, photo)


# this will be used when a user add words, appending it to the csv
def add_word(inputi):
    with open("trap_words.csv", "a") as f:
        writer = csv.writer(f)
        new_word = (str(inputi))
        writer.writerow([new_word])

#this deletes all words in the trap word csv besides the header
def delete_words():
    with open("trap_words.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["TRAP WORDS"])

#this bit of code is used to get the length of the csv list
all_words = []
with open("trap_words.csv", "r") as f:
    reader = csv.reader(f)
    for i in reader:
        all_words.append(i)
#these functions will be used to cycle the index of the list so you can show different words, we need the length so the index does not go out of range
global index
index = 0
global index_range
index_range = len(all_words)

def add_2():
    global index, index_range
    index += 2 #we add two because theres a blank space between words
    if index == index_range:
        index = 0 #this will reset the index if it goes out of range
    else:
        return index

def remove_2(): #same function except used for going back one words
    global index
    index -= 2
    if index == -index_range:
        index = 0
    else:
        return index
def see_words(): #this will show a new window that we will use to show the trap words to the user
    w = 300
    h = 180
    #same logic as the main window except we want to show this a bit further left of the main window so they dont collide
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 3.7) - (w / 3.7)
    y = (hs / 3) - (h / 3)
    Window = Toplevel(window)
    Window.title("Banned Words")
    Window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    Window.configure(bg="#36393f",takefocus=True)
    Window.resizable(False, False)
    Window.iconphoto(False, photo)
    label = customtkinter.CTkLabel(master=Window, text="Trap words", text_font="Arial")
    label.pack()
    text = customtkinter.CTkCanvas(Window, width=250, height=50, bg="#36393f")


    text.create_text(123, 30, text=all_words[index], fill="white", font='none 20 bold')

    text.pack()

    #the command variables will run 3 functions, first it will create a new see_words() window when clicked, destroy the previous one, and then add 2 to the index to show a new words
    command =lambda : [see_words(),Window.destroy(),add_2()]
    customtkinter.CTkButton(master = Window, text="Next", width=60, height=30, fg_color="#228B22", bg_color='#36393f', hover_color='#32CD32',
                            command=command).place(x = 210, y = 90)
    #same logic except instead we remove 2 from the index
    command2 = lambda: [see_words(), Window.destroy(), remove_2()]
    customtkinter.CTkButton(master = Window, text="Previous", width=60, height=30, fg_color="#990000", bg_color='#36393f',border_color='#B30000',hover_color="#B30000",
                            command=command2).place(x = 30, y = 90)



#this function will open a window with an input field to add new words
def get_input():
    w = 200
    h = 150
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 1.4) - (w / 1.4)
    y = (hs / 3) - (h / 3)
    newWindow = Toplevel(window)
    newWindow.title("Add Trap Words")
    newWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
    newWindow.configure(bg="#36393f")
    newWindow.resizable(False, False)
    newWindow.iconphoto(False, photo)
    label = customtkinter.CTkLabel(master=newWindow, text="Only Add One Word\n", text_font="Arial")
    label.pack()

    # Create an Entry widget to accept User Input
    entry = customtkinter.CTkEntry(newWindow, width=100, corner_radius=8)
    entry.focus_set()
    entry.pack()

    # I need to run this nested function so the new word can be run as a parameter to the add_word function
    def word_get():
        word = entry.get()
        if word == "":
            return " "
        else:
            return word.lower()
    # we need to both destroy the window when we click ok and send the input to the csv file to be saved
    command = lambda: [add_word(word_get()), newWindow.destroy()]
    customtkinter.CTkButton(newWindow, text="Add Word", width=20, fg_color="#228B22", hover_color="#32CD32",
                            bg_color="#36393f", command=command).pack(pady=20)

#this is a simple info window for the user
def info():
    newWindow = Toplevel(window)
    newWindow.title("Information Center")
    newWindow.geometry("500x530")
    newWindow.configure(bg="#36393f")
    newWindow.resizable(False, False)
    newWindow.iconphoto(False, photo)
    label = customtkinter.CTkLabel(master=newWindow, text="Made by Rrez44", text_font="Calibri")
    label.pack()
    text = customtkinter.CTkCanvas(newWindow, width=430, height=400, bg="#36393f")
    text.create_text(160, 50,
                     text="• This program will read keyboard input and \nscreenshot when the trap words match your input",
                     fill="white", font='Arial')
    text.create_text(178, 100,
                     text="• The screenshots can be found by searching your \nfiles for pictures named [fullscreen+(number)]",
                     fill='white', font="Arial")
    text.create_text(193, 150,
                     text="• The program will run even after you close the window,\n to stop press the insert key",
                     fill='white', font="Arial")
    text.create_text(206, 200,
                     text="• Words you add should appear in lowercase, but for good\n measure add them in lower case yourself",
                     fill='white', font="Arial")
    text.create_text(204, 250, text="• New words that are added should appear after you reset\n the program",
                     fill='white', font="Arial")
    text.create_text(180, 300, text="• You may add numbers but not special characters,\n DONT USE SPACES WHEN YOU ADD WORDS",
                     fill='white', font="Arial")
    text.pack()

    command = lambda: [newWindow.destroy()]
    customtkinter.CTkButton(newWindow, text="Thanks!", width=20, fg_color="#228B22", hover_color="#32CD32",
                            bg_color="#36393f", command=command).pack(pady=20)


# originally supposed to run program on click but after implementing threading it starts the function itself and i cant be bothered to fix
but1 = lambda : [run_program()]
Button_1 = customtkinter.CTkButton(master=window,
                                   text="Program Running",
                                   text_font="none 20 bold",
                                   hover=True,
                                   hover_color="#9842E0",
                                   height=50,
                                   width=250,
                                   border_width=2,
                                   corner_radius=8,
                                   border_color="#421C61",
                                   bg_color="#36393f",
                                   fg_color="#6D2FA1",
                                   command=threading.Thread(target=but1).start())

Button_2 = customtkinter.CTkButton(master=window,
                                   text="Add Words",
                                   text_font="none 20 bold",
                                   hover=True,
                                   hover_color="#36ACD7",
                                   height=50,
                                   width=250,
                                   border_width=2,
                                   corner_radius=8,
                                   border_color="#18617B",
                                   bg_color="#36393f",
                                   fg_color="#2596be",
                                   command=get_input)
Button_3 = customtkinter.CTkButton(master=window,
                                   text="See Words",
                                   text_font="none 20 bold",
                                   hover=True,
                                   hover_color="#ff9d5c",
                                   height=50,
                                   width=250,
                                   border_width=2,
                                   corner_radius=8,
                                   border_color="#ff9d5c",
                                   bg_color="#36393f",
                                   fg_color="#cc7000",
                                   command=see_words)
Button_4 = customtkinter.CTkButton(master=window,
                                   text="Delete Words",
                                   text_font="none 20 bold",
                                   hover=True,
                                   hover_color="#B30000",
                                   height=50,
                                   width=250,
                                   border_width=2,
                                   corner_radius=8,
                                   border_color="#B30000",
                                   bg_color="#36393f",
                                   fg_color="#990000",
                                   command=delete_words)
Button_5 = customtkinter.CTkButton(master=window,
                                   text="i",
                                   text_font="Webdings",
                                   text_color="black",
                                   hover=True,
                                   hover_color="#ade6e6",
                                   height=50,
                                   width=50,
                                   border_width=2,
                                   corner_radius=8,
                                   border_color="#ade6e6",
                                   bg_color="#36393f",
                                   fg_color="#99ccff",
                                   command=info)
Button_6 = customtkinter.CTkButton(master=window,
                                   text="Close Window",
                                   text_font="none 17 bold",
                                   hover=True,
                                   hover_color="#A0787F",
                                   height=50,
                                   width=190,
                                   border_width=2,
                                   corner_radius=8,
                                   border_color="#A0787F",
                                   bg_color="#36393f",
                                   fg_color="#B2868E",
                                   command=window.destroy)
# placing the buttons
Button_1.place(x=15, y=10)
Button_2.place(x=15, y=70)
Button_3.place(x=15, y=130)
Button_4.place(x=15, y=190)
Button_5.place(x=210, y=250)
Button_6.place(x=15, y=250)

# run the main loop
window.mainloop()
