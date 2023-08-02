import tkinter #this module will provide the GUI
gui = tkinter.Tk() #create GUI object
gui.title("Calculator") #name the GUI object
# gui.geometry("200x600") #set size of calculator GUI. This will be changed by the sticky and columnconfigure/row_configure commands
gui_width = 300
gui_height = 300
gui.geometry(str(gui_width) + 'x' + str(gui_height))
#give rows and columns equal weight relative to each other to the window will resize according to these proportions to snugly fit everything:
gui.columnconfigure(1, weight=1)
gui.columnconfigure(2, weight=1)
gui.columnconfigure(3, weight=1)
gui.columnconfigure(4, weight=1)
gui.rowconfigure(1, weight=1)
gui.rowconfigure(2, weight=1)
gui.rowconfigure(3, weight=1)
gui.rowconfigure(4, weight=1)
gui.rowconfigure(5, weight=1)

#declare a simple empty string that will be filled up with numbers and operators
text = ''

#create a function that dictates what happens when a number or operator button is pressed
def press(button):
    global text # to affect the text variable that is outside of this function
    text = text + str(button) #add the pressed button's value onto the text string
    expression.set(text) #expression, which will be defined later outside of this function, will change to read out the updated text

#create a function for when the equals button is pressed
def equals():
    try:
        global text #again, want to affect text outside of this function
        result = str(eval(text)) #use eval function to calculate the text, then set it back into string form
        expression.set(result) #have the result read out as expression; expression will be linked to the readout later
        text = '' #start over, so nothing from what was done before carries over to what comes after
    except: #if the evaluation cannot go through for some reason
        expression.set('ERROR') #readout that there was an error
        text = '' #start fresh again

#create a function to connect to a button to manually clear what has been inputted
def clear():
    global text # as with the other functions
    text = '' #clear the text
    expression.set('') #clear the readout

expression = tkinter.StringVar()

text_box = tkinter.Entry(gui, textvariable=expression) #create a text box object containing that text
text_box.grid(row=1, # have it be on the top row
    columnspan = 4, #have it span all four columns that I will be creating. This brings it to the beginning of the 5th column, so spans all 4 working columns
    ipadx = 0, #make the text box itself thicker width-wise
    ipady = 20, #make the text box itself thicker height-wise
    pady = 30, #give it a margin on top of it and below it of 30 pixels
    stick = 'we') #have it stretch the entire width (west and east) of its cell, which is effectively all columns of row 1
buttonclear = tkinter.Button(gui, text = 'Clear', fg='black', bg='red', height=2, width=8, command = lambda: clear())
buttonclear.grid(row=1, column=4)

button7 = tkinter.Button(gui, text=' 7 ', fg='black', bg='red', height=2, width=8, command= lambda: press(7))
button7.grid(row=2, column=1)
button8 = tkinter.Button(gui, text=' 8 ', fg='black', bg='red', height=2, width=8, command= lambda: press(8))
button8.grid(row=2, column=2)
button9 = tkinter.Button(gui, text=' 9 ', fg='black', bg='red', height=2, width=8, command= lambda: press(9))
button9.grid(row=2, column=3)
buttonplus = tkinter.Button(gui, text=' + ', fg='black', bg='red', height=2, width=8, command= lambda: press('+'))
buttonplus.grid(row=2, column=4)

button4 = tkinter.Button(gui, text=' 4 ', fg='black', bg='red', height=2, width=8, command= lambda: press(4))
button4.grid(row=3, column=1)
button5 = tkinter.Button(gui, text=' 5 ', fg='black', bg='red', height=2, width=8, command= lambda: press(5))
button5.grid(row=3, column=2)
button6 = tkinter.Button(gui, text=' 6 ', fg='black', bg='red', height=2, width=8, command= lambda: press(6))
button6.grid(row=3, column=3)
buttonminus = tkinter.Button(gui, text=' - ', fg='black', bg='red', height=2, width=8, command= lambda: press('-'))
buttonminus.grid(row=3, column=4)

button1 = tkinter.Button(gui, text=' 1 ', fg='black', bg='red', height=2, width=8, command= lambda: press(1))
button1.grid(row=4, column=1)
button2 = tkinter.Button(gui, text=' 2 ', fg='black', bg='red', height=2, width=8, command= lambda: press(2))
button2.grid(row=4, column=2)
button3 = tkinter.Button(gui, text=' 3 ', fg='black', bg='red', height=2, width=8, command= lambda: press(3))
button3.grid(row=4, column=3)
buttontimes = tkinter.Button(gui, text=' X ', fg='black', bg='red', height=2, width=8, command= lambda: press('*'))
buttontimes.grid(row=4, column=4)

button0 = tkinter.Button(gui, text=' 0 ', fg='black', bg='red', height=2, width=8, command= lambda: press(0))
button0.grid(row=5, column=1)
buttondot = tkinter.Button(gui, text=' . ', fg='black', bg='red', height=2, width=8, command= lambda: press('.'))
buttondot.grid(row=5, column=2)
buttonequals = tkinter.Button(gui, text=' = ', fg='black', bg='red', height=2, width=8, command= lambda: equals())
buttonequals.grid(row=5, column=3)
buttondivide = tkinter.Button(gui, text=' ÷ ', fg='black', bg='red', height=2, width=8, command= lambda: press('/'))
buttondivide.grid(row=5, column=4)



gui.mainloop() #run the gui window
