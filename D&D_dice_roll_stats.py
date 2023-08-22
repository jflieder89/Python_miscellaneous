import tkinter
from itertools import chain, product
import statistics
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageTk, Image
# from time import sleep

def calc():
    #Account for fields left blank or zeroes put in:
    if (dice_quantity.get() == '') or (dice_range.get() == '') or (dice_quantity.get() == '0') or (dice_range.get() == '0'):
        display.config(text="Please enter non-zero digits for both dice quantity and dice range")
        return
    #see if only digits were entered. This is redundant now that I have the digit validation working, but I'll keep it in for now:
    try:
        display.config(text='')
        int(dice_quantity.get())
        int(dice_range.get())
    except:
        display.config(text="Digits only please")
        return
    #get a list for possibilities of a single roll of the die:
    lst_base = list(range(1, int(dice_range.get()) + 1))
    #if only one die roll is called for, ex 1d8 or 1d6
    if int(dice_quantity.get()) == 1:
        lst_final = lst_base
        # display.config(text=lst_final)
        # print(lst_final)
    #I found an elegant way to get the result for 2 dice rolls specifically
    elif int(dice_quantity.get()) == 2:
        lst_final = [v for v, r in enumerate(chain(range(1, int(dice_range.get())), range(int(dice_range.get()), 0, -1)), 2) for _ in range(r)]
        # display.config(text=lst_final)
        # print(lst_final)
    #if the number of dice rolls is more than two:
    else:
        lst_final = [sum(tup) for tup in list(product(range(1, int(dice_range.get()) + 1), repeat = int(dice_quantity.get())))]
    #     # lst = lst_base #make a list that starts with the base, but will be modified through the iterations
    #     # for extra_iteration in range(1, int(dice_quantity.get())):
    #     #     print('\n', 'extra iteration number is:', extra_iteration)
    #     #     new_lst = [] #this will be what the possibilites will be for sums after this iteration
    #     #     for elem1 in lst:
    #     #         for elem2 in lst_base:
    #     #             print('previous total from dice rolls is', elem1,'and new roll to add is', elem2, 'and total now is', elem1+elem2)
    #     #             new_lst.append(elem1+elem2)
    #     #     lst = new_lst #sort of a checkpoint of possible sums after this latest iteration of roll amounts
    #     # lst_final = sorted(lst)
    #     # display.config(text=lst_final)
    #     lst_final = []
    #     # for number in range(int(dice_quantity.get()), int(dice_quantity.get()) * int(dice_range.get()) + 1):
    #     #     print(number)
    #     #     count = sum(1 for roll in product(range(1, int(dice_range.get())+1), repeat=int(dice_quantity.get())) if sum(roll)==number)
    #     #     for item in range(count):
    #     #         lst_final.append(number)
    #     # print(lst_final)
    #     temp_list = list(range(int(dice_quantity.get()), int(dice_quantity.get())*int(dice_range.get())+1))
    #     # print('initial temp_list:', temp_list, '\n')
    #     lst_final.extend(temp_list) #add the temp list to the result list once in the first temp_list form, so the lowest and highest possible sums are accounted for only once
    #     temp_list = temp_list[1:-1] #whittle away the temp_list from the edges
    #     while temp_list:
    #         # print('start of while. temp_list is ', temp_list, 'and lst_final is', lst_final, '\n')
    #         lst_final.extend(temp_list * (int(dice_quantity.get())-1))#need to do this one less time than there are dice rolled
    #         temp_list = temp_list[1:-1]#whittle away the temp_list from the edges
    #     # print('unsorted result is:', lst_final)
    # # print('got here')
    # print(lst_final)
    # for number in range(int(dice_quantity.get()), int(dice_quantity.get()) * int(dice_range.get()) + 1):
    #     print(str(number), 'occurs this many times:', lst_final.count(number))
    # return

    #Now set the statistics of the dice rolls:
    maximum_display.config( text = int(dice_quantity.get())*int(dice_range.get()) )
    minimum_display.config( text = int(dice_quantity.get()) )
    #Cut off decimal place if the decimal is only zero for mean and median:
    if ((int(dice_range.get()) + 1) * (int(dice_quantity.get())) * 0.5) == (int((int(dice_range.get()) + 1) * (int(dice_quantity.get())) * 0.5)):
        mean_display.config( text = int(((int(dice_range.get()) + 1) * int(dice_quantity.get()) * 0.5) ))
    else:
        mean_display.config( text = ((int(dice_range.get()) + 1) * int(dice_quantity.get()) * 0.5) )
    if statistics.median(lst_final) == int(statistics.median(lst_final)):
        median_display.config( text = int(statistics.median(lst_final)) )
    else:
        median_display.config( text = statistics.median(lst_final) )

    mode_display.config( text = statistics.mode(lst_final) )
    # print('lst_final is:', lst_final)
    # print(len(range(int(dice_quantity.get()), int(dice_quantity.get())*int(dice_range.get()))))

    #Now prepare the plotting of possible values:
    plt.clf() #clear the figure off of the plt if there already is one
    plt.hist(lst_final, bins = np.arange(int(dice_quantity.get()) - 0.5, int(dice_quantity.get())*int(dice_range.get()) + 1.5, 1), ec = 'black')
    plt.xlabel('Dice Sum')
    plt.ylabel('Occurrences of Dice Sums')
    title_str = 'Distribution of Possibilities for ' + dice_quantity.get() + 'd' + dice_range.get()
    plt.title(title_str)
    #set the xticks with 4 or less possible sums so not decimals are in the xticks, and over 25 stays as default to not have so many ticks that they overlap:
    if len(set(lst_final)) <= 25:
        plt.xticks(list(range(int(dice_quantity.get()), int(dice_quantity.get())*int(dice_range.get()) + 1, 1)))

    plt.savefig('Dice Histogram.png')
    # sleep(5)
    #now handle getting the image into the label within the frame:
    img = ImageTk.PhotoImage(Image.open("Dice Histogram.png").resize((image_frame.winfo_width(), image_frame.winfo_height())))
    image_label = tkinter.Label(image_frame, image = img)
    image_label.pack()
    image_label.place(relx = 0, rely = 0, relheight = 1, relwidth = 1)
    image_label.image = img #need this to occur after label is made for the image to show for some reason. so label must be made in this function when called instead of down below the function
    if int(dice_quantity.get()) > 1:
        success_text_str = "Showing results for " + dice_quantity.get() + ' ' + dice_range.get() + '-sided dice:'
    else:
        success_text_str = "Showing results for a"
        if (dice_range.get() in ['8', '18', '11', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89']):
            success_text_str += 'n'
        success_text_str += ' ' + dice_range.get() + '-sided die:'
    display.config(text=success_text_str)
    return
#A quit function for the quit button:
def quit_func():
    raise SystemExit
    gui.destroy()
#Here is function to help validate that entries into the entry widgets are digits only.:
def enter_only_digits(entry, action_type):
    if action_type == '1' and not entry.isdigit(): #if something is entered and it is not a digit
        return False
    return True

gui = tkinter.Tk() #create GUI object
gui.title("Dice Roll Stats") #name the GUI object
# gui.geometry("200x600") #set size of calculator GUI. This will be changed by the sticky and columnconfigure/row_configure commands
gui_width = 900
gui_height = 600
dice_quantity = tkinter.StringVar()
dice_range = tkinter.StringVar()
gui.geometry(str(gui_width) + 'x' + str(gui_height))
quit = tkinter.Button(gui, text=' Quit ', fg='black', bg='red', justify = 'center', command = lambda: quit_func())
quit.place(relx = 0, rely = 0.02, relheight = 0.2, relwidth = 0.2)

#here is the code to validate the characters entered into the entry boxes to only pass through digits and backspaces:
vcmd = (gui.register(enter_only_digits), '%P', '%d') #%P allows a good entry (digit) to be passed in, while %d allows for action to be differentiated (1 for entry, 0 for backspace/delete, -1 for other)

dice_quantity_label = tkinter.Label(gui, bg = 'white', bd = 3, relief = 'solid', text = "Number of dice:")
dice_quantity_label.place(relx = 0.24, rely = 0, relheight = 0.05, relwidth = 0.25)
dice_quantity_entry = tkinter.Entry(gui, textvariable=dice_quantity, validate = 'key', validatecommand=vcmd) #'key' causes the validation to occur upon being edited, and vcmd is a true/false filter for letting entries through or not
dice_quantity_entry.place(relx = 0.51, rely = 0, relheight = 0.05, relwidth = 0.25)
dice_range_label = tkinter.Label(gui, bg = 'white', bd = 3, relief = 'solid', text = "Dice range:")
dice_range_label.place(relx = 0.24, rely = 0.05, relheight = 0.05, relwidth = 0.25)
dice_range_entry = tkinter.Entry(gui, textvariable=dice_range, validate = 'key', validatecommand=vcmd)#'key' causes the validation to occur upon being edited, and vcmd is a true/false filter for letting entries through or not
dice_range_entry.place(relx = 0.51, rely = 0.05, relheight = 0.05, relwidth = 0.25)

calc_button = tkinter.Button(gui, text=' Calculate ', fg='black', bg='lightgreen', justify = 'center', relief = 'raised', command = lambda: calc())
calc_button.place(relx = 0.8, rely = 0.02, relheight = 0.2, relwidth = 0.2)
display = tkinter.Label(gui, bg = 'white', bd = 3, relief = 'solid', text = "Please note that calculating 6 or more dice may take awhile...", justify='center')
display.bind('<Configure>', lambda e: display.config(wraplength=display.winfo_width())) #this is to make the display wrap at the width of its window. Need to do it in separate line after this label is defined already.
display.place(relx = 0.24, rely = 0.1, relheight = 0.1, relwidth = 0.52)

maximum_label = tkinter.Label(gui, bg = 'white', bd = 3, relief = 'solid', text = "Maximum:")
maximum_label.place(relx = 0.80, rely = 0.35, relheight = 0.1, relwidth = 0.09)
maximum_display = tkinter.Label(gui, bg = 'white', bd = 3, relief = 'solid', text = "")
maximum_display.place(relx = 0.90, rely = 0.35, relheight = 0.1, relwidth = 0.09)
minimum_label = tkinter.Label(gui, bg = 'white', bd = 3, relief = 'solid', text = "Minimum:")
minimum_label.place(relx = 0.80, rely = 0.45, relheight = 0.1, relwidth = 0.09)
minimum_display = tkinter.Label(gui, bg = 'white', bd = 3, relief = 'solid', text = "")
minimum_display.place(relx = 0.90, rely = 0.45, relheight = 0.1, relwidth = 0.09)
mean_label = tkinter.Label(gui, bg = 'white', bd = 3, relief = 'solid', text = "Mean:")
mean_label.place(relx = 0.80, rely = 0.55, relheight = 0.1, relwidth = 0.09)
mean_display = tkinter.Label(gui, bg = 'white', bd = 3, relief = 'solid', text = "")
mean_display.place(relx = 0.90, rely = 0.55, relheight = 0.1, relwidth = 0.09)
median_label = tkinter.Label(gui, bg = 'white', bd = 3, relief = 'solid', text = "Median:")
median_label.place(relx = 0.80, rely = 0.65, relheight = 0.1, relwidth = 0.09)
median_display = tkinter.Label(gui, bg = 'white', bd = 3, relief = 'solid', text = "")
median_display.place(relx = 0.90, rely = 0.65, relheight = 0.1, relwidth = 0.09)
mode_label = tkinter.Label(gui, bg = 'white', bd = 3, relief = 'solid', text = "Mode:")
mode_label.place(relx = 0.80, rely = 0.75, relheight = 0.1, relwidth = 0.09)
mode_display = tkinter.Label(gui, bg = 'white', bd = 3, relief = 'solid', text = "")
mode_display.place(relx = 0.90, rely = 0.75, relheight = 0.1, relwidth = 0.09)

#set frame for where the image will go. The image label and image itself will be set in the calculating function
image_frame = tkinter.Frame(gui, highlightthickness=2, highlightbackground="black")
image_frame.pack()
image_frame.place(relx=0.05, rely=0.25, relwidth = 0.71, relheight = 0.7)
# image_label = tkinter.Label(image_frame, image = None) #refresh this so an older image doesn't stick around underneath a new one
# image_label.pack() #refresh this so an older image doesn't stick around underneath a new one
# image_label.place(relx = 0, rely = 0, relheight = 1, relwidth = 1) #refresh this so an older image doesn't stick around underneath a new one

if __name__ == "__main__":
    gui.mainloop()
