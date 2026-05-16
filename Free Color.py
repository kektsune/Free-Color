# -------------------------------------------------------------------------
#   INFO
# -------------------------------------------------------------------------
# Name:         Free Color
# Purpose:      A simple program that allows the user to free draw and change drawing options
# Programmer:   Kektsune
# Date:         01/16/2026
# -------------------------------------------------------------------------

from tkinter import *
from tkinter import colorchooser

window=Tk() 
window.title("Free Color!!")


#Sets the dimensions of the page close to the screen size
SCREEN_WIDTH = window.winfo_screenwidth() - 150
SCREEN_HEIGHT = window.winfo_screenheight() - 150

colorHex='black'

sizeAnswer = 5

#Creates a canvas
canvas = Canvas(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
canvas.pack(side=TOP)

titleText = canvas.create_text(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, text="Welcome to Free Color! Click anywhere to get started!", anchor="center")
tag = canvas.create_text(SCREEN_WIDTH/2, (SCREEN_HEIGHT/2) + 100, text="by: Kektsune", anchor="center")

current_shape = "Line"

# ----------------------- FUNCTIONS ---------------------- #

#Chooses the color and stores it (and removes intro text)
def colorPicker(): 
    canvas.delete(titleText)
    canvas.delete(tag)
    global colorHex
    color = colorchooser.askcolor() 
    colorHex = color[1] 

#Allows drawing input when left clicking the mouse
def drag_start(event):
    global sizeAnswer
    canvas.delete(titleText)
    canvas.delete(tag)
    window.startX = event.x
    window.startY = event.y
    if(current_shape=="Line"): 
        shape = canvas.create_line(event.x+4,event.y+4,event.x, event.y, fill=colorHex, width=sizeAnswer)
    elif(current_shape=="Rectangle"): 
        shape = canvas.create_rectangle(event.x+4,event.y+4,event.x, event.y, fill=colorHex, outline=colorHex, width=sizeAnswer)
    elif(current_shape=="Misc"): 
        shape = canvas.create_arc(event.x+4,event.y+4,event.x, event.y, outline=colorHex, width=sizeAnswer)
    elif(current_shape=="Oval"): 
        shape = canvas.create_oval(event.x+4,event.y+4,event.x, event.y, fill=colorHex, outline=colorHex, width=sizeAnswer)
    shape

#Allows drawing input when dragging the mouse
def drag_motion(event):
    global sizeAnswer
    canvas.delete(titleText)
    canvas.delete(tag)
    x = event.x 
    y = event.y
    if(current_shape=="Line"): 
        shape = canvas.create_line(event.x+4,event.y+4,event.x, event.y, fill=colorHex, width=sizeAnswer)
    elif(current_shape=="Rectangle"): 
        shape = canvas.create_rectangle(event.x+4,event.y+4,event.x, event.y, fill=colorHex, outline=colorHex, width=sizeAnswer)
    elif(current_shape=="Misc"): 
        shape = canvas.create_arc(event.x+4,event.y+4,event.x, event.y, outline=colorHex, width=sizeAnswer)
    elif(current_shape=="Oval"): 
        shape = canvas.create_oval(event.x+4,event.y+4,event.x, event.y, fill=colorHex, outline=colorHex, width=sizeAnswer)
    shape

#Removes any leftover marks on the page by deleting the canvas and making a new one
def clearPage():
    global canvas
    canvas.destroy()
    canvas = Canvas(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    canvas.pack(side=TOP)
    canvas.bind("<Button-1>", drag_start)
    canvas.bind("<B1-Motion>", drag_motion)

#Changes size of drawing strokes by opening a window of options
def changeSize():
    global warningLabel, sizeEntry, notifier
    canvas.delete(titleText)
    canvas.delete(tag)
    new_window = Toplevel() 
    title = Label(new_window, text="What size would you like to change the brush to?")
    title.pack()
    sizeEntry = Entry(new_window)
    sizeEntry.pack()
    notifier = Label(new_window, text="")
    notifier.pack()
    warningLabel = Label(new_window, text="")
    warningLabel.pack()
    submitButton = Button(new_window, text="Submit", command=submit)
    submitButton.pack()

#Submits a number to size to change the size globally
def submit():
    global sizeAnswer
    try:
        sizeAnswer = int(sizeEntry.get())
        notifier.config(text="You have changed the size to: " + str(sizeAnswer))
        warningLabel.config(text="")
    except ValueError:
        warningLabel.config(text="Please enter a number.", fg='red')
    
    sizeEntry.delete(0, END)

#Gives the option to change the drawing style, aka shape via new window
def changeShape():
    global warningLabel, effectedLabel
    canvas.delete(titleText)
    canvas.delete(tag)
    new_window_2 = Toplevel() 
    title = Label(new_window_2, text="What shape would you like to change the draw style to?")
    title.grid(row=0, column=0, columnspan=2)
    frameShapes = Frame(new_window_2)
    frameShapes.grid(row=1, column=0)
    lineButton = Button(frameShapes, text="Line", command=submitLine)
    lineButton.grid(row=2, column=0, padx=10, pady=10)
    rectangleButton = Button(frameShapes, text="Rectangle", command=submitRectangle)
    rectangleButton.grid(row=2, column=1, padx=10, pady=10)
    arcButton = Button(frameShapes, text="Miscellaneous", command=submitArc)
    arcButton.grid(row=2, column=2, padx=10, pady=10)
    ovalButton = Button(frameShapes, text="Oval", command=submitOval)
    ovalButton.grid(row=2, column=3, padx=10, pady=10)
    effectedLabel = Label(new_window_2, text="")
    effectedLabel.grid(row=3, column=0, columnspan=2)

#Line option
def submitLine():
    global current_shape
    current_shape = "Line"
    effectedLabel.config(text="Changed shape to a line!")

#Rectangle option
def submitRectangle():
    global current_shape
    current_shape = "Rectangle"
    effectedLabel.config(text="Changed shape to a rectangle!")

#Miscelleanous option
def submitArc():
    global current_shape
    current_shape = "Misc"
    effectedLabel.config(text="Changed shape to miscelleanous shape!")

#Oval option
def submitOval():
    global current_shape
    current_shape = "Oval"
    effectedLabel.config(text="Changed shape to an oval!")

# ----------------------- WIDGET SETUP ---------------------- #

frame = Frame(window) #Creates a frame widget, adding it to the window, making the background color pink, creating a border, and using the sunken border
frame.pack(side=BOTTOM)

changeSizeButton = Button(frame, text='Click to change brush size!', command=changeSize) 
changeSizeButton.pack(side=LEFT) 

changeShapeButton = Button(frame, text='Click to change drawing shape!', command=changeShape) 
changeShapeButton.pack(side=LEFT) 

colorButton = Button(frame, text='Click to choose a color!', command=colorPicker) 
colorButton.pack(side=LEFT) 

clearButton = Button(frame, text='Click to clear!', command=clearPage) 
clearButton.pack(side=LEFT) 

canvas.bind("<Button-1>", drag_start)
canvas.bind("<B1-Motion>", drag_motion)

window.mainloop()