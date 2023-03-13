bday = input('Enter your birthday in 8 digits: ')
sum = 0
for digit in bday: 
    sum += int(digit) #sum up the digits a first time
#print('first sum is: ', sum)

while len(str(sum)) > 1: # now iterate through until down to a single digit
    #print('start new iteration of while loop.')
    sum_new = 0 #new dummy sum_new gets set to zero at the start of each while loop iteration
    for digit in str(sum):
        sum_new += int(digit)
        #print('sum_new is: ', sum_new)
    sum = sum_new
print('Your digit of life is: ',sum)