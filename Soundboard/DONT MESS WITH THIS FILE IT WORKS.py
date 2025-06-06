import keyboard # this imports all the modules that we need
import pygame
import time
import tkinter
from tkinter import *
from tkinter import filedialog, simpledialog
from tkinter.constants import *
import eyed3


pygame.init() # initalizes pygame assets
pygame.mixer.init()


tk = tkinter.Tk() # creates the soundboard window with tkinter
tk.title("Soundboard")
tk.geometry("942x557")


# sets default keybinds
key1 = '5'
key2 = '6'
key3 = '7'
key4 = '8'
key5 = '9'
key6 = '0'
key7 = '-'
key8 = '='
selecttitle=''
selectmp3=''
repeat=0


def browseFiles1(): # this browses through and selects files
    global filename1 # this makes the variable "filename1" global so it can be used outside of this function
    filename1 = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Music files",
                                                        "*.mp3*"),
                                                       ("all files",
                                                        "*.*"))) # this assigns the searched file to the variable
    audiofile = eyed3.load(filename1)
    global title1
    title1 = audiofile.tag.title
    global mp3length1
    mp3length1 = audiofile.info.time_secs
    button.configure(text=title1+"\nSelected")
   
def browseFiles2():
    global filename2
    filename2 = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Music files",
                                                        "*.mp3*"),
                                                       ("all files",
                                                        "*.*")))
    audiofile = eyed3.load(filename2)
    global title2
    title2 = audiofile.tag.title
    global mp3length2
    mp3length2 = audiofile.info.time_secs
    button2.configure(text=title2+"\nSelected")


def browseFiles3():
    global filename3
    filename3 = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Music files",
                                                        "*.mp3*"),
                                                       ("all files",
                                                        "*.*")))
    audiofile = eyed3.load(filename3)
    global title3
    title3 = audiofile.tag.title
    global mp3length3
    mp3length3 = audiofile.info.time_secs
    button3.configure(text=title3+"\nSelected")
   
def browseFiles4():
    global filename4
    filename4 = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Music files",
                                                        "*.mp3*"),
                                                       ("all files",
                                                        "*.*")))
    audiofile = eyed3.load(filename4)
    global title4
    title4 = audiofile.tag.title
    global mp3length4
    mp3length4 = audiofile.info.time_secs
    button4.configure(text=title4+"\nSelected")
   
def browseFiles5():
    global filename5
    filename5 = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Music files",
                                                        "*.mp3*"),
                                                       ("all files",
                                                        "*.*")))
    audiofile = eyed3.load(filename5)
    global title5
    title5 = audiofile.tag.title
    global mp3length5
    mp3length5 = audiofile.info.time_secs
    button5.configure(text=title5+"\nSelected")
   
def browseFiles6():
    global filename6
    filename6 = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Music files",
                                                        "*.mp3*"),
                                                       ("all files",
                                                        "*.*")))
    audiofile = eyed3.load(filename6)
    global title6
    title6 = audiofile.tag.title
    global mp3length6
    mp3length6 = audiofile.info.time_secs
    button6.configure(text=title6+"\nSelected")


def play1(): # defining the function called play1
        global repeat # defining the global variable repeat
        pygame.mixer.music.pause() # pauses the songs
        pygame.mixer.music.load(filename1) # loads teh file that you searched
        pygame.mixer.music.play(loops=repeat) #sets stuff on whether to repeat affter sound effect ends or not


def play2():
        global repeat
        pygame.mixer.music.pause()
        pygame.mixer.music.load(filename2)
        pygame.mixer.music.play(loops=repeat)
       
def play3():
        global repeat
        pygame.mixer.music.pause()
        pygame.mixer.music.load(filename3)
        pygame.mixer.music.play(loops=repeat)


def play4():
        global repeat
        pygame.mixer.music.pause()
        pygame.mixer.music.load(filename4)
        pygame.mixer.music.play(loops=repeat)


def play5():
        global repeat
        pygame.mixer.music.pause()
        pygame.mixer.music.load(filename5)
        pygame.mixer.music.play(loops=repeat)


def play6():
        global repeat
        pygame.mixer.music.pause()
        pygame.mixer.music.load(filename6)
        pygame.mixer.music.play(loops=repeat)


def pausemp3():
        pygame.mixer.music.pause()


def unpausemp3(): # defining the unpause function
    try:
        global selectmp3
        selectmp3=False
        global selecttitle # defines the selcttitle varible as global
        titlelabel.configure(text=selecttitle+" Playing") # makes the title of the selected mp3 say 'playing' om the tkinter button
        pygame.mixer.music.rewind #rewinds with slider
        pos_current=tslider.get() # finds position of the slider
        pygame.mixer.music.set_pos(pos_current) # sets position of the slider
        pygame.mixer.music.unpause() #unpauses on position of the slider
    except pygame.error as e:
        titlelabel.configure(text="Error: No sound loaded")


def update_keylabel(): # this just does keybinding
    keylabel.configure(text='Press '+key1+', '+key2+', '+key3+', '+key4+', '+key5+', and '+key6+'\nTo Play/Pause') # configures the button to show the keys and what yor keybinds are
    button7.configure(text="Change Keybind \n Currently set to "+key1, command=change_keybind1) #configures the keybind
    button8.configure(text="Change Keybind \n Currently set to "+key2, command=change_keybind2)
    button9.configure(text="Change Keybind \n Currently set to "+key3, command=change_keybind3)
    button10.configure(text="Change Keybind \n Currently set to "+key4, command=change_keybind4)
    button11.configure(text="Change Keybind \n Currently set to "+key5, command=change_keybind5)
    button12.configure(text="Change Keybind \n Currently set to "+key6, command=change_keybind6)


def change_keybind1(): # defines the change_keybind1 function
    global key1 # makes the key1 variable global
    ask_key = simpledialog.askstring("Change Keybind", "Enter new key for sound 1:", parent=tk) # finds the key
    new_key = ask_key[0] # sets the key as a new key
    if new_key: # if there's a new key then...
        keyboard.remove_hotkey(key1) #removes the original hotkey
        key1 = new_key # makes the detected key the new hotkey
        keyboard.add_hotkey(key1, toggle_sound1) #binds the hotkey with the function
        update_keylabel() # calls on the update_keylabel function


def change_keybind2():
    global key2
    ask_key = simpledialog.askstring("Change Keybind", "Enter new key for sound 2:", parent=tk)
    new_key = ask_key[0]
    if new_key:
        keyboard.remove_hotkey(key2)
        key2 = new_key
        keyboard.add_hotkey(key2, toggle_sound2)
        update_keylabel()


def change_keybind3():
    global key3
    ask_key = simpledialog.askstring("Change Keybind", "Enter new key for sound 3:", parent=tk)
    new_key = ask_key[0]
    if new_key:
        keyboard.remove_hotkey(key3)
        key3 = new_key
        keyboard.add_hotkey(key3, toggle_sound3)
        update_keylabel()


def change_keybind4():
    global key4
    ask_key = simpledialog.askstring("Change Keybind", "Enter new key for sound 4:", parent=tk)
    new_key = ask_key[0]
    if new_key:
        keyboard.remove_hotkey(key4)
        key4 = new_key
        keyboard.add_hotkey(key4, toggle_sound4)
        update_keylabel()


def change_keybind5():
    global key5
    ask_key = simpledialog.askstring("Change Keybind", "Enter new key for sound 5:", parent=tk)
    new_key = ask_key[0]
    if new_key:
        keyboard.remove_hotkey(key5)
        key5 = new_key
        keyboard.add_hotkey(key5, toggle_sound5)
        update_keylabel()


def change_keybind6():
    global key6
    ask_key = simpledialog.askstring("Change Keybind", "Enter new key for sound 6:", parent=tk)
    new_key = ask_key[0]
    if new_key:
        keyboard.remove_hotkey(key6)
        key6 = new_key
        keyboard.add_hotkey(key6, toggle_sound5)
        update_keylabel()


frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=8) # creates a tkinter frame
frame.pack(fill=BOTH,expand=1)


tslider = tkinter.Scale(frame, from_=0, to=0, orient=HORIZONTAL, length=250) # creates a tkinter slider
tslider.grid(row=1, column=2, columnspan=2)


exit = tkinter.Button(frame, text="Exit", command=tk.destroy) # creates the tkinter exit button
exit.config(width=20, height=3)
exit.grid(row=1,column=6, padx=2, pady=2)


button = tkinter.Button(frame, text="Browse Files", command = browseFiles1) # creates a tkinter button that browses files
button.config(width=20, height=25)
button.grid(row=2,column=1, padx=2, pady=2)


button2 = tkinter.Button(frame, text="Browse Files", command = browseFiles2)
button2.config(width=20, height=25)
button2.grid(row=2,column=2, padx=2, pady=2)


button3 = tkinter.Button(frame, text="Browse Files", command = browseFiles3)
button3.config(width=20, height=25)
button3.grid(row=2,column=3, padx=2, pady=2)


button4 = tkinter.Button(frame, text="Browse Files", command = browseFiles4)
button4.config(width=20, height=25)
button4.grid(row=2,column=4, padx=2, pady=2)


button5 = tkinter.Button(frame, text="Browse Files", command = browseFiles5)
button5.config(width=20, height=25)
button5.grid(row=2,column=5, padx=2, pady=2)


button6 = tkinter.Button(frame, text="Browse Files", command = browseFiles6)
button6.config(width=20, height=25)
button6.grid(row=2,column=6, padx=2, pady=2)


button7 = tkinter.Button(frame, text="Change Keybind \n Currently set to "+key1, command=change_keybind1) # creates a tkinter button that calls upon the chang_keybind1 function
button7.config(width=20, height=5)
button7.grid(row=3,column=1, padx=2, pady=2)


button8 = tkinter.Button(frame, text="Change Keybind \n Currently set to "+key2, command=change_keybind2)
button8.config(width=20, height=5)
button8.grid(row=3,column=2, padx=2, pady=2)


button9 = tkinter.Button(frame, text="Change Keybind \n Currently set to "+key3, command=change_keybind3)
button9.config(width=20, height=5)
button9.grid(row=3,column=3, padx=2, pady=2)


button10 = tkinter.Button(frame, text="Change Keybind \n Currently set to "+key4, command=change_keybind4)
button10.config(width=20, height=5)
button10.grid(row=3,column=4, padx=2, pady=2)


button11 = tkinter.Button(frame, text="Change Keybind \n Currently set to "+key5, command=change_keybind5)
button11.config(width=20, height=5)
button11.grid(row=3,column=5, padx=2, pady=2)


button12 = tkinter.Button(frame, text="Change Keybind \n Currently set to "+key6, command=change_keybind6)
button12.config(width=20, height=5)
button12.grid(row=3,column=6, padx=2, pady=2)


keylabel = tkinter.Label(frame, text='Press '+key1+', '+key2+', '+key3+', '+key4+', '+key5+', and '+key6+'\nTo Play/Pause') # Creates some text using tkinter
keylabel.config(width=20, height=3)
keylabel.grid(row=1,column=5, padx=2, pady=2)


titlelabel = tkinter.Label(frame, text='Nothing Playing') # creates some more text with tkinter
titlelabel.config(width=20, height=3)
titlelabel.grid(row=1,column=1, padx=2, pady=2)


unpauselabel = tkinter.Label(frame, text='Press '+key7+' to Unpause from \nthe Current Location '+'\n'+key8+' to Turn Looping on') # creates text that is reconfigured to show whether something is playing or not
unpauselabel.config(width=20, height=3)
unpauselabel.grid(row=1,column=4, padx=2, pady=2)


# Pause state tracking
selectmp3=True


def toggle_sound1():  # defines the toggle_sound1 function
    global music1_paused  # makes these variables global
    global selecttitle
    global selectmp3
    try:
        music1_paused=selectmp3
        selecttitle = title1
        if music1_paused:  # sees if music1 is paused
            selectmp3 = False  # makes music1_paused equal False
            play1()  # calls on the play1 function
            tslider.configure(from_=0, to=mp3length1)  # configures the slider to change position
            titlelabel.configure(text=title1 + " Playing")  # updates the GUI with playing status
        else:
            pausemp3()  # calls on the pausemp3 function
            selectmp3 = True  # makes music1_paused equal True
            titlelabel.configure(text=title1 + " Paused")
    except NameError as e:
        # Handle the NameError gracefully by updating the GUI or logging the error
        titlelabel.configure(text="Error: No sound loaded")


def toggle_sound2():
    global music2_paused
    global selecttitle
    global selectmp3
    try:
        music2_paused=selectmp3
        selecttitle = title2
        if music2_paused:
            selectmp3 = False
            play2()
            tslider.configure(from_=0, to=mp3length2)
            titlelabel.configure(text=title2 + " Playing")
        else:
            pausemp3()
            selectmp3 = True
            titlelabel.configure(text=title2 + " Paused")
    except NameError as e:
        titlelabel.configure(text="Error: No sound loaded")


def toggle_sound3():
    global music3_paused
    global selecttitle
    global selectmp3
    try:
        music3_paused=selectmp3
        selecttitle = title3
        if music3_paused:
            selectmp3 = False
            play3()
            tslider.configure(from_=0, to=mp3length3)
            titlelabel.configure(text=title3 + " Playing")
        else:
            pausemp3()
            selectmp3 = True
            titlelabel.configure(text=title3 + " Paused")
    except NameError as e:
        titlelabel.configure(text="Error: No sound loaded")


def toggle_sound4():
    global music4_paused
    global selecttitle
    global selectmp3
    try:
        music4_paused=selectmp3
        selecttitle = title4
        if music4_paused:
            selectmp3 = False
            play4()
            tslider.configure(from_=0, to=mp3length4)
            titlelabel.configure(text=title4 + " Playing")
        else:
            pausemp3()
            selectmp3 = True
            titlelabel.configure(text=title4 + " Paused")
    except NameError as e:
        titlelabel.configure(text="Error: No sound loaded")


def toggle_sound5():
    global music5_paused
    global selecttitle
    global selectmp3
    try:
        music5_paused=selectmp3
        selecttitle = title5
        if music5_paused:
            selectmp3 = False
            play5()
            tslider.configure(from_=0, to=mp3length5)
            titlelabel.configure(text=title5 + " Playing")
        else:
            pausemp3()
            selectmp3 = True
            titlelabel.configure(text=title6 + " Paused")
    except NameError as e:
        titlelabel.configure(text="Error: No sound loaded")


def toggle_sound6():
    global music6_paused
    global selecttitle
    global selectmp3
    try:
        music6_paused=selectmp3
        selecttitle = title6
        if music6_paused:
            selectmp3 = False
            play6()
            tslider.configure(from_=0, to=mp3length6)
            titlelabel.configure(text=title6 + " Playing")
        else:
            pausemp3()
            selectmp3 = True
            titlelabel.configure(text=title6 + " Paused")
    except NameError as e:
        titlelabel.configure(text="Error: No sound loaded")


def loop(): # defiens the function 'loop'
    global repeat
    if repeat==0:
        unpauselabel.configure(text='Press '+key7+' to Unpause from \nthe Current Location '+'\n'+key8+' to Turn Looping off')
        repeat=-1
    elif repeat==-1:
        repeat=0
        unpauselabel.configure(text='Press '+key7+' to Unpause from \nthe Current Location '+'\n'+key8+' to Turn Looping on')


# Assign keys to the toggle functions. Here, keys '5', '6', and '7' trigger the functions.
keyboard.add_hotkey(key1, toggle_sound1)
while keyboard.is_pressed(key1):
    time.sleep(0.1)  # Prevent multiple plays from one press of button
keyboard.add_hotkey(key2, toggle_sound2)
while keyboard.is_pressed(key2):
    time.sleep(0.1)  # Prevent multiple plays from one press of button
keyboard.add_hotkey(key3, toggle_sound3)
while keyboard.is_pressed(key3):
    time.sleep(0.1)  # Prevent multiple plays from one press of button
keyboard.add_hotkey(key4, toggle_sound4)
while keyboard.is_pressed(key4):
    time.sleep(0.1)  # Prevent multiple plays from one press of button
keyboard.add_hotkey(key5, toggle_sound5)
while keyboard.is_pressed(key5):
    time.sleep(0.1)  # Prevent multiple plays from one press of button
keyboard.add_hotkey(key6, toggle_sound6)
while keyboard.is_pressed(key6):
    time.sleep(0.1)  # Prevent multiple plays from one press of button
keyboard.add_hotkey(key7, unpausemp3)
while keyboard.is_pressed(key7):
    time.sleep(0.1)  # Prevent multiple plays from one press of button
keyboard.add_hotkey(key8, loop) # this is a key that makes the sound loop if you want
while keyboard.is_pressed(key8):
    time.sleep(0.1)  # Prevent multiple plays from one press of button


tk.mainloop()


"({{('/''|""Work-Better""':)}})"



