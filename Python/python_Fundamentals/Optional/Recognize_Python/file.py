num1 = 42  # variable declaration , integer type 
num2 = 2.3 # variable declaration , float type
boolean = True # variable declaration , boolean type
string = 'Hello World' # variable declaration , string type
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration , list type
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration , dictionary type
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration , tuple type
print(type(fruit)) # print the type of the variable fruit
print(pizza_toppings[1]) # print the value of the index 1 of the variable pizza_toppings
pizza_toppings.append('Mushrooms') # add the value 'Mushrooms' to the variable pizza_toppings
print(person['name']) # print the value of the key 'name' of the variable person
person['name'] = 'George' # change the value of the key 'name' of the variable person to 'George'
person['eye_color'] = 'blue'    # add the key 'eye_color' with the value 'blue' to the variable person
print(fruit[2]) # print the value of the index 2 of the variable fruit

if num1 > 45: # if statement
    print("It's greater") # print the string
else: # else statement
    print("It's lower") # print the string

if len(string) < 5: # if statement
    print("It's a short word!") # print the string
elif len(string) > 15: # else if statement
    print("It's a long word!") # print the string
else: # else statement
    print("Just right!") # print the string

for x in range(5): # for loop
    print(x) # print the value of x
for x in range(2,5): # for loop
    print(x) # print the value of x
for x in range(2,10,3): # for loop
    print(x) # print the value of x
x = 0 # variable declaration , integer type
while(x < 5): # while loop 
    print(x) # print the value of x
    x += 1 # increment the value of x

pizza_toppings.pop() # remove the last value of the variable pizza_toppings
pizza_toppings.pop(1) # remove the value of the index 1 of the variable pizza_toppings

print(person) # print the variable person
person.pop('eye_color') # remove the key 'eye_color' of the variable person
print(person) # print the variable person

for topping in pizza_toppings:  # for loop 
    if topping == 'Pepperoni':  # if statement
        continue    # continue statement
    print('After 1st if statement') # print the string
    if topping == 'Olives':     
        break   # break statement

def print_hello_ten_times():    # function declaration
    for num in range(10):   # for loop
        print('Hello') # print the string

print_hello_ten_times() # call the function print_hello_ten_times

def print_hello_x_times(x):   # function declaration
    for num in range(x):  # for loop
        print('Hello') # print the string

print_hello_x_times(4)  # call the function print_hello_x_times with the argument 4

def print_hello_x_or_ten_times(x = 10): # function declaration
    for num in range(x): # for loop
        print('Hello')  # print the string

print_hello_x_or_ten_times()    # call the function print_hello_x_or_ten_times
print_hello_x_or_ten_times(4)  # call the function print_hello_x_or_ten_times with the argument 4


"""
Bonus section
"""

print(num3)  # NameError: name <variable name> is not defined
num3 = 72 # variable declaration , integer type
fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
print(person['favorite_team'])  # KeyError: 'favorite_team'
print(pizza_toppings[7])   # IndexError: list index out of range
print(boolean) # print the value of the variable boolean
fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'