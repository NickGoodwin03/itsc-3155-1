# Nick Goodwin
 
# Program 1
# Write a Python program that receives a string and returns a new string 
# with the first 2 and the last 2 chars from a given string. 
# If the string length is less than 2, print out an appropriate message to the user.

from argparse import HelpFormatter


print("Program 1: \n")
def string_both_ends(str):
    if len(str) < 2:
        return 'Your string is too short'
    return str[0:2] + str[-2:]

string = input("Enter your string: ")
stringToReturn = string_both_ends(string)
print(stringToReturn)

# Program 2
# Write a Python program that will find all numbers between 
# two given numbers divisible by 7 but not a multiple of 5.

print("Program 2: \n")
def numbers_five_seven(int1, int2):
    if int1 < int2:
        nums = range(int1, int2)
    else:
        nums = range(int2, int1)
    for n in nums:
        if n % 7 == 0:
            if n % 5 != 0:
                print(n)

int1 = input("Enter your first number: ")
int2 = input("Enter your second number: ")
numbers_five_seven(int(int1), int(int2))

# Program 3
# Write a Python program that receives two dictionaries and 
# combine them by adding values for common keys.

dict1 = {
    'a':100,
    'b':200,
    'c':300,
    'e':800
}
dict2 = {
    'a':300,
    'b':200,
    'd':400,
    'g':600
}
def combine_dicts(dict1, dict2):
    for k in dict2:
        if k in dict1:
            dict2[k]=dict2[k]+dict1[k]
        else:
            pass
    for k in dict1:
        if k in dict2:
            pass
        else:
            dict2[k]=dict1[k]
    print(dict2)

    

combine_dicts(dict1, dict2)

# Program 4
# Write a Python program which receives a number of items in an invoice 
# then asks for input the items (item name and price). 
# Item and price will be separated by a space, and each item should be entered in a separate line. 
# Print out the invoice item and price order by their price.
class Item(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price and self.name == other.name

    def __lt__(self, other):
        return self.price < other.price


def invoice(num_items):
    num_items = int(num_items)
    items=[]
    x=0
    
    while x < num_items:
        input_item = input("Enter an item and its price seperated by a space: ")
        item_values = input_item.split(" ")
        item = Item(name=item_values[0], price=item_values[1])
        items.append(item)

        x += 1

    items_sorted = sorted(items)
    items_sorted_order = [i for i in items_sorted]
    for i in items_sorted_order:
        print(i.name, i.price)
    
        
    
        
        
    #price = invoice_dict.values()
    #price = price.sort()
    #print(price)    
invoice(input("Enter the number of items in the invoice: "))

