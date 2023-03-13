import re #import regular expressions to check input format
from time import sleep
def dmg_calc():
    sleep(1)
    print('\n' + 'Hello, fellow nerd.')
    sleep(2)
    print('\n' + 'This program can provide the maximum and average damage amounts for D&D damage sources.')
    sleep(4)
    print('\n' + 'All that is needed from you is to input the damage amount(s) and type(s) of the source.')
    sleep(4)
    print('\n' + 'An example of this is: 1d6, 1d4 fire, 1d6+2 cold')
    sleep(3)
    print('\n' + 'Enter the damage with base damage first, with different damage types separated by a comma: ')
    sleep(4)
    print('\n' + 'If the first damage type is not specified, it\'ll be labeled as base damage.')
    sleep(4)
    print('\n' + 'Are you ready? Please enter your damage amount(s) and type(s), or enter q to quit:')
    dmg_input = input().lower() #get an initial attempt at an input
    #now lets dig into the input
    dmg_input_acceptable = False
    while dmg_input_acceptable == False:
        if dmg_input == 'q':
            sleep(2)
            print('\n' + 'Good-bye, fellow nerd.')
            sleep(2)
            quit()
        elif (dmg_input == '') or (dmg_input == '\s'):
            sleep(1)
            print('\n' + 'There\'s not much I can do with that input.')
            sleep(2)
            print('\n' + 'Please re-enter your damage information or enter q to quit:')
            dmg_input = input().lower()
            continue #get back to beginning of while loop
        else:
            dmg_lst = dmg_input.split(',')# separate the damage types into list elements
            dmg_lst_clean = []
            problem = False #this will flag if any of the items in dmg_lst are found to be bad in the following for loop
            entry_count = 0 #just to differentiate the first, base damage entry from other entries
            for dmg_entry in dmg_lst:
                dmg_entry_new = dmg_entry[:].strip() #create a new variable that will be added to a new list. This entry cannot be modified such that its entry into the list it is already in can be changed.
                if (dmg_entry_new == ''): #if there was nothing other than whitespace or there is nothing at all
                    sleep(2)
                    print('\n' + 'Yikes, at least one of those damage entries is entries is blank.')
                    sleep(2)
                    print('\n' + 'Please re-enter your damage information or enter q to quit:')
                    dmg_input = input().lower()
                    problem = True
                    break #get back to beginning of while loop. continue would just take us to the next iteration of the for loop
                if (dmg_entry_new.count('+') + dmg_entry_new.count('-') > 1): #if there is more than one + or - combined in the entry
                    sleep(2)
                    print('\n' + 'Oops, we have too many operation signs for at least one damage type in there.')
                    sleep(2)
                    print('\n' + 'Please re-enter your damage information or enter q to quit:')
                    dmg_input = input().lower()
                    problem = True
                    break #get back to beginning of while loop. continue would just take us to the next iteration of the for loop
                if (re.search('[a-z]+$', dmg_entry_new) == None) and (entry_count != 0): #if a non-base damage entry is not specified for type of damage
                    sleep(2)
                    print('\n' + 'Please add in damage descriptors for all non-base damage entries. It is optional for the base damage entry.')
                    sleep(2)
                    print('\n' + 'Please re-enter your damage information or enter q to quit:')
                    dmg_input = input().lower()
                    problem = True
                    break
                #needs to remove all spaces BEFORE either the last number or the first letter in the last letter sequence in the dmg_entry to accommodate multi-word damage types like magical fire (not remove that last space)
                #need to take rindex instead of index so the rightmost '1' is taken in a case like 1d6+1
                needed_index = dmg_entry_new.rindex((re.findall('\d+', dmg_entry_new)[-1])) + len((re.findall('\d+', dmg_entry_new)[-1])) #find the index right after the last number match
                dmg_entry_new = dmg_entry_new[:needed_index + 1].replace(' ', '') + dmg_entry_new[needed_index + len((re.findall('\d', dmg_entry_new)[-1])):] #add the +1 in case there is no original space between the last number and the descriptor like '1d4fire' instead of '1d4 fire'
                #now check for the general formats fitting the following: 111d666/111d666fire/111d666mag fire, 111d666+111/111d666+111fire, 111d666-111/111d666-111fire
                if ( re.search('^\d+d\d+[a-z]*', dmg_entry_new) == None) and (re.search('^\d+d\d+\+\d+[a-z]*', dmg_entry_new) == None) and ( re.search('^\d+d\d+-\d+[a-z]*', dmg_entry_new) == None):
                    sleep(2)
                    print('\n' + 'Oops, we have at least one damage type format that doesn\'t work in there.')
                    sleep(2)
                    print('\n' + 'Please re-enter your damage information or enter q to quit:')
                    dmg_input = input().lower()
                    problem = True
                    break #get back to beginning of while loop
                else:
                    dmg_lst_clean.append(dmg_entry_new)
                    entry_count += 1
            if problem == True:
                continue #if there was a issue with any entries during the for loop stuff, go back to the while loop's start
            dmg_input_acceptable = True #change the variable for the while loop after the for loop is completed successfully without a problem
            sleep(1)
            print('\n' + 'Nice, I can work with this.')
            break #move on past the while loop for dmg_input_acceptable
    #now to dissect the damage types and organize the information in each
    dmg_dct = {}
    if (re.search("[a-z]+$", dmg_lst_clean[0]) == None): #if base damage type is not specified
        dmg_lst_clean[0] += 'base'

    bonus_penalty = 0 #reset an assignment of + damage or - dmg_type_damage
    count = -1 #keep count for index of damage entry
    for entry in dmg_lst_clean:
        print(entry)
        count += 1
        dice_quantity = re.findall('^\d+', entry)[0] #find the number of dice rolled at the beginning of the entry
        index_a = len(dice_quantity) + 1 #starting entry at this index will start at the dice type now (right of the dice 'd')
        dice_type = re.findall('\d+', entry)[1] #find the type of die, which is the die's max roll
        if ('+' in entry):
            x = entry.index('+') + 1 #to get index of number after the bonus/penalty sign
            bonus_penalty = int( re.findall('^\d+', entry[x:])[0] )
        elif ('-' in entry):
            x = entry.index('-') + 1
            bonus_penalty = int( re.findall('^\d+', entry[x:])[0] ) * (-1)
        else:
            bonus_penalty = 0
        descriptor_index = entry.rindex(re.findall('\d', entry)[-1]) + 1 #take the index of the character after the last number before the damage type desciption. Need rindex instead of index to get the rightmost 5 in case like 5d8+5
        descriptor = entry[descriptor_index:]
        print(re.findall('\d', entry))
        print(entry[descriptor_index])
        # print('entry is ', entry, 'and dice_quantity is ', dice_quantity, 'and dice_type is', dice_type, 'and bonus/penalty is', bonus_penalty, 'and descriptor is ', descriptor)
        dmg_dct[count] = [dice_quantity, dice_type, bonus_penalty, descriptor]
    print(dmg_dct)
    #now work out max and average damages
    max_dmg = 0
    max_dmg_statement_total = ''
    max_dmg_statement_ind = ''
    avg_dmg = 0
    avg_dmg_statement_total = ''
    avg_dmg_statement_ind = ''
    for entry in dmg_dct:
        max_dmg_ind = ( int(dmg_dct[entry][0]) * int(dmg_dct[entry][1]) ) + int(dmg_dct[entry][2]) #max damage of this damage entry type is dice quantity x dice type + bonus_penalty
        max_dmg += max_dmg_ind
        avg_dmg_ind = ( (int(dmg_dct[entry][1]) + 1) * int(dmg_dct[entry][0]) * 0.5 ) + int(dmg_dct[entry][2]) #avg damage of this type is (dice type + 1) * dice quantity * 0.5 + bonus_penalty
        avg_dmg += avg_dmg_ind
        max_dmg_statement_ind += ' The maximum ' + dmg_dct[entry][3] + ' damage is ' + str(max_dmg_ind) + '.'
        avg_dmg_statement_ind += ' The average ' + dmg_dct[entry][3] + ' damage is ' + str(avg_dmg_ind) + '.'
    max_dmg_statement_total += '\n' + '\n' + 'The maximum total damage is ' + str(max_dmg) + '.' + max_dmg_statement_ind
    avg_dmg_statement_total += '\n' + '\n' + 'The average total damage is ' + str(avg_dmg) + '.' + avg_dmg_statement_ind

    final_statement = max_dmg_statement_total + '\n' + avg_dmg_statement_total
    sleep(2)
    return final_statement

print(dmg_calc())
