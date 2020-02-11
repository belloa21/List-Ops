#Alex Bello
#2/11/2020
#Applies different methods to a user generated list that do not modify the original list

import collections


#Creating a blank list for a user to input into
ages = []
#This will do multiple things, have the user pick how many numbers they want for the list, the numbers they want in the
#list, and puts those numbers into the blank list
n = int(input("Please input how many numbers you want in this list, thanks! :"))
for i in range(0 , n):
    print("Enter number at location", i, ":")
    item = int(input())
    ages.append(item)
print("Your list is", ages)

sorted(ages)
ages





