text = input('Provide a line of text to encrypt: ')
flag = False # dummy variable to allow while loop to continue until acceptable value is given
while flag == False:
    shift_value = input('Input a shift value between 1 and 25, or enter -1 to quit: ')
    # print(shift_value)
    # print(type(shift_value))
    try:
        shift_value = int(shift_value)
    except:
        print('Please enter either a number between 1 and 25, or enter -1 to quit.')
        continue #to go directly to the beginning of the while loop again
    if shift_value == -1:
        print('This program has been ended.')
        quit()
    elif shift_value > 25 or shift_value < 1:
        print("Please keep your entry above 0 and below 26, or enter -1 to quit.")
        continue #to go directly to the beginning of the while loop again
    else:
        flag = True # can change the dummy variable to exit the while loop when acceptable number is given

text_ciphered = ''
for char in text:
    if not char.isalpha():
        text_ciphered += char #put the character in as it was if it is not an alphabet char
        continue # go to next character

    if char.isupper(): #for only uppercase letters
        code = ord(char) + shift_value #make the shift in the ASCII table index
        if code > 90: # if the shift took it past Z on the ASCII table
            code = code - 26
    else: #for only lowercase letters:
        code = ord(char) + shift_value #make the shift
        if code > 122: # if the shift took it past z on the ASCII table
            code = code - 26
    text_ciphered += chr(code) #transfer back from ASCII index to a character and add to ciphered text

print(text_ciphered)
