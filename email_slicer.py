import re #import regular expressions to be able to check the from of the entered email addresses

#regex search function stops after finding the leftmost match, which works for this because I only need one iteration/possibility to be true
# for abc@123.com, finding only 1 match is fine. I don't the many matches c@123.c, bc@123.co, etc
""" testing:
x = "abc@123123.com"
print(re.search('.+@.+\..+', x))
searching for 1 or more of any characters (.+) then an @ sign (@) then 1 or more of any characters (.+)
then a period (\.) then 1 or more of any characters (.+)"""


address = input("Please put in your email address or enter q to quit: ").strip()
if address.lower() == "q":
    exit()
while re.search('.+@.+\..+', address) == None:
    if address.lower() == "q":
        exit()
    address = input("Please put in a proper email address this time or enter q to quit: ")

username = [] #empty list to be appended into
domain = [] #empty list to be appended into
#print('Address is ', address)
flag = 1 #this flag will be used to keep track of which part of the address we're in: username or domain (which side of the '@' were on)
for elem in address:
        if (elem != '@') and (flag == 1): #if we are in the username still
            username.append(elem)
            #print('Element is ', elem, 'and username is ', username)
        elif (elem == '@') and (flag == 1):
            flag += 1
        elif (flag > 1):
            domain.append(elem)
            #print('Element is ', elem, 'and domain is ', domain)
#print('got here')
username = ''.join(username)
domain = ''.join(domain)
print('The username is', username)
print('The domain is', domain)

"""
#alternate way I found online for doing it more quickly:
email = input('Enter your email: ').strip()
username = email[:email.index('@')] #from beginning to @
domain = email[email.index('@') + 1:] #from the element after @ until the end
print(f'Your username is {username} & domain is {domain}')
"""
