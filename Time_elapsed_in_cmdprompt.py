import datetime

#Here is a little function to check if a year is a leap year or not, which I will be using later on to sort if an input of a day is valid:
def is_leap_year(year):
    year = int(year)
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 ==0) and (year % 100 != 0):
        return True
    else:
        return False

mode = input('Press 1 to obtain the difference between two times/dates or press 2 to project a certain amount of time \
ahead from a certain date: ' + '\n')
# mode = '2'
while (mode != '1') and (mode != '2'):
    print('start of while and mode is:', mode)
    mode = input('Press 1 to obtain the difference between two times/dates or press 2 to project a certain amount of time \
ahead from a certain date: ' + '\n')

print('Let\'s gather the start time info down to the minute: ' + '\n')

start_year_acceptable = False
start_year = input('Please enter the year of the start time/date: ' + '\n')
while start_year_acceptable == False:
    try:
        start_year = int(float(start_year)) #throw the float in there to handle wise guys with decimal inputs
        break #get out of while loop
        # start_year_acceptable = True
        # continue #to get back to start of while loop, which will be broken out of since the acceptable variable it True now
    except:
        start_year = input('The year of the start time/date must be number: ' + '\n')
        continue

start_month_acceptable = False
start_month = input('Please enter the number of the month of the start time/date: ' + '\n')
while start_month_acceptable == False:
    try:
        start_month = int(float(start_month)) #throw the float in there to handle wise guys with decimal inputs
        if (start_month >= 1) and (start_month <= 12): #if start month is a number and a valid month value as well
            break #get out of while loop
            # start_month_acceptable = True
            # continue #to get back to start of while loop, which will be broken out of since the acceptable variable it True now
        elif start_month < 1: #if a number was inputted but it was too low
            start_month = input('That\'s too low. The month number must be at least 1, which corresponds with January: ' + '\n')
            continue #get back to while loop
        elif start_month > 12: #if a number was inputted but it was too high
            start_month = input('That\'s too high. The month number must be at most 12, which corresponds with December: ' + '\n')
            continue #get back to while loop
    except: #if a non-number was entered
        start_month = input('The month of the start time/date must be number as small as 1 for January and as large as 12 for December: ' + '\n')
        continue # get back to while loop

start_day_acceptable = False
months_with_31_days = [1, 3, 5, 7, 8, 10, 12] #list of month numbers with 31 days
months_with_30_days = [4, 6, 9, 11] #list of month numbers with 30 days
start_day = input('Please enter the number of the day in the month for the start time/date: ' + '\n')
while start_day_acceptable == False:
    # print('\n')
    # print('just started the while loop from the top with start_day: ', start_day)
    try:
        # print('beginning of try part')
        start_day = int(float(start_day)) #throw the float in there to handle wise guys with decimal inputs
        # print('got to right before the first if statement')
        if start_day < 1: #too handle all inputs that are too low
            # print('got to the too low part')
            start_day = input('That\'s too low. The day number must be at least 1, which corresponds with the first day of the month: ' + '\n')
            continue #get back to while loop
        elif (start_month == 2) and (is_leap_year(start_year) == True) and (start_day <= 29): #if February is the month, a leap year is chosen, and the day is 29 or lower, which is valid
            # print('good Feb leap year')
            break #get out of while loop
        elif (start_month == 2) and (is_leap_year(start_year) == False) and (start_day <= 28): # if Feb, non-leap, and day is 28 or less, which is valid
            # print('good Feb not a leap year')
            break #get out of while loop
        elif (start_month in months_with_31_days) and (start_day <= 31):
            # print('good 31 day month')
            break #get out of while loop
        elif (start_month  in months_with_30_days) and (start_day <= 30):
            # print('good 30 day month')
            break #get out of while loop
        else:
            # print('got to the too high part')
            start_day = input('That is too high of a number of a day for that month. Please choose a lower number: ' + '\n')
            continue
    except Exception as error: #if a non-number was entered
        # print("An error occurred:", type(error).__name__)
        start_day = input('The day of the start time/date must be number as small as 1 or as high as the number of days in the month chosen: ' + '\n')
        continue # get back to while loop

start_hour_acceptable = False
start_hour = (input('Please enter the hour of the start time/date. Use military time so that midnight is 0, 1pm is 13, 2pm is 14, etc.: ' + '\n'))
while start_hour_acceptable == False:
    # print('\n')
    # print('just started while loop with start hour :', start_hour)
    try:
        start_hour = int(float(start_hour)) #throw the float in there to handle wise guys with decimal inputs
        if start_hour < 0: #too handle all inputs that are too low
            # print('got to the too low part')
            start_hour = input('That\'s too low. The hour must be at least 0, which corresponds with midnight: ' + '\n')
            continue #get back to while loop
        elif start_hour > 23:
            start_hour = input('That\'s too high. The hour must be at most 23, which corresponds with 11 pm: ' + '\n')
            continue#get back to while loop
        break #get out of while loop
        # start_hour_acceptable = True
        # continue #to get back to start of while loop, which will be broken out of since the acceptable variable it True now
    except: #to handle non-number inputs
        start_hour = input('The hour of the start time/date must be number: ' + '\n')
        continue

start_minute_acceptable = False
start_minute = (input('Please enter the minute of the start time/date:' + '\n'))
while start_minute_acceptable == False:
    # print('\n')
    # print('just started while loop with start minute :', start_minute)
    try:
        start_minute = int(float(start_minute)) #throw the float in there to handle wise guys with decimal inputs
        if start_minute < 0: #too handle all inputs that are too low
            # print('got to the too low part')
            start_minute = input('That\'s too low. The minute must be at least 0: ' + '\n')
            continue #get back to while loop
        elif start_minute > 59:
            start_minute = input('That\'s too high. The minute must be at most 59, which corresponds to the 59th minute of the hour: ' + '\n')
            continue#get back to while loop
        break #get out of while loop
        # start_hour_acceptable = True
        # continue #to get back to start of while loop, which will be broken out of since the acceptable variable it True now
    except: #to handle non-number inputs
        start_hour = input('The minute of the start time/date must be number: ' + '\n')
        continue
# start_year = 2023
# start_month = 7
# start_day = 3
# start_hour = 12
# start_minute = 5

start_date_time = datetime.datetime(start_year, start_month, start_day, start_hour, start_minute, 0)
print('The start date/time is ', start_date_time.strftime('%A'), ', ', start_date_time.strftime('%d'), ' ', start_date_time.strftime('%B'), \
', ', start_date_time.strftime('%Y'), ' at ', start_date_time.strftime('%X'), '.', '\n', sep = '' )
if mode == '1':
    print('Now let\'s get the ending time info.', '\n')

    end_year_acceptable = False
    end_year = input('Please enter the year of the end time/date: ' + '\n')
    while end_year_acceptable == False:
        try:
            end_year = int(float(end_year)) #throw the float in there to handle wise guys with decimal inputs
            break #get out of while loop
            # end_year_acceptable = True
            # continue #to get back to end of while loop, which will be broken out of since the acceptable variable it True now
        except:
            end_year = input('The year of the end time/date must be number: ' + '\n')
            continue

    end_month_acceptable = False
    end_month = input('Please enter the number of the month of the end time/date: ' + '\n')
    while end_month_acceptable == False:
        try:
            end_month = int(float(end_month)) #throw the float in there to handle wise guys with decimal inputs
            if (end_month >= 1) and (end_month <= 12): #if end month is a number and a valid month value as well
                break #get out of while loop
                # end_month_acceptable = True
                # continue #to get back to end of while loop, which will be broken out of since the acceptable variable it True now
            elif end_month < 1: #if a number was inputted but it was too low
                end_month = input('That\'s too low. The month number must be at least 1, which corresponds with January: ' + '\n')
                continue #get back to while loop
            elif end_month > 12: #if a number was inputted but it was too high
                end_month = input('That\'s too high. The month number must be at most 12, which corresponds with December: ' + '\n')
                continue #get back to while loop
        except: #if a non-number was entered
            end_month = input('The month of the end time/date must be number as small as 1 for January and as large as 12 for December: ' + '\n')
            continue # get back to while loop

    end_day_acceptable = False
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12] #list of month numbers with 31 days
    months_with_30_days = [4, 6, 9, 11] #list of month numbers with 30 days
    end_day = input('Please enter the number of the day in the month for the end time/date: ' + '\n')
    while end_day_acceptable == False:
        # print('\n')
        # print('just ended the while loop from the top with end_day: ', end_day)
        try:
            # print('beginning of try part')
            end_day = int(float(end_day)) #throw the float in there to handle wise guys with decimal inputs
            # print('got to right before the first if statement')
            if end_day < 1: #too handle all inputs that are too low
                # print('got to the too low part')
                end_day = input('That\'s too low. The day number must be at least 1, which corresponds with the first day of the month: ' + '\n')
                continue #get back to while loop
            elif (end_month == 2) and (is_leap_year(end_year) == True) and (end_day <= 29): #if February is the month, a leap year is chosen, and the day is 29 or lower, which is valid
                # print('good Feb leap year')
                break #get out of while loop
            elif (end_month == 2) and (is_leap_year(end_year) == False) and (end_day <= 28): # if Feb, non-leap, and day is 28 or less, which is valid
                # print('good Feb not a leap year')
                break #get out of while loop
            elif (end_month in months_with_31_days) and (end_day <= 31):
                # print('good 31 day month')
                break #get out of while loop
            elif (end_month  in months_with_30_days) and (end_day <= 30):
                # print('good 30 day month')
                break #get out of while loop
            else:
                # print('got to the too high part')
                end_day = input('That is too high of a number of a day for that month. Please choose a lower number: ' + '\n')
                continue
        except Exception as error: #if a non-number was entered
            # print("An error occurred:", type(error).__name__)
            end_day = input('The day of the end time/date must be number as small as 1 or as high as the number of days in the month chosen: ' + '\n')
            continue # get back to while loop

    end_hour_acceptable = False
    end_hour = (input('Please enter the hour of the end time/date. Use military time so that midnight is 0, 1pm is 13, 2pm is 14, etc.: ' + '\n'))
    while end_hour_acceptable == False:
        # print('\n')
        # print('just ended while loop with end hour :', end_hour)
        try:
            end_hour = int(float(end_hour)) #throw the float in there to handle wise guys with decimal inputs
            if end_hour < 0: #too handle all inputs that are too low
                # print('got to the too low part')
                end_hour = input('That\'s too low. The hour must be at least 0, which corresponds with midnight: ' + '\n')
                continue #get back to while loop
            elif end_hour > 23:
                end_hour = input('That\'s too high. The hour must be at most 23, which corresponds with 11 pm: ' + '\n')
                continue#get back to while loop
            break #get out of while loop
            # end_hour_acceptable = True
            # continue #to get back to end of while loop, which will be broken out of since the acceptable variable it True now
        except: #to handle non-number inputs
            end_hour = input('The hour of the end time/date must be number: ' + '\n')
            continue

    end_minute_acceptable = False
    end_minute = (input('Please enter the minute of the end time/date:' + '\n'))
    while end_minute_acceptable == False:
        # print('\n')
        # print('just ended while loop with end minute :', end_minute)
        try:
            end_minute = int(float(end_minute)) #throw the float in there to handle wise guys with decimal inputs
            if end_minute < 0: #too handle all inputs that are too low
                # print('got to the too low part')
                end_minute = input('That\'s too low. The minute must be at least 0: ' + '\n')
                continue #get back to while loop
            elif end_minute > 59:
                end_minute = input('That\'s too high. The minute must be at most 59, which corresponds to the 59th minute of the hour: ' + '\n')
                continue#get back to while loop
            break #get out of while loop
            # end_hour_acceptable = True
            # continue #to get back to end of while loop, which will be broken out of since the acceptable variable it True now
        except: #to handle non-number inputs
            end_hour = input('The minute of the end time/date must be number: ' + '\n')
            continue


    # end_year = 2020
    # end_month = 7
    # end_day = 3
    # end_hour = 12
    # end_minute = 5


    # end_year = 2023
    # end_month = 7
    # end_day = 19
    # end_hour = 14
    # end_minute = 0

    end_date_time = datetime.datetime(end_year, end_month, end_day, end_hour, end_minute, 0)
    print('The end date/time is ', end_date_time.strftime('%A'), ', ', end_date_time.strftime('%d'), ' ', end_date_time.strftime('%B'), \
    ', ', end_date_time.strftime('%Y'), ' at ', end_date_time.strftime('%X'), '.', '\n', sep = '' )

    diff = end_date_time - start_date_time #create a time delta object that is the difference of end and start times. This will only have days, second, and milliseconds so I'll need to convert to also get weeks, hours, and minutes
    diff_weeks = diff_hours = diff_minutes = 0
    diff_days = diff.days #define these now in case one of them is zero and to avoid funny business with the following week,hour,minute creations
    diff_seconds = diff.seconds
    if diff.days > 6: #if 7 days or more have passed
        diff_weeks = diff.days // 7 #get the number of full weeks
        diff_days = diff.days - (diff_weeks * 7) #get a new count of days remaining that doesn't include those full weeks
    if diff_seconds > 3600: #if more than an hour has passed
        diff_hours = diff_seconds // 3600 #get the number of full hours
        diff_seconds = diff_seconds - (diff_hours * 3600) #get a new count of seconds that doesn't include the full hours
    if diff_seconds > 60: #if more than a full minute
        diff_minutes = diff_seconds // 60
        diff_seconds = diff_seconds - (diff_minutes * 60)

    # print('diff_weeks is: ', diff_weeks)
    # print('diff_days is: ', diff_days)
    # print('diff_hours is: ', diff_hours)
    # print('diff_minutes is: ', diff_minutes)
    # print('diff_seconds is: ', diff_seconds)
    #create a dictionary to cycle through so I can check and only print out non-zero values. No need for seconds since that will be zero since I only measured the start time to the minute.
    diff_dict = {'0': ['week', diff_weeks], '1': ['day', diff_days], '2': ['hour', diff_hours], '3': ['minute', diff_minutes]}
    non_zero_terms_remaining = 0 #start a count of how many categories of time have a non-zero amount
    for digit in range (0,4):
        digit = str(digit)
        if diff_dict[digit][1] != 0: #if that term in the dictionary is non-zero
            non_zero_terms_remaining += 1
            # print('going up due to ', diff_dict[digit][0])
    # print(non_zero_terms_remaining)

    if non_zero_terms_remaining == 0: #if the condition of start and end time are the same is met
        print('No time has elapsed. The start and end time are the same.')
        quit()
    statement = 'The time elapsed from start to end is' #start ending print statement for actual time elapsed if not zero

    for digit in range (0,4):
        digit = str(digit)
        if diff_dict[digit][1] != 0: #only do the following if the value is not zero
            statement = statement + ' ' + str(diff_dict[digit][1]) + ' ' + diff_dict[digit][0]
            if (diff_dict[digit][1] > 1) or (diff_dict[digit][1] < 0): #to account for multiple in positive or negative amounts
                statement += 's'
            non_zero_terms_remaining -= 1
            if non_zero_terms_remaining == 0: #if this was the last term
                statement += '.'
            elif non_zero_terms_remaining == 1: #if this was just the second to last term
                statement += ', and'
            else:
                statement += ','
    print(statement)
    #Now get the time elapsed in only hours and minutes:
    statement2 = 'In just hours and minutes, this is'
    diff_hours_new = diff_hours + (diff_weeks * 24 * 7) + (diff_days * 24)
    diff_dict_new = {'0': ['hour', diff_hours_new], '1': ['minute', diff_minutes]}
    non_zero_terms_remaining_new = 0 #start a count of how many categories of time have a non-zero amount
    for digit in range (0,2):
        digit = str(digit)
        if diff_dict_new[digit][1] != 0: #if that term in the dictionary is non-zero
            non_zero_terms_remaining_new += 1
            # print('going up due to ', diff_dict_new[digit][0])
    # print(non_zero_terms_remaining_new)
    for digit in range (0,2):
        digit = str(digit)
        if diff_dict_new[digit][1] != 0: #only do the following if the value is not zero
            statement2 = statement2 + ' ' + str(diff_dict_new[digit][1]) + ' ' + diff_dict_new[digit][0]
            if (diff_dict_new[digit][1] > 1) or ((diff_dict_new[digit][1] < 0)): #to account for multiple in positive or negative amounts
                statement2 += 's'
            non_zero_terms_remaining_new -= 1
            if non_zero_terms_remaining_new == 0: #if this was the last term
                statement2 += '.'
            elif non_zero_terms_remaining_new == 1: #if this was just the second to last term
                statement2 += ' and'
    print('\n' + statement2)
    quit()

elif mode == '2':
    weeks_add_acceptable = False
    weeks_add = input('Please enter the number of weeks you\'d like to jump into the future: ' + '\n')
    while weeks_add_acceptable == False:
        try:
            weeks_add = int(float(weeks_add)) #throw the float in there to handle wise guys with decimal inputs
            break #get out of while loop
        except:
            weeks_add = input('The number of weeks added to the start date must be number: ' + '\n')
            continue

    days_add_acceptable = False
    days_add = input('Please enter the number of days you\'d like to jump into the future: ' + '\n')
    while days_add_acceptable == False:
        try:
            days_add = int(float(days_add)) #throw the float in there to handle wise guys with decimal inputs
            break #get out of while loop
        except:
            days_add = input('The number of days added to the start date must be number: ' + '\n')
            continue

    hours_add_acceptable = False
    hours_add = input('Please enter the number of hours you\'d like to jump into the future: ' + '\n')
    while hours_add_acceptable == False:
        try:
            hours_add = int(float(hours_add)) #throw the float in there to handle wise guys with decimal inputs
            break #get out of while loop
        except:
            hours_add = input('The number of hours added to the start date must be number: ' + '\n')
            continue

    minutes_add_acceptable = False
    minutes_add = input('Please enter the number of minutes you\'d like to jump into the future: ' + '\n')
    while minutes_add_acceptable == False:
        try:
            minutes_add = int(float(minutes_add)) #throw the float in there to handle wise guys with decimal inputs
            break #get out of while loop
        except:
            minutes_add = input('The number of minutes added to the start date must be number: ' + '\n')
            continue
    # weeks_add = 0
    # days_add = 0
    # hours_add = 0
    # minutes_add = 0
    statement_add = 'The amount of time to add is'
    statement_add_2 = ''
    dict_add = {'0': ['week', weeks_add], '1': ['day', days_add], '2': ['hour', hours_add], '3': ['minute', minutes_add]}
    non_zero_terms_remaining_add = 0 #start a count of how many categories of time have a non-zero amount
    for digit in range (0,4):
        digit = str(digit)
        if dict_add[digit][1] != 0: #if that term in the dictionary is non-zero
            non_zero_terms_remaining_add += 1
    if non_zero_terms_remaining_add == 0:
        statement_add_2 += ' nothing.'
    for digit in range (0,4):
        digit = str(digit)
        if dict_add[digit][1] != 0: #only do the following if the value is not zero
            statement_add_2 = statement_add_2 + ' ' + str(dict_add[digit][1]) + ' ' + dict_add[digit][0]
            if (dict_add[digit][1] > 1) or ((dict_add[digit][1] < 0)): #to account for multiple in positive or negative amounts
                statement_add_2 += 's'
            non_zero_terms_remaining_add -= 1
            if non_zero_terms_remaining_add == 0: #if this was the last term
                statement_add_2 += '.'
            elif non_zero_terms_remaining_add == 1: #if this was just the second to last term
                statement_add_2 += ', and'
            else:
                statement_add_2 += ','
    print(statement_add + statement_add_2 + '\n')


    add_time = datetime.timedelta(days = (weeks_add * 7 + days_add), hours = hours_add, minutes = minutes_add)
    # print(add_time)
    end_date_time = start_date_time + add_time
    # print(end_date_time)
    print('The end date/time is ', end_date_time.strftime('%A'), ', ', end_date_time.strftime('%d'), ' ', end_date_time.strftime('%B'), \
    ', ', end_date_time.strftime('%Y'), ' at ', end_date_time.strftime('%X'), '.',sep = '' )
