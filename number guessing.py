from random import randint, seed
from time import sleep
seed()

game_going = True
print('\n' + 'Welcome to Number Guessing!' + '\n')
while game_going:
    sleep(2)
    print('Alright, let\'s get started.')
    sleep(2)
    #getting the lower limit all set:
    print('\n' + 'Please enter the lower limit for this round of guessing, or enter q to quit: ')
    lower_limit = input()
    lower_limit_acceptable = False
    while lower_limit_acceptable == False:
        if (lower_limit.lower() == 'q'):
            sleep(2)
            print('\n' + 'Good-bye.')
            sleep(2)
            print('\n' + 'Feel free to stop by and play another round later.')
            sleep(2)
            quit()
        try:
            lower_limit = int(float(lower_limit)) #throw the float in there to handle any decimals from wise-guys
            lower_limit_acceptable = True
            sleep(1)
            print('\n' + 'That works! The lower limit is set at ', lower_limit, '. Moving on...', sep= '')
            continue
        except ValueError:
            sleep(1)
            print('Alright, enough messing around.')
            sleep(2)
            print('\n' + 'Please enter a number this time for the lower limit, or enter q to quit: ')
            lower_limit = input()
            continue #go back to line above that has: while lower_limit_acceptable == False
        # else:
        #     print('\n' + 'That works! Moving on...')

    #getting the upper limit all set
    sleep(2)
    print('\n' + 'Please enter the upper limit for this round of guessing, or enter q to quit: ')
    upper_limit = input()
    upper_limit_acceptable = False
    upper_limit_too_low_repeated = False #if there has already been an upper limit suggested that was below the lower limit
    while upper_limit_acceptable == False:
        if (upper_limit.lower() == 'q'):
            sleep(2)
            print('\n' + 'Good-bye.')
            sleep(2)
            print('\n' + 'Feel free to stop by and play another round later.')
            sleep(2)
            quit()
        try:
            upper_limit = int(float(upper_limit))#throw the float in there to handle any decimals from wise-guys

        except ValueError:
            sleep(1)
            print('You\'re making this harder than it has to be.')
            sleep(2)
            print('\n' + 'Please enter a number this time for the upper limit, or enter q to quit: ')
            upper_limit = input()
            continue #go back to line above that has: while lower_limit_acceptable == False
        if (upper_limit < lower_limit):
            sleep(1)
            print('\n' + 'Whoopsie daisy!')
            sleep(2)
            if (upper_limit_too_low_repeated == False):
                print('\n' + 'That upper limit of ', upper_limit, ' is below your lower limit of ', lower_limit, '.', sep= '')
            else:
                print('\n' + 'That upper limit of ', upper_limit, ' is still below your lower limit of ', lower_limit, '.', sep= '')
            sleep(2)
            upper_limit_too_low_repeated = True
            print('\n' + 'Please enter a higher number this time for the upper limit, or enter q to quit: ', sep= '')
            upper_limit = input()
            continue #go back to line above that has: while lower_limit_acceptable == False
        upper_limit_acceptable = True
        sleep(1)
        print('\n' + 'Good stuff. You\'re locked into an upper limit of ', upper_limit, '.', sep='')
        sleep(2)
        print('\n' + 'We\'re almost ready to start playing.')

    #getting the desired number of guesses set
    sleep(2)
    print('\n' + 'Please enter the number of guesses you would like to have, or enter q to quit: ')
    number_of_guesses_max = input()
    number_of_guesses_max_acceptable = False
    while number_of_guesses_max_acceptable == False:
        if (number_of_guesses_max.lower() == 'q'):
            sleep(2)
            print('\n' + 'Good-bye.')
            sleep(2)
            print('\n' + 'Feel free to stop by and play another round later.')
            sleep(2)
            quit()
        try:
            number_of_guesses_max = int(float(number_of_guesses_max))#throw the float in there to handle any decimals from wise-guys
        except ValueError:
            sleep(1)
            print('OK, I\'m wise to your tricks.')
            sleep(2)
            print('\n' + 'Please enter a number this time for the amount of guesses you\'d like, or enter q to quit: ')
            number_of_guesses_max = input()
            continue

        if number_of_guesses_max < 1:
            sleep(2)
            print('\n' + 'This time, please enter a positive amount of guesses that you\'d like that. 1 or higher will work fine: ')
            number_of_guesses_max = input()
            continue
        else:
            number_of_guesses_max_acceptable = True

        if number_of_guesses_max > (upper_limit - lower_limit):
            sleep(1)
            print('\n' + 'I\'m not sure you\'ll need all those guesses for this range, but we will proceed!')
        else:
            sleep(2)
            print('\n' + 'Excellent, let\'s get to the guessing.')

    #set target
    target_acceptable = False
    while target_acceptable == False:
        target = randint(lower_limit, upper_limit)
        # print('TARGET IS: ', target)
        target_acceptable = True
    sleep(1)
    print('\n' + 'Very good. The number you\'re trying to guess could be ', lower_limit, ', ', upper_limit, ', or anything in between.', sep='')
    if (upper_limit == lower_limit):
        sleep(2)
        print('\n' + 'However, something tells me that this will not be too difficult for you.')

    #get to guessing
    number_of_guesses_remaining = number_of_guesses_max
    dct_of_guesses = {}
    while number_of_guesses_remaining > 0:
        if number_of_guesses_remaining > 1:
            sleep(2)
            print('\n' + 'You currently have', number_of_guesses_remaining, 'guesses remaining.')
        if (number_of_guesses_remaining == number_of_guesses_max) and (number_of_guesses_remaining == 1): # if this is their first and only guess
            sleep(2)
            print('\n' + 'Alright, hotspot, let\'s see if you can get a hole-in-one here.')
            sleep(2)
            print('\n' + 'What is your first and only guess?')
        elif (number_of_guesses_remaining == number_of_guesses_max): #if this is the first guess but not also their only guess
            sleep(2)
            print('\n' + 'What is your first guess? Enter q to quit.')
        elif (number_of_guesses_remaining == 1): #if this is the last available guess but not also their first
            sleep(1)
            print('\n' + 'You have one guess remaining.')
            sleep(2)
            print('You better make it good!')
            sleep(2)
            print('\n' + 'What is your final, ultimate, last guess? Also, you can enter history to review previous guess, or enter q to quit.')
        else: #if this is not the first or last guess
            sleep(2)
            print('\n' + 'Enter your next guess or enter history to see the previous guesses. Or you can enter q to quit.')
        guess= input()
        guess_acceptable = False
        while guess_acceptable == False:
            if guess == 'q':
                sleep(2)
                print('\n' + 'Good-bye. I thought the game was going well but you have to do what you have to do.')
                sleep(2)
                print('\n' + 'Feel free to stop by and play another round later.')
                sleep(2)
                quit()
            if (guess == 'history') and (len(dct_of_guesses)) > 0: #if the user requests history and there is a history
                sleep(2)
                print('\n' + 'No problem. Get ready; here are your guesses so far:')
                sleep(1.75)
                for entry in dct_of_guesses:
                    # print('Entry: ', entry)
                    # print('type of entry: ', type(entry))
                    # print('dct_key[entry] :', dct_of_guesses[entry])
                    sleep(0.25)
                    print('\n', 'Guess number ', entry, ' of ', dct_of_guesses[entry][0], ' was ', dct_of_guesses[entry][1], sep='')
                sleep(2)
                print('\n' + 'Please enter a number this time for your guess, or enter q to quit: ')
                guess = input()
                continue #go back to line above that has: while guess_acceptable == False
            try:
                guess = int(float(guess))#throw the float in there to handle any decimals from wise-guys
                guess_acceptable = True
                continue
            except ValueError:
                sleep(1)
                print('\n' + 'Get it together, sillyhead.')
                sleep(2)
                print('\n' + 'Please enter a number this time for your guess, or enter q to quit: ')
                guess = input()
                continue #go back to line above that has: while guess_acceptable == False
        number_of_guesses_remaining -= 1
        # print('\n' + 'guess is ', guess, ' and target is ', target)

        #if the guess is not correct:
        miss_type = '' #just to declare it for now
        if guess > target:
            miss_type = 'too high'
            dct_key = number_of_guesses_max - number_of_guesses_remaining #1 for the first guess, 2 for the second guess, etc.
            dct_of_guesses[dct_key] = [guess, miss_type]
            sleep(1)
            print('\n' + 'Not correct. Your guess of ', guess, ' was ', miss_type, '.', sep='')
            # print('dictionary is: ', dct_of_guesses)
            continue #get to next guess
        elif guess < target:
            miss_type = 'too low'
            dct_key = number_of_guesses_max - number_of_guesses_remaining #1 for the first guess, 2 for the second guess, etc.
            dct_of_guesses[dct_key] = [guess, miss_type]
            sleep(1)
            print('Not correct. Your guess of ', guess, ' was ', miss_type, '.', sep='')
            # print('dictionary is: ', dct_of_guesses)
            continue #get to next guess

        #if the guess is correct:
        if guess == target:
            sleep(2)
            statement = '\n' + 'That\'s right, it was ' + str(target) + '.'
            if (number_of_guesses_remaining == 0) and (number_of_guesses_max == 1):
                statement += '\n' + ' And you got it on your first and only guess!'
            elif (number_of_guesses_remaining == 0):
                statement += '\n' + 'And you got it on your last guess!'
            elif (number_of_guesses_max - number_of_guesses_remaining) == 1:
                statement += '\nAnd you got it on your first guess!'
            for num in range(1,6):
                x = '.' * num
                print(x)
                sleep(1)

            print(statement)
            number_of_guesses_remaining = 0 #just so for sure we get out of this current while loop since the correct answer was found
            again_acceptable = False
            sleep(2)
            print('\n' + 'Would you like to play again? Press y for yes or n for no, or q to quit.')
            again = input().lower()
            while again_acceptable == False:
                if (again == 'y'):
                    sleep(1)
                    print('\n' + 'OK, here we go for another round...')
                    again_acceptable = True
                elif (again =='n') or (again == 'q'):
                    sleep(2)
                    print('\n' + 'Good-bye.')
                    sleep(2)
                    print('\n' + 'Feel free to stop by and play another round later.')
                    sleep(2)
                    quit()
                else:
                    print('\n' + 'This time, please enter y for yes to another round, n for no to another round, or q to quit.')
                    again = input().lower()

    #if the player loses
    if (number_of_guesses_remaining == 0) and (guess != target): #out of guesses and did not get it right on the last guess
        sleep(1)
        print('\n' + 'Bummer, you\'re out of guesses. Better luck next time. The correct answer was ', target, '.', sep='')
        again_acceptable = False
        sleep(2)
        print('\n' + 'Would you like to play again? Press y for yes or n for no, or q to quit.')
        again = input().lower()
        while again_acceptable == False:
            if (again == 'y'):
                print('\n' + 'OK, here we go for another round.')
                again_acceptable = True
            elif (again =='n') or (again == 'q'):
                sleep(2)
                print('\n' + 'Good-bye.')
                sleep(2)
                print('\n' + 'Feel free to stop by and play another round later.')
                sleep(2)
                quit()
            else:
                sleep(2)
                print('\n' + 'This time, please enter y for yes to another round, n for no to another round, or q to quit.')
                again = input().lower()
