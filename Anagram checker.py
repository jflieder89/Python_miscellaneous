first_text = input('Enter text for comparison: ').lower() #use lower method to unify lower and upper case
second_text = input('Enter another text for comparison: ').lower()

first_text = first_text.strip() #to remove whitespace characters
second_text = second_text.strip()

first_lst = [] #create empty lists that characters will be put into, to be later sorted
second_lst = []

for char in first_text:
    first_lst.append(char) #put all the characters of an entry individually into a list
for char in second_text:
    second_lst.append(char)

first_lst.sort() #use sort method to get in alphabetical order. No need to x = x.sort(); just do x.sort()
second_lst.sort()

if first_lst == second_lst:
    print('These two are anagrams.')
else:
    print('These two are not anagrams.')
