def palindrome_checker():
    text = input('Enter some text to see if it is a palindrome: ').lower() #use lower to standardize all upper and lower case so differences in case will be ignored
    #text = 'A man a plan a canal Panama'.lower()
    text_lst = [] #create empty list that will used to store individual characters of text
    reversed_lst = [] #empty lst of reversed text to compare with text
    for char in text:
        if not char.isspace(): #if the character is not whitespace
            text_lst.append(char) #add characters to the text_lst
            reversed_lst.insert(0, char) #So it's reversed compared to text_lst. Insert method can only be used on lists (not strings!)

    if text_lst == reversed_lst:
        return "It's a palindrome."
    else:
        return "It's not a palindrome."

print(palindrome_checker())
