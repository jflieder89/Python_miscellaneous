import tkinter #this module will provide the GUI
import re #use regex this for some of the more tricky functions lihe negate (+/-) and reciprocal
gui = tkinter.Tk() #create GUI object
gui.title("Calculator") #name the GUI object
# gui.geometry("200x600") #set size of calculator GUI. This will be changed by the sticky and columnconfigure/row_configure commands
gui_width = 450
gui_height = 300
gui.geometry(str(gui_width) + 'x' + str(gui_height))
#give rows and columns equal weight relative to each other to the window will resize according to these proportions to snugly fit everything:
gui.columnconfigure(1, weight=1)
gui.columnconfigure(2, weight=1)
gui.columnconfigure(3, weight=1)
gui.columnconfigure(4, weight=1)
gui.columnconfigure(5, weight=1)
gui.columnconfigure(6, weight=1)
gui.rowconfigure(1, weight=1)
gui.rowconfigure(2, weight=1)
gui.rowconfigure(3, weight=1)
gui.rowconfigure(4, weight=1)
gui.rowconfigure(5, weight=1)

#declare a simple empty string that will be filled up with numbers and operators
text = ''
result = '' #declare so I can try to keep a result after pressing equals, to roll right into another expression with a previous result

#create a function that dictates what happens when a number or operator button is pressed
def press(button):
    global text # to affect the text variable that is outside of this function
    global result
    if (button in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '.']) and (result != ''): #if digit/decimal pressed when result is present
        text += str(button)
        result = ''
    elif result != '': #if there is a result and something other than digit/decimal is pressed
        text = text + str(button) #add the pressed button's value onto the text string
    else: #if there is no result when a press function was called
        text += str(button)
    display.set(text) #display, which will be defined later outside of this function, will change to read out the updated text

#create a function for when the equals button is pressed
def equals():
    try:
        global text #again, want to affect text outside of this function
        global result
        result = eval(text) #use eval function to calculate the text. This will put in it int or float form, depending on it division was used
        if float(result) == int(result): #if no decimal place is needed, like 20 / 2, where the int form loses no info compared to the float form
            result = str(int(result))
        else: #if the flaot is different than the, implying the decimal places matter and should be kept
            result = str(float(result))
        display.set(result) #have the result read out as display; display will be linked to the readout later
        text = str(result) #set text to be this last result, so it can be used going forward if an operation is pressed next
    except: #if the evaluation cannot go through for some reason
        display.set('ERROR') #readout that there was an error, probably caused during the eval function
        text = '' #start fresh again

#create a function to connect to a button to manually clear what has been inputted
def clear():
    global text # as with the other functions
    global result
    text = '' #clear the text
    result = ''
    display.set('') #clear the readout

#create a function for backspace
def backspace():
    global text
    if len(text) > 0: #if there is any text at this point
        text_2 = text[:] #create a new text string copy using a slice so there is no copy funny business
        text = text_2[:-1] #take off the last inputted character then reassign to text
        display.set(text)

#create a function for negate (+/-)
def negate():
    global text
    #first deal with turning a negative number into a positive number
    # print('original text is: ', text, end= ". ")
    neg_number = False
    if (re.search('\(-\d+\.*\d*\)*$', text) != None): #if text ends ($) in ( then - then digits (decimal point and numbers after being optional) then an optional ) and is therefore a negative number
        # print(text, 'ends in negative number', end = '. ')
        neg_number = True #this was a negative number
        index = -1 #to keep track of where in the string I'm checking
        end_paren_count = 0 # to keep track of how many closing parentheses there are at the end
        while text[index] == ')': #if it ends in a closing parenthesis, whether it be one or more closing parentheses
            index -= 1 #go to the left of that character in the text
            end_paren_count += 1 #to signify a closing parenthesis is at the end
        while (len(text) + index > -1): #so we don't search for more characters of the string than there are characters in the string
            if text[index] == '.':
                index -= 1
                continue #go back to while loop
            try:
                int(text[index]) #if this element is a digit
                index -= 1
            except: #if this element is not a digit or decimal point
                break
        to_keep = text[1:index] #put the 1 at the beginning of the slice to get rid of the now unnecessary opening parenthesis
        # print('to_keep is : ', to_keep, end='. ')
        changed = text[index+1:-1] #put the -1 at the ending of the slice to get rid of the now unnecessary closing parenthesis
        # print('changed is :', changed, end='. ')
        text = to_keep + changed
        display.set(text)
        # print('new text after negative number found is: ', text)
    if (neg_number == False) and ( (re.search('\d+\.*\d*$', text) != None) or (re.search('\(\d+\.*\d*\)*$', text) != None) ): # if the text was not just changed into positive number by the first part of this function and fits te positive number ending pattern
        # print(text, 'ends in a positive number', end='. ')
        neg_number = True #this was a negative number
        index = -1 #to keep track of where in the string I'm checking
        end_paren_count = 0 # to keep track of how many closing parentheses there are at the end
        while text[index] == ')': #if it ends in a closing parenthesis, whether it be one or more closing parentheses
            index -= 1 #go to the left of that character in the text
            end_paren_count += 1 #to signify a closing parenthesis is at the end
        while (len(text) + index > -1): #so we don't search for more characters of the string than there are characters in the string
            if text[index] == '.':
                index -= 1
                continue #go back to while loop
            try:
                int(text[index]) #if this element is a digit
                index -= 1
            except: #if this element is not a digit or decimal point
                break
        to_keep = text[:index+1]
        # print('to_keep is : ', to_keep, end='. ')
        changed = '(-' + text[index+1:] + ')'
        # print('changed is : ', changed, end='. ')
        text = to_keep + changed
        display.set(text)

#define function for reciprocal (+/-)
def reciprocal():
    global text
    if (re.search('[(\d+)|(\.+)]\)+$', text) != None) or (re.search('[\d+|\.+]$', text) != None): #if text ends ($) optional opening parenthesis, combo of numbers and decimal places, then optional closing parenthesis
        index = -1 #to keep track of where in the string I'm checking
        end_paren_count = 0 # to keep track of how many closing parentheses there are at the end
        while text[index] == ')': #if it ends in a closing parenthesis, whether it be one or more closing parentheses
            index -= 1
            end_paren_count += 1 #to signify a closing parenthesis is at the end
        while (len(text) + index > -1): #so we don't search for more characters of the string than there are characters in the string
            if text[index] == '.':
                index -= 1
                continue #go back to while loop
            try:
                int(text[index]) #if this element is a digit
                index -= 1
            except: #if this element is not a digit or it is out of proper range to look there
                break
        if end_paren_count > 0:
            to_change = text[index + 1:(-1 * end_paren_count)]
        else:
            to_change = text[index + 1:]
            if to_change[-1] == ')': #cut off the last ending parenthesis if it is there
                to_change = to_change[:-1]
        to_keep = text[:index+1]
        # print('to keep', to_keep, end=' ')
        # print('what needs to be changed: ',to_change, ". ", end=' ')
        changed = 1 / float(to_change)
        if changed == int(changed): #if no decimal place is needed, like 20 / 2, where the int form loses no info compared to the float form
            changed = str(int(changed))
        else: #if the flaot is different than the, implying the decimal places matter and should be kept
            changed = str(changed)
        # print('it was changed to: ', changed)
        text = to_keep + changed
        if end_paren_count > 0:
            text += end_paren_count * ')'
    display.set(text)

display = tkinter.StringVar()

text_box = tkinter.Entry(gui, textvariable=display) #create a text box object containing that text
text_box.grid(row=1, # have it be on the top row
    columnspan = 6, #have it span all four columns that I will be creating. This brings it to the beginning of the 5th column, so spans all 4 working columns
    ipadx = 0, #make the text box itself thicker width-wise
    ipady = 20, #make the text box itself thicker height-wise
    pady = 30, #give it a margin on top of it and below it of 30 pixels
    sticky = 'nswe') #have it stretch the entire width (west and east) of its cell, which is effectively all columns of row 1
button_clear = tkinter.Button(gui, text = 'Clear', fg='black', bg='red', height=2, width=8, command = lambda: clear())
button_clear.grid(row=1, column=6, sticky = 'NSWE', padx = 4, pady = 30)

button_7 = tkinter.Button(gui, text=' 7 ', fg='black', bg='red', height=2, width=8, command= lambda: press(7))
button_7.grid(row=2, column=1, padx = 4, pady = 4, sticky = 'nswe')
button_8 = tkinter.Button(gui, text=' 8 ', fg='black', bg='red', height=2, width=8, command= lambda: press(8))
button_8.grid(row=2, column=2, padx = 4, pady = 4, sticky = 'nswe')
button_9 = tkinter.Button(gui, text=' 9 ', fg='black', bg='red', height=2, width=8, command= lambda: press(9))
button_9.grid(row=2, column=3, padx = 4, pady = 4, sticky = 'nswe')
button_plus = tkinter.Button(gui, text=' + ', fg='black', bg='red', height=2, width=8, command= lambda: press('+'))
button_plus.grid(row=2, column=4, padx = 4, pady = 4, sticky = 'nswe')
button_minus = tkinter.Button(gui, text=' - ', fg='black', bg='red', height=2, width=8, command= lambda: press('-'))
button_minus.grid(row=2, column=5, padx = 4, pady = 4, sticky = 'nswe')
button_leftparen = tkinter.Button(gui, text=' ( ', fg='black', bg='red', height=2, width=8, command= lambda: press('('))
button_leftparen.grid(row=2, column=6, padx = 4, pady = 4, sticky = 'nswe')


button_4 = tkinter.Button(gui, text=' 4 ', fg='black', bg='red', height=2, width=8, command= lambda: press(4))
button_4.grid(row=3, column=1, padx = 4, pady = 4, sticky = 'nswe')
button_5 = tkinter.Button(gui, text=' 5 ', fg='black', bg='red', height=2, width=8, command= lambda: press(5))
button_5.grid(row=3, column=2, padx = 4, pady = 4, sticky = 'nswe')
button_6 = tkinter.Button(gui, text=' 6 ', fg='black', bg='red', height=2, width=8, command= lambda: press(6))
button_6.grid(row=3, column=3, padx = 4, pady = 4, sticky = 'nswe')
button_times = tkinter.Button(gui, text=' X ', fg='black', bg='red', height=2, width=8, command= lambda: press('*'))
button_times.grid(row=3, column=4, padx = 4, pady = 4, sticky = 'nswe')
button_divide = tkinter.Button(gui, text=' ÷ ', fg='black', bg='red', height=2, width=8, command= lambda: press('/'))
button_divide.grid(row=3, column=5, padx = 4, pady = 4, sticky = 'nswe')
button_rightparen = tkinter.Button(gui, text=' ) ', fg='black', bg='red', height=2, width=8, command= lambda: press(')'))
button_rightparen.grid(row=3, column=6, padx = 4, pady = 4, sticky = 'nswe')

button_1 = tkinter.Button(gui, text=' 1 ', fg='black', bg='red', height=2, width=8, command= lambda: press(1))
button_1.grid(row=4, column=1, padx = 4, pady = 4, sticky = 'nswe')
button_2 = tkinter.Button(gui, text=' 2 ', fg='black', bg='red', height=2, width=8, command= lambda: press(2))
button_2.grid(row=4, column=2, padx = 4, pady = 4, sticky = 'nswe')
button_3 = tkinter.Button(gui, text=' 3 ', fg='black', bg='red', height=2, width=8, command= lambda: press(3))
button_3.grid(row=4, column=3, padx = 4, pady = 4, sticky = 'nswe')
button_exponent = tkinter.Button(gui, text=' ^ ', fg='black', bg='red', height=2, width=8, command= lambda: press('**'))
button_exponent.grid(row=4, column=4, padx = 4, pady = 4, sticky = 'nswe')
button_negate = tkinter.Button(gui, text=' +/- ', fg='black', bg='red', height=2, width=8, command= lambda: negate())
button_negate.grid(row=4, column=5, padx = 4, pady = 4, sticky = 'nswe')
button_backspace = tkinter.Button(gui, text=' <- ', fg='black', bg='red', height=2, width=8, command = lambda: backspace())
button_backspace.grid(row=4, column=6, padx = 4, pady = 4, sticky = 'nswe')


button_0 = tkinter.Button(gui, text=' 0 ', fg='black', bg='red', height=2, width=8, command= lambda: press(0))
button_0.grid(row=5, column=1, columnspan = 2, padx = 4, pady = 4, sticky = 'nswe')
button_dot = tkinter.Button(gui, text=' . ', fg='black', bg='red', height=2, width=8, command= lambda: press('.'))
button_dot.grid(row=5, column=3, padx = 4, pady = 4, sticky = 'nswe')
button_reciprocal = tkinter.Button(gui, text=' 1/X ', fg='black', bg='red', height=2, width=8, command = lambda: reciprocal())
button_reciprocal.grid(row=5, column=4, padx = 4, pady = 4, sticky = 'nswe')
button_equals = tkinter.Button(gui, text=' = ', fg='black', bg='red', height=2, width=8, command= lambda: equals())
button_equals.grid(row=5, column=5, columnspan = 2, padx = 4, pady = 4, sticky = 'nswe')

gui.mainloop() #run the gui window
