#create pieces_lists such that the first (0th) element will have the display for that row for zero, etc.
first_row_pieces = ['###', '  #', '###', '###', '# #', '###', '###', '###', '###', '###', '   ']
second_row_pieces = ['# #', '  #', '  #', '  #', '# #', '#  ', '#  ', '  #', '# #', '# #', '   ']
third_row_pieces = ['# #', '  #', '###', '###', '###', '###', '###', '  #', '###', '###', '###']
fourth_row_pieces = ['# #', '  #', '#  ', '  #', '  #', '  #', '# #', '  #', '# #', '  #', '   ']
fifth_row_pieces = ['###', '  #', '###', '###', '  #', '###', '###', '  #', '###', '###', '   ']

# print(first_row_pieces)
# print(second_row_pieces)
# print(third_row_pieces)
# print(fourth_row_pieces)
# print(fifth_row_pieces)

def seven_segment_display():
    number = input('Please enter a combination of numbers and hyphens that you\'d like displayed in seven segment style: ').replace('\s', '')
    input_acceptable = False #to get into the while loop
    while input_acceptable == False:
        input_acceptable = True # do this such that one failed character can prompt a change back to failing and the while loop will repeat
        for char in number:
            if not ( (char == '-') or (char in '0123456789') ): #if the char is not either a hyphen or a number
                input_acceptable = False
                number = input('Please enter a number you\'d like displayed in seven segment style. Digits and hyphens only this time: ').replace('\s', '')
                continue #go back to start of while loop
    #create strings to build the display out of:
    first_row = second_row = third_row = fourth_row = fifth_row = ''

    remaining_length = len(number) # dummy variable so I can treat last character differently with regards to spacing

    for char in number:
        if remaining_length > 1: #to put spaces in if another char is coming after this one
            if char == '-':
                first_row = first_row + first_row_pieces[10] + '   '
                second_row = second_row + second_row_pieces[10] + '   '
                third_row = third_row + third_row_pieces[10] + '   '
                fourth_row = fourth_row + fourth_row_pieces[10] + '   '
                fifth_row = fifth_row + fifth_row_pieces[10] + '   '
                remaining_length -= 1

            else:
                first_row = first_row + first_row_pieces[int(char)] + '   '
                second_row = second_row + second_row_pieces[int(char)] + '   '
                third_row = third_row + third_row_pieces[int(char)] + '   '
                fourth_row = fourth_row + fourth_row_pieces[int(char)] + '   '
                fifth_row = fifth_row + fifth_row_pieces[int(char)] + '   '
                remaining_length -= 1
        else: #to only put in the #'s with no spaces afterwards for the last digit
            if char == '-':
                first_row = first_row + first_row_pieces[10]
                second_row = second_row + second_row_pieces[10]
                third_row = third_row + third_row_pieces[10]
                fourth_row = fourth_row + fourth_row_pieces[10]
                fifth_row = fifth_row + fifth_row_pieces[10]
            else:
                first_row = first_row + first_row_pieces[int(char)]
                second_row = second_row + second_row_pieces[int(char)]
                third_row = third_row + third_row_pieces[int(char)]
                fourth_row = fourth_row + fourth_row_pieces[int(char)]
                fifth_row = fifth_row + fifth_row_pieces[int(char)]

    #to better handle the \n line breaks, set the desired print out to a variable and then return the variable
    statement = '\n' + first_row + '\n' + second_row + '\n' + third_row + '\n' + fourth_row + '\n' + fifth_row + '\n'
    return statement


print(seven_segment_display())
