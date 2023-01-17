import tkinter as tk
from tkinter import ttk
from tkinter import *
import random


# Password generator
# Goals: - Refresh knowledge on python through use of random library and functions
#        - Learn tkinter library to create basic GUI
#
# Bugs: - generated passwords are not centered dispite using grid cords
#       - as a result, label, entry box, and button are slighty shifted to the left
#
#
# Notes: - used various methods to create updating scroll bar, final version had to be done using global space


root = tk.Tk()

# set title of gui
root.title("Password Generator")

# set icon of gui (remove this when sending to github)
root.iconbitmap('c:/Users/reima/Code/Python/Projects/gui/password_gen/pw.ico')

# set dimensions of window
root.geometry("500x200")

# creates a canvas 
canvas = tk.Canvas(root)

# creates a frame
frame = tk.Frame(canvas)

# creates a scrollbar
scrollbar = tk.Scrollbar(root)

def generate(n):
    
    # Variables for character lists
    up_lst = []
    low_lst = []
    spec_list = []
    num_list = []

    # list generation
    for up_letter in range(26):
        up_lst.append(chr(65+up_letter)) # unicode for upper case

    for low_letter in range(26):
        low_lst.append(chr(97+low_letter)) # unicode for lowercase

    spec = "~@#$%^&*(){|}<>.-_=+[]" # random symbols
    for char in spec:
        spec_list.append(char)

    for num in range(10):
        num_list.append(str(num)) # numbers between 0-9
    
    # list shuffle
    lst = [num_list,spec_list, low_lst, up_lst] 
    for thing in lst:
        random.shuffle(thing) # shuffles each list

    # loop that picks random character from each list until length - (check) is reached
    halfpass = []
    for i in range((n-4)):

        # randomly generated numbers that fit each lists max length
        num1 = random.randint(0,len(num_list)-1)
        num2 = random.randint(0,len(spec_list)-1)
        num3 = random.randint(0,len(low_lst)-1)
        num4 = random.randint(0,len(up_lst)-1)

        # lists the randomly chosen charactr from each list
        lst = [num_list[num1],spec_list[num2], low_lst[num3], up_lst[num4]]

        # randomly chooses one character from the list of chosen characters with equal weight
        random_lst = random.choices(lst, weights=(25,25,25,25), k = 1)

        #appends random character to new list
        halfpass.append(random_lst[0])

    # generates a check that gaurentees valid password 
    # numbers are rerolled to gaurentee unpredictability

    num1 = random.randint(0,len(num_list)-1)
    num2 = random.randint(0,len(spec_list)-1)
    num3 = random.randint(0,len(low_lst)-1)
    num4 = random.randint(0,len(up_lst)-1)
    check = "".join([num_list[num1],spec_list[num2], low_lst[num3], up_lst[num4]])

    # combines randomly generated list with check 
    halfstr = "".join(halfpass)
    fullstr = check + halfstr

    # randomly scrambles string so that the last 4 characters arn't always one of each
    password = "".join(random.sample(fullstr, len(fullstr)))

    return password

# Updates the scrollable region of the Canvas to encompass all the widgets in the Frame
def updateScrollRegion():
	canvas.update_idletasks()
	canvas.config(scrollregion=frame.bbox())

# Sets up the Canvas, Frame, and scrollbars for scrolling
def createScrollableContainer():
	canvas.config(yscrollcommand=scrollbar.set, highlightthickness=0)
	scrollbar.config(orient=tk.VERTICAL, command=canvas.yview)

	scrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
	canvas.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.TRUE)
	canvas.create_window(0, 0, window=frame, anchor=tk.NW)


i = 3
def click(entry, frame):
    global i
    # label = ttk.Label(frame, text = "u clicked the button!")
    # label.grid(row = i, column = 0)

    # saves current input as an integer
    n = entry.get() 

    if (n.isdigit()):
        # uses length givene by input to generate password
        n = int(n)
        password = generate(n)

        # creates text widget for password 
        pw = Text(frame, height=1)
        # inserts passowrd into text widget with length 1
        pw.insert(1.0, password)

        # displays at next available spot
        pw.grid(row = i, column = 0)

        # configures background of text to be same as root background and removes text box
        pw.configure(bg = frame.cget('bg'), relief = "flat", font =('Arial', 10)) 
        # text cannot be directly interacted with (can be highlighted and copied)
        pw.configure(state = "disabled")

    else:
        entry.delete(0, END)
        entry.insert(0, "Invalid input")

    updateScrollRegion()
    i += 1 

# adds necessary widgets to use program
def interface():
    
    top = ttk.Label(frame, text = "Enter password length:")
    top.grid(row = 0, column = 0)

    entry = ttk.Entry(frame, width = 50)
    entry.grid(row = 1, column = 0)

    button = ttk.Button(frame, text = "Enter", command = lambda: click(entry, frame))
    button.grid(row = 2, column = 0)


createScrollableContainer()
interface()

root.mainloop()