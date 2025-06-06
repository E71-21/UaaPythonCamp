import keyboard # this imports all the modules that we need
import pygame
import time
import eyed3.mp3
import keyboard
import tkinter
from tkinter import filedialog
from tkinter.constants import *
from pathlib import Path
from pathlib import PureWindowsPath
import os
import eyed3



pygame.init() # initalizes pygame assets
pygame.mixer.init()


key1 = '5'
key2 = '6'
key3 = '7'
key4 = '8'
key5 = '9'
key6 = '0'

tk = tkinter.Tk() # creates the soundboard window with tkinter
tk.title("Soundboard")
tk.geometry("915x532")




def browseFiles1(): # this browses through and selects files
    global filename1 # this makes the variable "filename1" global so it can be used outside of this function
    filename1 = filedialog.askopenfilename(initialdir = "/", # this assigns the searched file to the variable
                                          title = "Select a File",
                                          filetypes = (("Music files",
                                                        "*.mp3*"),
                                                       ("all files",
                                                        "*.*")))
    audiofile = eyed3.load(filename1) # finds the file title name
    global title1 # ,ales the variable title1 global so it can be used outside of this function
    title1 = audiofile.tag.title
    button.configure(text="5\n"+title1+"\nSelected") #configures the Tkinter button to display the title of the file playing




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
    button2.configure(text="6\n"+title2+"\nSelected")




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
    button3.configure(text="7\n"+title3+"\nSelected")




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
    button4.configure(text="8\n"+title4+"\nSelected")




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
    button5.configure(text="9\n"+title5+"\nSelected")




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
    button6.configure(text="0\n"+title6+"\nSelected")





def play1(): #this is a function
        pygame.mixer.music.load(filename1) # loads the .mp3 file
        pygame.mixer.music.play(loops=0) # plays the loaded file




def play2():
        pygame.mixer.music.load(filename2)
        pygame.mixer.music.play(loops=0)




def play3():
        pygame.mixer.music.load(filename3)
        pygame.mixer.music.play(loops=0)




def play4():
        pygame.mixer.music.load(filename4)
        pygame.mixer.music.play(loops=0)




def play5():
        pygame.mixer.music.load(filename5)
        pygame.mixer.music.play(loops=0)




def play6():
        pygame.mixer.music.load(filename6)
        pygame.mixer.music.play(loops=0)




def pausemp3():
        pygame.mixer.music.pause()




frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=8)
frame.pack(fill=BOTH,expand=1)


#tslider = tkinter.Scale(frame, from_=0, to=-1, orient=HORIZONTAL, length=250)
#tslider.grid(row=1, column=2, columnspan=2)


exit = tkinter.Button(frame, text="Exit", command=tk.destroy)
exit.config(width=20, height=3)
exit.grid(row=1,column=6)


button = tkinter.Button(frame, text=f"choose file for \n the {key1} key", command = browseFiles1)
button.config(width=20, height=30)
button.grid(row=3,column=1)


button2 = tkinter.Button(frame, text=f"choose file for \n the {key2} key", command = browseFiles2)
button2.config(width=20, height=30)
button2.grid(row=3,column=2)


button3 = tkinter.Button(frame, text=f"choose file for \n the {key3} key", command = browseFiles3)
button3.config(width=20, height=30)
button3.grid(row=3,column=3)


button4 = tkinter.Button(frame, text=f"choose file for \n the {key4} key", command = browseFiles4)
button4.config(width=20, height=30)
button4.grid(row=3,column=4)


button5 = tkinter.Button(frame, text=f"choose file for \n the {key5} key", command = browseFiles5)
button5.config(width=20, height=30)
button5.grid(row=3,column=5)


button6 = tkinter.Button(frame, text=f"choose file for \n the {key6} key", command = browseFiles6)
button6.config(width=20, height=30)
button6.grid(row=3,column=6)


#these will change the keybind

def on_release(event):
    event.widget.config(relief=tk.RAISED)




button7 = tkinter.Button(frame, text="change keybind")
button7.config(width=20, height=5)
button7.grid(row=2,column=1)


button8 = tkinter.Button(frame, text="change keybind")
button8.config(width=20, height=5)
button8.grid(row=2,column=2)


button9 = tkinter.Button(frame, text="change keybind")
button9.config(width=20, height=5)
button9.grid(row=2,column=3)


button10 = tkinter.Button(frame, text="change keybind")
button10.config(width=20, height=5)
button10.grid(row=2,column=4)


button11 = tkinter.Button(frame, text="change keybind")
button11.config(width=20, height=5)
button11.grid(row=2,column=5)


buttont12 = tkinter.Button(frame, text="change keybind")
buttont12.config(width=20, height=5)
buttont12.grid(row=2,column=6)


keylabel = tkinter.Label(frame, text=f'Press {key1}, {key2}, {key3}, {key4}, {key5}, {key6} \nTo Play Sounds')
keylabel.config(width=20, height=3)
keylabel.grid(row=1,column=5)


titlelabel = tkinter.Label(frame, text='Nothing Playing')
titlelabel.config(width=20, height=3)
titlelabel.grid(row=1,column=1)




# Pause state tracking
music1_paused = True
music2_paused = True
music3_paused = True
music4_paused = True
music5_paused = True
music6_paused = True




def toggle_sound1(): #defining a function
    global music1_paused #declares a global variable to be used outside of this function
    if music1_paused == True: #checkes if music1 is paused and if its true unpauses it and plays the song
        music1_paused = False
        play1() # calls on a previously designed project to
        titlelabel.configure(text=title1+" Playing") #shows the title of the song playing
    else:
        pausemp3() #calls on a previously defined function to pause the song
        music1_paused = True #says that music1 is paused
        titlelabel.configure(text=title1+" Paused") # says on GUI that it is paused








def toggle_sound2():
    global music2_paused
    if music2_paused == True:
        music2_paused = False
        play2()
        titlelabel.configure(text=title2+" Playing")
    else:
        pausemp3()
        music2_paused = True
        titlelabel.configure(text=title2+" Paused")




def toggle_sound3():
    global music3_paused
    if music3_paused == True:
        music3_paused = False
        play3()
        titlelabel.configure(text=title3+" Playing")
    else:
        pausemp3()
        music3_paused = True
        titlelabel.configure(text=title3+" Paused")




def toggle_sound4():
    global music4_paused
    if music4_paused == True:
        music4_paused = False
        play4()
        titlelabel.configure(text=title4+" Playing")
    else:
        pausemp3()
        music4_paused = True
        titlelabel.configure(text=title4+" Paused")




def toggle_sound5():
    global music5_paused
    if music5_paused == True:
        music5_paused = False
        play5()
        titlelabel.configure(text=title5+" Playing")
    else:
        pausemp3()
        music5_paused = True
        titlelabel.configure(text=title5+" Paused")




def toggle_sound6():
    global music6_paused
    if music6_paused == True:
        music6_paused = False
        play6()
        titlelabel.configure(text=title6+" Playing")
    else:
        pausemp3()
        music6_paused = True
        titlelabel.configure(text=title1+" Paused")






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




tk.mainloop()
