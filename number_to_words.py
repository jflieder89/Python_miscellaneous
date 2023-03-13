import math #for ceiling function
import re #import regular expressions to just make sure only numbers are entered

hundreds = {'1': 'one hundred', '2': 'two hundred', '3': 'three hundred', '4': 'four hundred', '5': 'five hundred', \
'6': 'six hundred', '7': 'seven hundred', '8': 'eight hundred', '9': 'nine hundred'}
tens = {'2': 'twenty', '3': 'thirty', '4': 'fourty', '5': 'fifty', \
'6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}
teens = {'10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', \
'16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'}
ones = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', \
'6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
places_dict = {'5': ['trillion', 'billion', 'million', 'thousand', 'ones'], '4': ['billion', 'million', 'thousand', 'ones'], \
'3': ['million', 'thousand', 'ones'], '2': ['thousand', 'ones'], '1': ['ones']}
decimal_ending = ['tenths', 'hundredths', 'thousandths', 'ten thousandths', 'hundred thousandths', 'millionths', \
'ten millionths', 'hundred millionths', 'billionths', 'ten billionths', 'hundred billionths', 'trillionths', 'ten trillionths', \
'hundred trillionths', 'quadrillionths']

def words_number(digits, placement): #my side function to spit out wording for a specific placement (millions, thousands, etc.) for left side of decimal place
    statement = ''
    if placement == 'ones': #remove ones so it is not added to the string at the end
        placement = ''
    if int(digits) == 0: #just cut out if there is a 000 for a placement like in 3,000,436
        return
    if (digits == '0') or (digits == '00') or (digits == '000') or (digits == ''): #if there is zero for this entire placement like the thousands in 3,000,325
        return
    #deal with the hundreds place:
    if (len(digits) == 3) and (digits[0] != '0'): #if there will be hundreds of the placement
        statement += (' ' + hundreds[digits[0]])
        digits = digits[1:] #just keep the non-hundreds portion going forward
    elif (len(digits) == 3) and (digits[0] == 0): #if there are no hundreds of the placement
        digits = digits[1:] #just keep the non-hundreds portion going forward
    #deal with the tens place, and with the shift of digits from above, the tens place is now the 0th element of digits
    if (len(digits) > 1) and (digits[0] != '0') and (digits[0] != '1'): #if there will be tens in the placement, with no teens included yet
        #print(digits)
        #print(digits[0] != 1)
        statement += (' ' + tens[digits[0]])
        digits = digits[1:] #just keep the ones going forward
    elif (len(digits) > 1) and (digits[0] == '1'): # if there are teens
        statement += (' ') + teens[digits]
        #can end it here since the teens part took up the ones part as well:
        statement += ' ' + placement
        return statement.strip() + ','
    elif (len(digits) > 1) and (digits[0] == '0'): #No tens, whether it be with teens or otherwise
        digits = digits[1:] #just keep the ones going forward

    #deal with the ones place:
    if digits != '0': #if there is a ones place that is non-zer0
        statement += (' ') + ones[digits]
        #can end it here since whole of the original digits is done now
        statement += ' ' + placement
        return statement.strip() + ','
    statement += ' ' + placement
    return statement.strip() + ','
#print(word_numbers('9', 'thousand'))
#print(words_number('923', 'trillion'))

def words_decimal(digits): #my side function to spit out wording for right side of decimal place
    statement = ''
    placement = decimal_ending[len(digits) - 1] #pick your ending of tenths, thousandths, etc before going forward
    if int(digits) == 1: #if the decimal part of the original part was .001 or .01 or .1
        placement = placement.strip('s') #make is singular in this case
    #print('Placement for decimal is :', placement)
    #deal with the all 3 decimal places with a digit:
    if (len(digits) == 3):
        if digits[0] != '0': #non-zero tenths spot
            statement += ' ' + hundreds[digits[0]]
        if (digits[1] != '1') and (digits[1] != '0'): # no zero or one in hundredths spot
            statement += ' ' + tens[digits[1]]
        elif digits[1] == '1':
            statement += ' ' + teens[digits[1:]] + ' ' + placement
            return statement
        if digits[2] != '0': #if hundredths
            statement += ' ' + ones[digits[2]] + ' ' + placement
            return statement
    if (len(digits) == 2) :
        if (digits[0] != '1') and (digits[0] != '0'):
            statement += ' ' + tens[digits[0]]
        elif digits[0] == '1':
            statement += ' ' + teens[digits] + ' ' + placement
            return statement
        if digits[1] != '0':
            statement += ' ' + ones[digits[1]] + ' ' + placement
            return statement
    if (len(digits) == 1):
        if digits != '0':
            statement += ' ' + ones[digits] + ' ' + placement
            return statement






def number_to_words (number):
    decimal = "" #just to declare it for now
    decimal_flag = False
    final_statement = '' # our desired output at the end
#print(number)
    if ',' in number: #if there are commas in there, take them out
        number = number.split(',')
        number = "".join(number)
    # print('Number before: ', number)
    if '.' in number: #if there is a decimal place
        decimal_flag = True
        x = number.split('.')
        number = x[0].lstrip('0').strip().lstrip('0')
        decimal = x[1].rstrip('0').strip().rstrip('0')
    # print(len(number))
    # print(len(decimal))
    while ( (len(number) == 0) and (len(decimal) == 0) ) or (len(number) > 15) or (len(decimal) > 3) \
    or ( (decimal_flag == True) and (len(decimal) == 0) ) or (re.search('\D+', number) != None) or (re.search('\D+', decimal) != None) :
    #     print(len(number))
        if number == "q":
            exit()
        number = input("Your entry is either blank, has too many or too few digits on at \
least one side of the decimal place, or has non-digits included. Please try again or enter q to quit: ")
        decimal = "" #just to declare it for now
        decimal_flag = False #is there a decimal place in the inputted number?
        final_statement = '' # our desired output at the end
    #print(number)
        if ',' in number: #if there are commas in there, take them out
            number = number.split(',')
            number = "".join(number)
        # print('Number before: ', number)
        if '.' in number: #if there is a decimal place
            decimal_flag = True #
            x = number.split('.')
            number = x[0].lstrip('0').strip().lstrip('0')
            decimal = x[1].rstrip('0').strip().rstrip('0')
    # print(len(number))
    # print('Number after splitting: ', number)
    # print('Number type: ', type(number))
    # print('Decimal after splitting: ', decimal)
    # print('Decimal type: ', type(decimal))
    #quit()
    if len(number) > 0:
        if number[0] == '-':
            final_statement += 'Negative'
            number = number[1:]

        number_of_places = str(math.ceil(len(number) / 3))
        offset = len(number) % 3 #to take into account the number of individual digits in the highest places three (333 million has zero, 3 million has one, 33 million has two)
        if offset == 0: #this helps for my convention below setting the start and stop indices
            offset = 3
        # print('number_of_places is :', number_of_places)
        # print('offset is :', offset)
        places_seen = 0 #how many three digit places we've seen (billions counts as one. billons and millions count as two. etc.)
        for pip in places_dict[number_of_places]:
            #print(pip)
            if places_seen == 0:
                start = 0
                stop = offset
            elif places_seen == 1:
                start = offset
                stop = start + 3
            elif places_seen > 1:
                start = (places_seen - 1) * 3 + offset
                stop = start + 3
            places_seen += 1
            # print('Start is :', start)
            # print('Stop is :', stop)
            # print(words_number(number[start:stop], pip))
            if ( words_number(number[start:stop], pip) != None ):
                final_statement += ' ' + words_number(number[start:stop], pip)
        final_statement = final_statement.strip(',')
        if number == '0':
            final_statement += 'zero'
    else:
        final_statement += 'zero'

    #Now take care of a decimal if there is one
    #print('Here :', decimal)
    if (decimal != ''):
        dec_statement = ' and ' + words_decimal(decimal).strip(',').strip()
        final_statement += dec_statement

    return final_statement.strip().capitalize().strip(',')

print(number_to_words(number = input('Input a number you\'d like spelled out that is less than one quadrillion and up to 3 decimal places, or enter q to quit: ').strip()))
