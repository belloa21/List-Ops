# Alex Bello
# 2/11/2020
# Applies different methods to a user generated list that do not modify the original list

from Methods import *


# Creating a blank list for a user to input into
ages = []
# This will do multiple things, have the user pick how many numbers they want for the list, the numbers they want in the
# list, and puts those numbers into the blank list
n = int(input("Please input how many numbers you want in this list, thanks! : "))
for i in range(0 , n):
    item = int(input("Enter number at location " + str(i) + " : "))
    ages.append(item)
print("Your list is", ages)

print("This is your list sorted least from greatest.")
ages.sort()
print(ages)

print("This is the sum of your list.")
print(sums(ages))

print("This is the product of the numbers in your list.")
print(product(ages))

print("Great we found the mean of your list.")
print(mean(ages))

print("Yes! This is the median of the list.")
print(median(ages))

print("Here's the most common number,or the mode, of the list.")
print(mode(ages))

print("What we have here is the lists smallest number.")
print(small_boi(ages))

print("What we have here is the lists largest number.")
print(big_boi(ages))

print("I've removed all the duplicates from the list, no need to thank me.")
print(removal(ages))

print("The list without the odd numbers in it.")
print(odd_times(ages))

print("The list without the even numbers in it.")
print(even_times(ages))

print(tell_me(ages))

print("Finally, the second largest number in the list.")
print(bonus(ages))



