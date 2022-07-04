num1 = 42   #varibale declaration, int (whole Nnumber)
num2 = 2.3  #variable declaration, flat (decimal number)
boolean = True  #variable declaration, #boolean (True || False) uppercase First letter
string = 'Hello World'  #variable declaration, string ('single' or "double" quotes, but recommend  either and not both )
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #variable declaration, initialize list (list is muatable just like array) 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}      #variable declaration, initialize dictionary 
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration tuple (data types that cannot be modified)
print(type(fruit))  # logs || Outputs, type of fruit object-  prints tuple
print(pizza_toppings[1])    #   log, accesses value of list at index 1
pizza_toppings.append('Mushrooms')  # adds vaule to the end of the list
print(person['name'])    # log, accesses the dictionary person and logs the value associated with the key 'name'
person['name'] = 'George' # change the value 'name' in the dictionary 'person' to 'George'
person['eye_color'] = 'blue'    # adds key 'eye_color' in the dictionary 'person' value to 'blue'
print(fruit[2])     # log, the second index of tulpe 'fruit'

if num1 > 45:               # conditional, if 
    print("It's greater")   # log, "It's greater"
else:                       # conditional, else
    print("It's lower")     #log, "it's lower"

if len(string) < 5:             # conditional, if /  the length of string less than 5
    print("It's a short word!") # log
elif len(string) > 15:          # conditional, else if /  the length of string  greater than 15 
    print("It's a long word!")  # log
else:                           #  conditional, else /
    print("Just right!")        # log

for x in range(5):              # for loop, start from 0-4  
    print(x)                    # log
for x in range(2,5):            # for loop, start from  2 - 4
    print(x)                    # log
for x in range(2,10,3):         # for loop, start from 2 - 9 by 3s
    print(x)                    # log
x = 0                           # variable declaration int 
while(x < 5):                   # while loop start from x til its greater than or equal to 5
    print(x)                    # log
    x += 1                      # increment x + 1

pizza_toppings.pop()            # removes last value from list
pizza_toppings.pop(1)           # removes index value 1 from list

print(person)                   # log
person.pop('eye_color')         # removes key:value pair from the dictionary
print(person)                   # log

for topping in pizza_toppings:  # starts for loop through each index of list
    if topping == 'Pepperoni':  # conditional if, 
        continue                # continues to next iteration
    print('After 1st if statement')     #log
    if topping == 'Olives':     # condtional if,
        break                   #breaks out of for loop once meet

def print_hello_ten_times():    # creates function() 
    for num in range(10):       #  for loop starting from 0-9
        print('Hello')          # log

print_hello_ten_times()         # invokes function()

def print_hello_x_times(x):     # creates a function() with a parameter 
    for num in range(x):        # for loop 
        print('Hello')          # log

print_hello_x_times(4)          # invokes function() that has an agrument 4 

def print_hello_x_or_ten_times(x = 10):     # create function() with parameter variable declaration
    for num in range(x):                    # for loop  starts from 0-9
        print('Hello')                      # log

print_hello_x_or_ten_times()                # invokes function()
print_hello_x_or_ten_times(4)               # invokes function() with arguement 4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)