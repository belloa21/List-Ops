#Alex Bello
#2/11/2020
#Applies different methods to a user generated list that do not modify the original list

from Methods import *


#Creating a blank list for a user to input into
ages = []
#This will do multiple things, have the user pick how many numbers they want for the list, the numbers they want in the
#list, and puts those numbers into the blank list
n = int(input("Please input how many numbers you want in this list, thanks! : "))
for i in range(0 , n):
    item = int(input("Enter number at location " + str(i) + " : "))
    ages.append(item)
print("Your list is", ages)
ages.sort()
print(ages)
print(sums(ages))
print(product(ages))
print(mean(ages))
print(median(ages))
print(mode(ages))
print(small_boi(ages))
print(big_boi(ages))
print(removal(ages))
print(odd_times(ages))
print(even_times(ages))
print(tell_me(ages))
print(bonus(ages))



