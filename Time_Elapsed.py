import tkinter
from tkinter import ttk
from datetime import datetime, timedelta, date

#Here is a little function to check if a year is a leap year or not, which I will be using later on to sort if an input of a day is valid:
def is_leap_year(year):
    year = int(year)
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False
#create functions to clear all of some of the top half and the bottom half back to default values
def clear_all_top_func():
    global year_str_top_start, year_str_top_end, month_str_top_start, month_str_top_end, day_str_top_start, day_str_top_end,\
    hour_str_top_start, hour_str_top_end, minute_str_top_start, minute_str_top_end, AM_PM_top_start, AM_PM_top_end
    year_str_top_start.set('Select a year')
    year_str_top_end.set('Select a year')
    month_str_top_start.set('Select a month')
    month_str_top_end.set('Select a month')
    day_str_top_start.set('Select a day')
    day_str_top_end.set('Select a day')
    hour_str_top_start.set('Select an hour')
    hour_str_top_end.set('Select an hour')
    minute_str_top_start.set('Select a minute')
    minute_str_top_end.set('Select a minute')
    AM_PM_top_start.set('None') #make sure its a string; I'm not sure how/if tkinter handles Nonetype variables
    AM_PM_top_end.set('None') #make sure its a string; I'm not sure how/if tkinter handles Nonetype variables
    result_top.config(text ='', bg = 'yellow', fg = 'black')
def clear_start_top_func(): #just to clear the top starting time row
    global year_str_top_start, month_str_top_start, day_str_top_start,\
    hour_str_top_start, minute_str_top_start, AM_PM_top_start
    year_str_top_start.set('Select a year')
    month_str_top_start.set('Select a month')
    day_str_top_start.set('Select a day')
    hour_str_top_start.set('Select an hour')
    minute_str_top_start.set('Select a minute')
    AM_PM_top_start.set('None') #make sure its a string; I'm not sure how/if tkinter handles Nonetype variables
def clear_end_top_func(): #just to clear the second ending time row
    global year_str_top_end, month_str_top_end, day_str_top_end,\
    hour_str_top_end, minute_str_top_end, AM_PM_top_end
    year_str_top_end.set('Select a year')
    month_str_top_end.set('Select a month')
    day_str_top_end.set('Select a day')
    hour_str_top_end.set('Select an hour')
    minute_str_top_end.set('Select a minute')
    AM_PM_top_end.set('None') #make sure its a string; I'm not sure how/if tkinter handles Nonetype variables
def clear_result_top_func():
    result_top.config(text ='', bg = 'yellow', fg = 'black')
def clear_all_bottom_func():
    global year_str_bottom, month_str_bottom, day_str_bottom, hour_str_bottom, minute_str_bottom, \
    AM_PM_bottom, weeks_to_add, days_to_add, hours_to_add
    year_str_bottom.set('Select a year')
    month_str_bottom.set('Select a month')
    day_str_bottom.set('Select a day')
    hour_str_bottom.set('Select an hour')
    minute_str_bottom.set('Select a minute')
    AM_PM_bottom.set('None') #make sure its a string; I'm not sure how/if tkinter handles Nonetype variables for a value of None
    weeks_to_add.set('')
    days_to_add.set('')
    hours_to_add.set('')
    minutes_to_add.set('')
    result_bottom.config(text = '', bg = 'yellow', fg = 'black')
def clear_start_bottom_func(): #just to clear the top starting time row
    global year_str_bottom, month_str_bottom, day_str_bottom,\
    hour_str_bottom, minute_str_bottom, AM_PM_bottom
    year_str_bottom.set('Select a year')
    month_str_bottom.set('Select a month')
    day_str_bottom.set('Select a day')
    hour_str_bottom.set('Select an hour')
    minute_str_bottom.set('Select a minute')
    AM_PM_bottom.set('None') #make sure its a string; I'm not sure how/if tkinter handles Nonetype variables
def clear_add_bottom_func(): #just to clear the second ending time row
    global weeks_to_add, days_to_add, hours_to_add, minutes_to_add
    weeks_to_add.set('')
    days_to_add.set('')
    hours_to_add.set('')
    minutes_to_add.set('')
def clear_result_bottom_func():
    result_bottom.config(text ='', bg = 'yellow', fg = 'black')
#now, the engine of this code: make calculate functions for the top and bottom capabilities
def calc_top_func():
    global year_str_top_start, year_str_top_end, month_str_top_start, month_str_top_end, day_str_top_start, day_str_top_end,\
    hour_str_top_start, hour_str_top_end, minute_str_top_start, minute_str_top_end, AM_PM_top_start, AM_PM_top_end
    #first deal with scenario that number fields (year, day, hour, minute) are not all selected
    try:
        year_str_top_start.set(int(year_str_top_start.get()))
        year_str_top_end.set(int(year_str_top_end.get()))
        day_str_top_start.set(int(day_str_top_start.get()))
        day_str_top_end.set(int(day_str_top_end.get()))
        hour_str_top_start.set(int(hour_str_top_start.get()))
        hour_str_top_end.set(int(hour_str_top_end.get()))
        minute_str_top_start.set(int(minute_str_top_start.get()))
        minute_str_top_end.set(int(minute_str_top_end.get()))
    except:
        result_top.config(text = 'Please be sure to select all required variables', bg = 'red', fg = 'black')
        return #don't go any further into the function in this case
    #now deal with non-number fields (month, am_pm) that are not all selected
    if (month_str_top_start.get() == 'Select a month') or (month_str_top_end.get() == 'Select a month') or \
    (AM_PM_top_start.get() == 'None') or (AM_PM_top_end.get() == 'None'):
        result_top.config(text = 'Please be sure to select all required variables', bg = 'red', fg = 'black')
        return #don't go any further into the function in this case
    #Need to account for instances where an invalid day value it chosen for a particular month and year:
    first_line = second_line = False #set lines of text for start and end times (to be used if Feb day chosen is wrong) to be False until found out to be otherwise
    #check the start date/time first:
    if (month_str_top_start.get() == 'February') and (is_leap_year(int(year_str_top_start.get())) == True) and (int(day_str_top_start.get()) > 29):
        # x = 'The day value for the start is too high;' #+ '\n' +  'February only has 29 days that year'
        # result_top.config(text = 'The day value for the start is too high; February only has 29 days that year')
        # print('got here')
        first_line = 'The day value for the start is too high. February of that year has only 29 days.'
    elif (month_str_top_start.get() == 'February') and (is_leap_year(int(year_str_top_start.get())) == False) and (int(day_str_top_start.get()) > 28):
        first_line = 'The day value for the start is too high. February of that year has only 28 days.'
    elif (month_str_top_start.get() in months_with_30_days) and (int(day_str_top_start.get()) > 30):
        first_line = 'The day value for the start is too high. That month only has 30 days.'
    #now check the ending date/time:
    if (month_str_top_end.get() == 'February') and (is_leap_year(int(year_str_top_end.get())) == True) and (int(day_str_top_end.get()) > 29):
        second_line = 'The day value for the end is too high. February of that year has only 29 days.'
    elif (month_str_top_end.get() == 'February') and (is_leap_year(int(year_str_top_end.get())) == False) and (int(day_str_top_end.get()) > 28):
        second_line = 'The day value for the end is too high. February of that year has only 28 days.'
    elif (month_str_top_end.get() in months_with_30_days) and (int(day_str_top_end.get()) > 30):
        second_line = 'The day value for the end is too high. That month only has 30 days.'
    #Now if either the start or the end flagged for an invalid day, then print it out and exit the function
    while (first_line != False) or (second_line != False):
        if first_line == False:
            result_top.config(text = second_line, bg = 'red', fg = 'black')
            return
        elif second_line == False:
            result_top.config(text = first_line, bg = 'red', fg = 'black')
            return
        else:
            result_top.config(text = first_line + '\n' + second_line, bg = 'red', fg = 'black')
            return
    #Now set date_time objects for start time and end time:
    start_datetime_top = datetime(int(year_str_top_start.get()), int(month_conversion[month_str_top_start.get()]), int(day_str_top_start.get()), \
    int(hour_str_top_start.get()), int(minute_str_top_start.get()), 0)
    end_datetime_top = datetime(int(year_str_top_end.get()), int(month_conversion[month_str_top_end.get()]), int(day_str_top_end.get()), \
    int(hour_str_top_end.get()), int(minute_str_top_end.get()), 0)
    #Need to account for changes due toh AM/PM affects on hours including the need to convert to military time for datetime objects:
    if (AM_PM_top_start.get() == 'AM') and (hour_str_top_start.get() == '12'): #if the hour is midnight
        start_datetime_top -= timedelta(hours = 12) #turn the midnight 12 into 0
    elif (AM_PM_top_start.get() == 'PM') and (hour_str_top_start.get() != '12'): #if the hour is between 1pm and 11 pm
        start_datetime_top += timedelta(hours = 12) #add 12 to all PM times except noon
    if (AM_PM_top_end.get() == 'AM') and (hour_str_top_end.get() == '12'): #if the hour is midnight
        end_datetime_top -= timedelta(hours = 12) #turn the midnight 12 into 0
    elif (AM_PM_top_end.get() == 'PM') and (hour_str_top_end.get() != '12'): #if the hour is between 1pm and 11 pm
        end_datetime_top += timedelta(hours = 12) #add 12 to all PM times except noon
    # print('Start time: ' + str(start_datetime_top) + '. ' + 'End time: ' + str(end_datetime_top) + '.')
    diff = end_datetime_top - start_datetime_top #get the difference from start time to end time
    # print('difference is: ', diff)
    #Now recall that this diff object only has days and seconds (and milliseconds) to work with so weeks, hours, and minutes will need to be crafted
    diff_weeks = diff_hours = diff_minutes = 0
    diff_days = diff.days #define these now in case one of them is zero and to avoid funny business with the following week,hour,minute creations
    diff_seconds = diff.seconds
    #Account for is start time and end time are exactly the same:
    if (diff_seconds == 0) and (diff_days == 0):
        result_top.config(text = 'No time has elapsed. The start and end time are the same.', bg = 'red', fg = 'black')
        return
    #Account for the user putting in an end time that is prior to the start time:
    if (start_datetime_top > end_datetime_top):
        result_top.config(text = 'Your start time is currently later than your end time.' + '\n' + 'Please change the time for the start to be before the end.', bg = 'red', fg = 'black')
        return
    #Now with non-zero difference, get weeks, days, hours, and minutes sorted out:
    if diff_days > 6: #if 7 days or more have passed
        diff_weeks = diff_days // 7 #get the number of full weeks
        diff_days = diff_days - (diff_weeks * 7) #get a new count of days remaining that doesn't include those full weeks
    if diff_seconds >= 3599: #if more than an hour has passed
        diff_hours = diff_seconds // 3600 #get the number of full hours
        diff_seconds = diff_seconds - (diff_hours * 3600) #get a new count of seconds that doesn't include the full hours
    if diff_seconds > 59: #if more than a full minute
        diff_minutes = diff_seconds // 60
        #diff_seconds = diff_seconds - (diff_minutes * 60) #don't need this line since I'm not measuring time down to the second in this program
    # print('weeks: ', diff_weeks, '. days: ', diff_days, '. hours: ', diff_hours, '. minutes: ', diff_minutes)
    #create a dictionary to cycle through so I can check and only print out non-zero values. No need for seconds since that will be zero since I only measured the start time to the minute.
    diff_dict = {0: ['week', diff_weeks], 1: ['day', diff_days], 2: ['hour', diff_hours], 3: ['minute', diff_minutes]}
    non_zero_terms_remaining = 0 #start a count of how many categories of time have a non-zero amount
    for digit in range (0,4):
        if diff_dict[digit][1] != 0: #if that term in the dictionary is non-zero
            non_zero_terms_remaining += 1
    # print(non_zero_terms_remaining)
    #now create a full statement showing weeks/days/hours/minutes difference with applicable (non-zero) terms
    statement_top = 'The time elapsed from start to end is' #start ending print statement for actual time elapsed if not zero
    for digit in range (0,4):
        if diff_dict[digit][1] != 0: #only do the following if the value is not zero
            statement_top = statement_top + ' ' + str(diff_dict[digit][1]) + ' ' + diff_dict[digit][0]
            if (diff_dict[digit][1] > 1) or (diff_dict[digit][1] < 0): #to account for multiple in positive or negative amounts
                statement_top += 's'
            non_zero_terms_remaining -= 1
            if non_zero_terms_remaining == 0: #if this was the last term
                statement_top += '.'
            elif non_zero_terms_remaining == 1: #if this was just the second to last term
                statement_top += ', and'
            else:
                statement_top += ','
    #Now show the time difference in just hours and minutes if it there are weeks and/or days in the difference
    statement_bottom = '' #set this as empty string first. This will change if needed below
    if (diff_weeks != 0) or (diff_days != 0):
        statement_bottom = 'In just hours and minutes, this is'
        diff_hours_new = diff_hours + (diff_weeks * 24 * 7) + (diff_days * 24) #take the weeks and days and turn them into hours
        diff_dict_new = {0: ['hour', diff_hours_new], 1: ['minute', diff_minutes]} #make new dictionary
        non_zero_terms_remaining_new = 0 #start a count of how many categories of time have a non-zero amount
        for digit in range (0,2):
            if diff_dict_new[digit][1] != 0: #if that term in the dictionary is non-zero
                non_zero_terms_remaining_new += 1
        for digit in range (0,2):
            if diff_dict_new[digit][1] != 0: #only do the following if the value is not zero
                statement_bottom = statement_bottom + ' ' + str(diff_dict_new[digit][1]) + ' ' + diff_dict_new[digit][0]
                if (diff_dict_new[digit][1] > 1) or ((diff_dict_new[digit][1] < 0)): #to account for multiple in positive or negative amounts
                    statement_bottom += 's'
                non_zero_terms_remaining_new -= 1
                if non_zero_terms_remaining_new == 0: #if this was the last term
                    statement_bottom += '.'
                elif non_zero_terms_remaining_new == 1: #if this was just the second to last term. No comma needed since there are two terms maximum.
                    statement_bottom += ' and'
    if (statement_bottom == ''):
        result_top.config(text = statement_top, bg = 'green', fg = 'white')
        return
    else:
        result_top.config(text = statement_top + '\n' + statement_bottom, bg = 'green', fg = 'white')
        return

def calc_bottom_func():
    global year_str_bottom, month_str_bottom, day_str_bottom, hour_str_bottom, minute_str_bottom,\
    AM_PM_bottom, weeks_to_add, days_to_add, hours_to_add, minutes_to_add
    #first deal with scenario that number fields (year, day, hour, minute) are not all selected
    first_line = second_line = False
    try:
        year_str_bottom.set(int(year_str_bottom.get()))
        day_str_bottom.set(int(day_str_bottom.get()))
        hour_str_bottom.set(int(hour_str_bottom.get()))
        minute_str_bottom.set(int(minute_str_bottom.get()))
    except:
        first_line = 'Please be sure to select all required variables'
    if (month_str_bottom.get() == 'Select a month') or (AM_PM_bottom.get() == 'None'):
        first_line = 'Please be sure to select all required variables'
    #check the inputs of the start time for validity
    if (month_str_bottom.get() == 'February') and (is_leap_year(int(year_str_bottom.get())) == True) and (int(day_str_bottom.get()) > 29):
        first_line = 'The day value for the start is too high. February of that year has only 29 days.'
    elif (month_str_bottom.get() == 'February') and (is_leap_year(int(year_str_bottom.get())) == False) and (int(day_str_bottom.get()) > 28):
        first_line = 'The day value for the start is too high. February of that year has only 28 days.'
    elif (month_str_bottom.get() in months_with_30_days) and (int(day_str_bottom.get()) > 30):
        first_line = 'The day value for the start is too high. That month only has 30 days.'
    #check the inputs of the time to add for validity
    if (weeks_to_add.get() == '') and (days_to_add.get() == '') and (hours_to_add.get() == '') and (minutes_to_add.get() == ''): #if nothing has been inputted for time to add
        second_line = 'You haven\'t entered any time to add.'
    else: #Now account for non-digit entries
        for item in [weeks_to_add, days_to_add, hours_to_add, minutes_to_add]:
            if item.get() != '':
                try:
                    int(item.get())
                except:
                    second_line = 'Please make sure the amounts of time to add are digits only.'
    #Now if either the start or the end flagged for an invalid day, then print it out and exit the function
    while (first_line != False) or (second_line != False):
        if first_line == False:
            result_bottom.config(text = second_line, bg = 'red', fg = 'black')
            return
        elif second_line == False:
            result_bottom.config(text = first_line, bg = 'red', fg = 'black')
            return
        else:
            result_bottom.config(text = first_line + '\n' + second_line, bg = 'red', fg = 'black')
            return
    #Now handle good input scenarios. Create objects for start time and time to add, then add to get new time
    #Need to account for changes due toh AM/PM affects on hours including the need to convert to military time for datetime objects:
    start_datetime_bottom = datetime(int(year_str_bottom.get()), int(month_conversion[month_str_bottom.get()]), \
    int(day_str_bottom.get()), int(hour_str_bottom.get()), int(minute_str_bottom.get()), 0)
    # result_bottom.config(text = str(start_datetime_bottom))
    if (AM_PM_bottom.get() == 'AM') and (hour_str_bottom.get() == '12'): #if the hour is midnight
        start_datetime_bottom -= timedelta(hours = 12) #turn the midnight 12 into 0
    elif (AM_PM_bottom.get() == 'PM') and (hour_str_bottom.get() != '12'): #if the hour is between 1pm and 11 pm
        start_datetime_bottom += timedelta(hours = 12) #add 12 to all PM times except noon
    #Need to handle the total add time in cases that not all fields are filled in
    total_days_to_add = total_seconds_to_add = False
    if (weeks_to_add.get() == '') and (days_to_add.get() != ''):#if days are put in but not weeks
        total_days_to_add = timedelta(days = int(days_to_add.get()))
    elif (days_to_add.get() == '') and (weeks_to_add.get() != ''): #if weeks are put in but not days
         total_days_to_add = timedelta(days = (int(weeks_to_add.get()) * 7))
    elif (weeks_to_add.get() != '') and (days_to_add.get() != ''): #if both days and weeks are entered
        total_days_to_add = timedelta(days = ((int(weeks_to_add.get()) * 7) + int(days_to_add.get())))
    # print('weeks: ', weeks_to_add.get())
    # print('days: ', days_to_add.get())
    # print('total days: ', total_days_to_add)
    if (hours_to_add.get() == '') and (minutes_to_add.get() != ''): #if minutes are put in but not hours
        total_seconds_to_add = timedelta(seconds = int(minutes_to_add.get()) * 60)
    elif (hours_to_add.get() != '') and (minutes_to_add.get() == ''): #if hours are put in but not minutes
        total_seconds_to_add = timedelta(seconds = (int(hours_to_add.get()) * 3600))
    elif (hours_to_add.get() != '') and (minutes_to_add.get() != ''): #if both minutes and hours are entered
        total_seconds_to_add = timedelta(seconds = (int(hours_to_add.get()) * 3600) + ( int(minutes_to_add.get()) * 60) )
    # print('hours: ', hours_to_add.get())
    # print('minutes: ', minutes_to_add.get())
    # print('total seconds: ', total_seconds_to_add)
    if total_days_to_add == False:
        time_to_add = total_seconds_to_add
    elif total_seconds_to_add == False:
        time_to_add = total_days_to_add
    else:
        time_to_add = total_days_to_add + total_seconds_to_add
    # print('time to add is: ', time_to_add)

    # time_to_add = timedelta(days = ((int(weeks_to_add.get()) * 7) + int(days_to_add.get())), seconds = ((int(hours_to_add.get()) * 3600) + (int(minutes_to_add.get()) * 60)))
    # print(time_to_add)
    new_datetime = start_datetime_bottom + time_to_add
    new_year = new_datetime.strftime('%Y')
    new_month = new_datetime.strftime('%B')
    #apparently the verbiage to get the zeroes removed from single digits day numbers, '%-d', no longer works
    new_day = new_datetime.strftime('%d')
    # print(new_day)
    if new_day[0] == '0':
        new_day = new_day[1:]
    # print(new_day)
    new_weekday = new_datetime.strftime('%A')
    new_hour = new_datetime.strftime('%I')
    new_minute = new_datetime.strftime('%M')
    new_AM_PM= new_datetime.strftime('%p')
    # print(new_year)
    # print(new_month)
    # print(new_day)
    # print(new_hour)
    # print(new_minute)
    # print(new_weekday)
    # print(new_AM_PM)
    # print(type(new_hour))
    new_time = new_datetime.strftime('%I') + ':' + new_datetime.strftime('%M') + ' ' + new_datetime.strftime('%p')
    # print(new_time)
    #now add in the proper suffix for the day (st, nd, rd, th)
    if (new_day == '1') or (new_day == '21') or (new_day == '31'):
        new_day_suffix = 'st'
    elif (new_day == '2') or (new_day == '22'):
        new_day_suffix = 'nd'
    elif (new_day == '3') or (new_day == '23'):
        new_day_suffix = 'rd'
    else:
        new_day_suffix = 'th'
    result_bottom.config(text = 'With the given start time and time to add, the end date/time will be:' + '\n' + \
    new_weekday + ' ' + new_month + ' ' + new_day + new_day_suffix + ', ' + new_year + ' at ' + new_time + '.', bg = 'green', fg = 'white')

#Set the gui window basics:
gui = tkinter.Tk()
gui.title("Time Elapsed Calculator") #name the GUI object
# gui.geometry("200x600") #set size of calculator GUI.
gui_width = 1400
gui_height = 750
gui.geometry(str(gui_width) + 'x' + str(gui_height))
gui.resizable(False, False) #make it so the window cannot be resized

#Set some variables that will be needed for button options and operations:
day_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
 '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
  '25', '26', '27', '28', '29', '30', '31']
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
'August', 'September', 'October', 'November', 'December']
month_conversion = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7,
'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
months_with_30_days = ['April', 'June', 'September', 'November'] #list of month numbers with 30 days
year_list = list(range(date.today().year, 1899, -1))
hour_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
minute_list = list(range(0, 60))
#The real ones for the actual program:
year_str_top_start = tkinter.StringVar()
year_str_top_start.set('Select a year')
year_str_top_end = tkinter.StringVar()
year_str_top_end.set('Select a year')
year_str_bottom = tkinter.StringVar()
year_str_bottom.set('Select a year')
month_str_top_start = tkinter.StringVar()
month_str_top_start.set('Select a month')
month_str_top_end = tkinter.StringVar()
month_str_top_end.set('Select a month')
month_str_bottom = tkinter.StringVar()
month_str_bottom.set('Select a month')
day_str_top_start = tkinter.StringVar()
day_str_top_start.set('Select a day')
day_str_top_end = tkinter.StringVar()
day_str_top_end.set('Select a day')
day_str_bottom = tkinter.StringVar()
day_str_bottom.set('Select a day')
hour_str_top_start = tkinter.StringVar()
hour_str_top_start.set('Select an hour')
hour_str_top_end = tkinter.StringVar()
hour_str_top_end.set('Select an hour')
hour_str_bottom = tkinter.StringVar()
hour_str_bottom.set('Select an hour')
minute_str_top_start = tkinter.StringVar()
minute_str_top_start.set('Select a minute')
minute_str_top_end = tkinter.StringVar()
minute_str_top_end.set('Select a minute')
minute_str_bottom = tkinter.StringVar()
minute_str_bottom.set('Select a minute')
AM_PM_top_start = tkinter.StringVar()
AM_PM_top_start.set(None) #set the starting default to be neither
AM_PM_top_end = tkinter.StringVar()
AM_PM_top_end.set(None)#set the starting default to be neither
AM_PM_bottom = tkinter.StringVar()
AM_PM_bottom.set(None)#set the starting default to be neither
weeks_to_add = tkinter.StringVar()
weeks_to_add.set('')
days_to_add = tkinter.StringVar()
days_to_add.set('')
hours_to_add = tkinter.StringVar()
hours_to_add.set('')
minutes_to_add = tkinter.StringVar()
minutes_to_add.set('')
#for testing:
# year_str_top_start = tkinter.StringVar()
# year_str_top_start.set('2000')
# year_str_top_end = tkinter.StringVar()
# year_str_top_end.set('2004')
# year_str_bottom = tkinter.StringVar()
# year_str_bottom.set('2022')
# month_str_top_start = tkinter.StringVar()
# month_str_top_start.set('January')
# month_str_top_end = tkinter.StringVar()
# month_str_top_end.set('January')
# month_str_bottom = tkinter.StringVar()
# month_str_bottom.set('March')
# day_str_top_start = tkinter.StringVar()
# day_str_top_start.set('30')
# day_str_top_end = tkinter.StringVar()
# day_str_top_end.set('30')
# day_str_bottom = tkinter.StringVar()
# day_str_bottom.set('1')
# hour_str_top_start = tkinter.StringVar()
# hour_str_top_start.set('5')
# hour_str_top_end = tkinter.StringVar()
# hour_str_top_end.set('7')
# hour_str_bottom = tkinter.StringVar()
# hour_str_bottom.set('11')
# minute_str_top_start = tkinter.StringVar()
# minute_str_top_start.set('5')
# minute_str_top_end = tkinter.StringVar()
# minute_str_top_end.set('26')
# minute_str_bottom = tkinter.StringVar()
# minute_str_bottom.set('46')
# AM_PM_top_start = tkinter.StringVar()
# AM_PM_top_start.set('AM') #set the starting default to be neither
# AM_PM_top_end = tkinter.StringVar()
# AM_PM_top_end.set('PM')#set the starting default to be neither
# AM_PM_bottom = tkinter.StringVar()
# AM_PM_bottom.set('AM')#set the starting default to be neither
# weeks_to_add = tkinter.StringVar()
# weeks_to_add.set('3')
# days_to_add = tkinter.StringVar()
# days_to_add.set('2')
# hours_to_add = tkinter.StringVar()
# hours_to_add.set('4')
# minutes_to_add = tkinter.StringVar()
# minutes_to_add.set('7')

#Now set some labels for the two capabilities that this program will have, with a separator to separate them:
top_frame = tkinter.Frame(gui, highlightthickness=4, highlightbackground="black")
top_frame.place(relx=0, rely=0, relheight=0.5, relwidth=1)
top_canvas = tkinter.Canvas(top_frame, width = 1400, height = 375)
top_canvas.create_line(30, 183, 1362, 183, dash = (5, 1))
top_canvas.create_line(30, 265, 1362, 265, dash = (5, 1))
top_canvas.pack()
label_top = tkinter.Label(top_frame, bg = 'white', bd = 3, relief = 'solid', text = "Obtain time difference between two times/dates", font = 25)
label_top.place(relx=0.3, rely=0.04, relheight=0.2, relwidth=0.4)
#Make labels for the rows of data that will be needed:
label_start_year_top = tkinter.Label(top_frame, bg = 'white', bd = 3, relief = 'solid', text = "Start date and time:")
label_start_year_top.place(relx=0.02, rely=0.32, relheight=0.16, relwidth=0.13)

#Now create and set buttons for the first row, the start time/date for the top capability:
year_start_top_frame = tkinter.Frame(top_frame, highlightthickness=2, highlightbackground="black")
year_start_top_frame.place(relx = 0.16, rely = 0.32, relheight = 0.16, relwidth = 0.12)
year_start_top = tkinter.OptionMenu(year_start_top_frame, year_str_top_start, *year_list)
year_start_top.place(relx = 0, rely = 0, relheight = 0.7, relwidth = 1)
year_start_top_label = tkinter.Label(year_start_top_frame, bg = 'white', text = "Starting Year")
year_start_top_label.place(relx = 0, rely = 0.7, relheight = 0.3, relwidth = 1)

month_start_top_frame = tkinter.Frame(top_frame, highlightthickness=2, highlightbackground="black")
month_start_top_frame.place(relx = 0.29, rely = 0.32, relheight = 0.16, relwidth = 0.12)
month_start_top = tkinter.OptionMenu(month_start_top_frame, month_str_top_start, *month_list)
month_start_top.place(relx = 0, rely = 0, relheight = 0.7, relwidth = 1)
month_start_top_label = tkinter.Label(month_start_top_frame, bg = 'white', text = "Starting Month")
month_start_top_label.place(relx = 0, rely = 0.7, relheight = 0.3, relwidth = 1)

day_start_top_frame = tkinter.Frame(top_frame, highlightthickness=2, highlightbackground="black")
day_start_top_frame.place(relx = 0.42, rely = 0.32, relheight = 0.16, relwidth = 0.12)
day_start_top = tkinter.OptionMenu(day_start_top_frame, day_str_top_start, *day_list)
day_start_top.place(relx = 0, rely = 0, relheight = 0.7, relwidth = 1)
month_start_top_label = tkinter.Label(day_start_top_frame, bg = 'white', text = "Starting Day")
month_start_top_label.place(relx = 0, rely = 0.7, relheight = 0.3, relwidth = 1)

hour_start_top_frame = tkinter.Frame(top_frame, highlightthickness=2, highlightbackground="black")
hour_start_top_frame.place(relx = 0.55, rely = 0.32, relheight = 0.16, relwidth = 0.12)
hour_start_top = tkinter.OptionMenu(hour_start_top_frame, hour_str_top_start, *hour_list)
hour_start_top.place(relx = 0, rely = 0, relheight = 0.7, relwidth = 1)
hour_start_top_label = tkinter.Label(hour_start_top_frame, bg = 'white', text = "Starting Hour")
hour_start_top_label.place(relx = 0, rely = 0.7, relheight = 0.3, relwidth = 1)

minute_start_top_frame = tkinter.Frame(top_frame, highlightthickness=2, highlightbackground="black")
minute_start_top_frame.place(relx = 0.68, rely = 0.32, relheight = 0.16, relwidth = 0.12)
minute_start_top = tkinter.OptionMenu(minute_start_top_frame, minute_str_top_start, *minute_list)
minute_start_top.place(relx = 0, rely = 0, relheight = 0.7, relwidth = 1)
minute_start_top_label = tkinter.Label(minute_start_top_frame, bg = 'white', text = "Starting Minute")
minute_start_top_label.place(relx = 0, rely = 0.7, relheight = 0.3, relwidth = 1)

am_pm_top_start_frame = tkinter.Frame(top_frame, highlightthickness=2, highlightbackground="black")
am_pm_top_start_frame.place(relx = 0.81, rely = 0.32, relheight = 0.16, relwidth = 0.10)
am_radio_top_start = tkinter.Radiobutton(am_pm_top_start_frame, text = "AM", variable = AM_PM_top_start, value = 'AM')
am_radio_top_start.place(relx = 0, rely = 0, relheight = 0.35, relwidth = 1)
pm_radio_top_start = tkinter.Radiobutton(am_pm_top_start_frame, text = "PM", variable = AM_PM_top_start, value = 'PM')
pm_radio_top_start.place(relx = 0, rely = 0.35, relheight = 0.35, relwidth = 1)
am_pm_top_start_label = tkinter.Label(am_pm_top_start_frame, bg = 'white', text = 'Starting AM/PM')
am_pm_top_start_label.place(relx = 0, rely = 0.7, relheight = 0.3, relwidth = 1)

clear_start_top = tkinter.Button(top_frame, text=' Clear start ', fg='black', bg='red', justify = 'center', command = lambda: clear_start_top_func())
clear_start_top.place(relx = 0.92, rely = 0.32, relheight = 0.16, relwidth = 0.06)

#Now create and set buttons for the first row, the end time/date for the top capability:
label_end_year_top = tkinter.Label(top_frame, bg = 'white', bd = 3, relief = 'solid', text = "End date and time:")
label_end_year_top.place(relx=0.02, rely=0.52, relheight=0.16, relwidth=0.13)

#Now create and set buttons for the first row, the end time/date for the top capability:
year_end_top_frame = tkinter.Frame(top_frame, highlightthickness=2, highlightbackground="black")
year_end_top_frame.place(relx = 0.16, rely = 0.52, relheight = 0.16, relwidth = 0.12)
year_end_top = tkinter.OptionMenu(year_end_top_frame, year_str_top_end, *year_list)
year_end_top.place(relx = 0, rely = 0, relheight = 0.7, relwidth = 1)
year_end_top_label = tkinter.Label(year_end_top_frame, bg = 'white', text = "Ending Year")
year_end_top_label.place(relx = 0, rely = 0.7, relheight = 0.3, relwidth = 1)

month_end_top_frame = tkinter.Frame(top_frame, highlightthickness=2, highlightbackground="black")
month_end_top_frame.place(relx = 0.29, rely = 0.52, relheight = 0.16, relwidth = 0.12)
month_end_top = tkinter.OptionMenu(month_end_top_frame, month_str_top_end, *month_list)
month_end_top.place(relx = 0, rely = 0, relheight = 0.7, relwidth = 1)
month_end_top_label = tkinter.Label(month_end_top_frame, bg = 'white', text = "Ending Month")
month_end_top_label.place(relx = 0, rely = 0.7, relheight = 0.3, relwidth = 1)

day_end_top_frame = tkinter.Frame(top_frame, highlightthickness=2, highlightbackground="black")
day_end_top_frame.place(relx = 0.42, rely = 0.52, relheight = 0.16, relwidth = 0.12)
day_end_top = tkinter.OptionMenu(day_end_top_frame, day_str_top_end, *day_list)
day_end_top.place(relx = 0, rely = 0, relheight = 0.7, relwidth = 1)
month_end_top_label = tkinter.Label(day_end_top_frame, bg = 'white', text = "Ending Day")
month_end_top_label.place(relx = 0, rely = 0.7, relheight = 0.3, relwidth = 1)

hour_end_top_frame = tkinter.Frame(top_frame, highlightthickness=2, highlightbackground="black")
hour_end_top_frame.place(relx = 0.55, rely = 0.52, relheight = 0.16, relwidth = 0.12)
hour_end_top = tkinter.OptionMenu(hour_end_top_frame, hour_str_top_end, *hour_list)
hour_end_top.place(relx = 0, rely = 0, relheight = 0.7, relwidth = 1)
hour_end_top_label = tkinter.Label(hour_end_top_frame, bg = 'white', text = "Ending Hour")
hour_end_top_label.place(relx = 0, rely = 0.7, relheight = 0.3, relwidth = 1)

minute_end_top_frame = tkinter.Frame(top_frame, highlightthickness=2, highlightbackground="black")
minute_end_top_frame.place(relx = 0.68, rely = 0.52, relheight = 0.16, relwidth = 0.12)
minute_end_top = tkinter.OptionMenu(minute_end_top_frame, minute_str_top_end, *minute_list)
minute_end_top.place(relx = 0, rely = 0, relheight = 0.7, relwidth = 1)
minute_end_top_label = tkinter.Label(minute_end_top_frame, bg = 'white', text = "Ending Minute")
minute_end_top_label.place(relx = 0, rely = 0.7, relheight = 0.3, relwidth = 1)

am_pm_top_end_frame = tkinter.Frame(top_frame, highlightthickness=2, highlightbackground="black")
am_pm_top_end_frame.place(relx = 0.81, rely = 0.52, relheight = 0.16, relwidth = 0.10)
am_radio_top_end = tkinter.Radiobutton(am_pm_top_end_frame, text = "AM", variable = AM_PM_top_end, value = 'AM')
am_radio_top_end.place(relx = 0, rely = 0, relheight = 0.35, relwidth = 1)
pm_radio_top_end = tkinter.Radiobutton(am_pm_top_end_frame, text = "PM", variable = AM_PM_top_end, value = 'PM')
pm_radio_top_end.place(relx = 0, rely = 0.35, relheight = 0.35, relwidth = 1)
am_pm_top_end_label = tkinter.Label(am_pm_top_end_frame, bg = 'white', text = 'Ending AM/PM')
am_pm_top_end_label.place(relx = 0, rely = 0.7, relheight = 0.3, relwidth = 1)

clear_end_top = tkinter.Button(top_frame, text=' Clear end ', fg='black', bg='red', justify = 'center', command = lambda: clear_end_top_func())
clear_end_top.place(relx = 0.92, rely = 0.52, relheight = 0.16, relwidth = 0.06)
#Now create a calculate button, a result box, and a clear button for the third row (still in the top capability):
calculate_top = tkinter.Button(top_frame, text=' Calculate ', fg='black', bg='lightgreen', justify = 'center', relief = 'raised', command = lambda: calc_top_func())
calculate_top.place(relx = 0.05, rely = 0.76, relheight = 0.16, relwidth = 0.2)
result_top = tkinter.Label(top_frame, bg = 'yellow', bd = 3, relief = 'solid', text = "", justify = 'center')
result_top.place(relx = 0.3, rely = 0.76, relheight = 0.16, relwidth = 0.4)
clear_result_top = tkinter.Button(top_frame, text=' Clear result ', fg='black', bg='red', justify = 'center', command = lambda: clear_result_top_func())
clear_result_top.place(relx = 0.71, rely = 0.76, relheight = 0.16, relwidth = 0.08)
clear_all_top = tkinter.Button(top_frame, text=' Clear all ', fg='white', bg='darkred', justify = 'center', command = lambda: clear_all_top_func())
clear_all_top.place(relx = 0.80, rely = 0.76, relheight = 0.16, relwidth = 0.18)
#Now create and set buttons for the first row, the start time/date for the bottom capability:
bottom_frame = tkinter.Frame(gui, highlightthickness=4, highlightbackground="black")
bottom_frame.place(relx=0, rely=0.5, relheight=0.5, relwidth=1)
bottom_canvas = tkinter.Canvas(bottom_frame, width = 1400, height = 375)
bottom_canvas.create_line(30, 183, 1362, 183, dash = (5, 1))
bottom_canvas.create_line(30, 265, 1362, 265, dash = (5, 1))
bottom_canvas.pack()
label_bottom = tkinter.Label(bottom_frame, bg = 'white', bd = 3, relief = 'solid', text = "Project a set amount of time from a start time", font = 25)
label_bottom.place(relx=0.3, rely=0.04, relheight=0.2, relwidth=0.4)
#Make labels for the rows of data that will be needed:
label_start_year_bottom = tkinter.Label(bottom_frame, bg = 'white', bd = 3, relief = 'solid', text = "Start date and time:")
label_start_year_bottom.place(relx=0.02, rely=0.32, relheight=0.16, relwidth=0.13)

#Now create and set buttons for the first row, the start time/date for the bottom capability:
year_start_bottom_frame = tkinter.Frame(bottom_frame, highlightthickness=2, highlightbackground="black")
year_start_bottom_frame.place(relx = 0.16, rely = 0.32, relheight = 0.16, relwidth = 0.12)
year_start_bottom = tkinter.OptionMenu(year_start_bottom_frame, year_str_bottom, *year_list)
year_start_bottom.place(relx = 0, rely = 0, relheight = 0.7, relwidth = 1)
year_start_bottom_label = tkinter.Label(year_start_bottom_frame, bg = 'white', text = "Starting Year")
year_start_bottom_label.place(relx = 0, rely = 0.7, relheight = 0.3, relwidth = 1)

month_start_bottom_frame = tkinter.Frame(bottom_frame, highlightthickness=2, highlightbackground="black")
month_start_bottom_frame.place(relx = 0.29, rely = 0.32, relheight = 0.16, relwidth = 0.12)
month_start_bottom = tkinter.OptionMenu(month_start_bottom_frame, month_str_bottom, *month_list)
month_start_bottom.place(relx = 0, rely = 0, relheight = 0.7, relwidth = 1)
month_start_bottom_label = tkinter.Label(month_start_bottom_frame, bg = 'white', text = "Starting Month")
month_start_bottom_label.place(relx = 0, rely = 0.7, relheight = 0.3, relwidth = 1)

day_start_bottom_frame = tkinter.Frame(bottom_frame, highlightthickness=2, highlightbackground="black")
day_start_bottom_frame.place(relx = 0.42, rely = 0.32, relheight = 0.16, relwidth = 0.12)
day_start_bottom = tkinter.OptionMenu(day_start_bottom_frame, day_str_bottom, *day_list)
day_start_bottom.place(relx = 0, rely = 0, relheight = 0.7, relwidth = 1)
month_start_bottom_label = tkinter.Label(day_start_bottom_frame, bg = 'white', text = "Starting Day")
month_start_bottom_label.place(relx = 0, rely = 0.7, relheight = 0.3, relwidth = 1)

hour_start_bottom_frame = tkinter.Frame(bottom_frame, highlightthickness=2, highlightbackground="black")
hour_start_bottom_frame.place(relx = 0.55, rely = 0.32, relheight = 0.16, relwidth = 0.12)
hour_start_bottom = tkinter.OptionMenu(hour_start_bottom_frame, hour_str_bottom, *hour_list)
hour_start_bottom.place(relx = 0, rely = 0, relheight = 0.7, relwidth = 1)
hour_start_bottom_label = tkinter.Label(hour_start_bottom_frame, bg = 'white', text = "Starting Hour")
hour_start_bottom_label.place(relx = 0, rely = 0.7, relheight = 0.3, relwidth = 1)

minute_start_bottom_frame = tkinter.Frame(bottom_frame, highlightthickness=2, highlightbackground="black")
minute_start_bottom_frame.place(relx = 0.68, rely = 0.32, relheight = 0.16, relwidth = 0.12)
minute_start_bottom = tkinter.OptionMenu(minute_start_bottom_frame, minute_str_bottom, *minute_list)
minute_start_bottom.place(relx = 0, rely = 0, relheight = 0.7, relwidth = 1)
minute_start_bottom_label = tkinter.Label(minute_start_bottom_frame, bg = 'white', text = "Starting Minute")
minute_start_bottom_label.place(relx = 0, rely = 0.7, relheight = 0.3, relwidth = 1)

am_pm_bottom_frame = tkinter.Frame(bottom_frame, highlightthickness=2, highlightbackground="black")
am_pm_bottom_frame.place(relx = 0.81, rely = 0.32, relheight = 0.16, relwidth = 0.10)
am_radio_bottom = tkinter.Radiobutton(am_pm_bottom_frame, text = "AM", variable = AM_PM_bottom, value = 'AM')
am_radio_bottom.place(relx = 0, rely = 0, relheight = 0.35, relwidth = 1)
pm_radio_bottom = tkinter.Radiobutton(am_pm_bottom_frame, text = "PM", variable = AM_PM_bottom, value = 'PM')
pm_radio_bottom.place(relx = 0, rely = 0.35, relheight = 0.35, relwidth = 1)
am_pm_bottom_label = tkinter.Label(am_pm_bottom_frame, bg = 'white', text = 'Starting AM/PM')
am_pm_bottom_label.place(relx = 0, rely = 0.7, relheight = 0.3, relwidth = 1)

clear_start_bottom = tkinter.Button(bottom_frame, text=' Clear start ', fg='black', bg='red', justify = 'center', command = lambda: clear_start_bottom_func())
clear_start_bottom.place(relx = 0.92, rely = 0.32, relheight = 0.16, relwidth = 0.06)
#Now create boxes to enter time to add for bottom capability:
label_add_time_bottom = tkinter.Label(bottom_frame, bg = 'white', bd = 3, relief = 'solid', text = "Time to add:")
label_add_time_bottom.place(relx=0.02, rely=0.52, relheight=0.16, relwidth=0.13)

weeks_input_frame = tkinter.Frame(bottom_frame, highlightthickness=1, highlightbackground="black")
weeks_input_frame.place(relx = 0.16, rely = 0.52, relheight = 0.16, relwidth = 0.17)
weeks_input = tkinter.Entry(weeks_input_frame, textvariable = weeks_to_add, justify='center')
weeks_input.place(relx = 0, rely = 0, relheight = 0.75, relwidth = 1)
weeks_input_label = tkinter.Label(weeks_input_frame, bg = 'white', bd = 1, relief = 'solid', text = "Weeks to add")
weeks_input_label.place(relx = 0, rely = 0.75, relheight = 0.25, relwidth = 1)

days_input_frame = tkinter.Frame(bottom_frame, highlightthickness=1, highlightbackground="black")
days_input_frame.place(relx = 0.34, rely = 0.52, relheight = 0.16, relwidth = 0.17)
days_input = tkinter.Entry(days_input_frame, textvariable = days_to_add, justify='center')
days_input.place(relx = 0, rely = 0, relheight = 0.75, relwidth = 1)
days_input_label = tkinter.Label(days_input_frame, bg = 'white', bd = 1, relief = 'solid', text = "Days to add")
days_input_label.place(relx = 0, rely = 0.75, relheight = 0.25, relwidth = 1)


hours_input_frame = tkinter.Frame(bottom_frame, highlightthickness=1, highlightbackground="black")
hours_input_frame.place(relx = 0.52, rely = 0.52, relheight = 0.16, relwidth = 0.17)
hours_input = tkinter.Entry(hours_input_frame, textvariable = hours_to_add, justify='center')
hours_input.place(relx = 0, rely = 0, relheight = 0.75, relwidth = 1)
hours_input_label = tkinter.Label(hours_input_frame, bg = 'white', bd = 1, relief = 'solid', text = "Hours to add")
hours_input_label.place(relx = 0, rely = 0.75, relheight = 0.25, relwidth = 1)

minutes_input_frame = tkinter.Frame(bottom_frame, highlightthickness=1, highlightbackground="black")
minutes_input_frame.place(relx = 0.70, rely = 0.52, relheight = 0.16, relwidth = 0.17)
minutes_input = tkinter.Entry(minutes_input_frame, textvariable = minutes_to_add, justify='center')
minutes_input.place(relx = 0, rely = 0, relheight = 0.75, relwidth = 1)
minutes_input_label = tkinter.Label(minutes_input_frame, bg = 'white', bd = 1, relief = 'solid', text = "Minutes to add")
minutes_input_label.place(relx = 0, rely = 0.75, relheight = 0.25, relwidth = 1)

clear_add_bottom = tkinter.Button(bottom_frame, text=' Clear add time ', fg='black', bg='red', justify = 'center', command = lambda: clear_add_bottom_func())
clear_add_bottom.place(relx = 0.88, rely = 0.52, relheight = 0.16, relwidth = 0.1)
#Now create a calculate button, a result box, and a clear button for the third row of the bottom capability:
calculate_bottom = tkinter.Button(bottom_frame, text=' Calculate ', fg='black', bg='lightgreen', justify = 'center', relief = 'raised', command = lambda: calc_bottom_func())
calculate_bottom.place(relx = 0.05, rely = 0.76, relheight = 0.16, relwidth = 0.2)
result_bottom = tkinter.Label(bottom_frame, bg = 'yellow', bd = 3, relief = 'solid', text = "", justify = 'center')
result_bottom.place(relx = 0.3, rely = 0.76, relheight = 0.16, relwidth = 0.4)
clear_result_bottom = tkinter.Button(bottom_frame, text=' Clear result ', fg='black', bg='red', justify = 'center', command = lambda: clear_result_bottom_func())
clear_result_bottom.place(relx = 0.71, rely = 0.76, relheight = 0.16, relwidth = 0.08)
clear_all_bottom = tkinter.Button(bottom_frame, text=' Clear all ', fg='white', bg='darkred', justify = 'center', command = lambda: clear_all_bottom_func())
clear_all_bottom.place(relx = 0.80, rely = 0.76, relheight = 0.16, relwidth = 0.18)

if __name__ == "__main__":
    gui.mainloop()
