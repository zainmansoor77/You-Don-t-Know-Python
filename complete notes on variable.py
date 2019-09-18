name = "Mark" # python variable is created this way.
print(name) # pyton displaying.

name = "Mark"
name = "Ace" # python could change the value inside the variable.
print(name)

floggle = "Mark" # instead of writing name = "Mark", floggle = "Mark" is also acceptable beacause python is blind to semantics
print(floggle)

thnx = "thanks for your input"
print(thnx)

weight=150 # unlike strings number is not enclosed is quotes
print(weight+25)

original_num = 23
num_to_be_added = 7
new_num = original_num + num_to_be_added  # python can do calculation totally based on variable
print(new_num)

original_num = 90
original_num = original_num + 10 # a variable can be used to calculate its own new value
print(original_num)

your_age = "twenty"
print(your_age)
your_age = 20 # A variable in python could change its type
print(your_age)

a,b=2,3
c = a*b
print(c)

whats_left_over = 10 % 3
print(whats_left_over )

age = 12
age += 50
print(age)

age = 12
age -= 2
print(age)

age = 12
age *= 3
print(age)

age = 12
amount_to_increment = 3
age += amount_to_increment
print(age)

left_over = 12 % 3
print(left_over )

x = 100
x += 3
x /= x
print(x)

total_cost = 1 + 3 * 4
print(total_cost)

result_of_computation = (2 * 4) * 4 + 2
print(result_of_computation)

greeting = "Hello"
addressee = "World"
whole_greeting = greeting + addressee # You tell Python to combine the two strings this way
print(whole_greeting)

greeting = "Hello"
separators = ", "
addressee = "World"
punc = "!"
whole_greeting = greeting + separators + addressee + punc
print(whole_greeting)

a,b,c = "a", "b", "c"
d = a + b + c
print(d)

first = 10
second = 15
print(first+second)

first = '100'
second = '150'
print(first + second)

first = 'Test '
second = 3
print(first * second)

message = 'And now for something completely different'
n = 17
pi = 3.1415926535897931
print(type(message))
print(type(n))
print(type(pi))

name = input('What is your name? ') # Before getting input from the user, it is a good idea to print a prompt telling the
# user what to input.
print(name)

minute = 45
percentage = (minute * 100) / 60 # compute the percentage of the hour
print(percentage)

a = "Hello, World!"
print(a[0])
print(a[5])

a = "Hello, World!"
print(a[0])
print(a[5])

a = "Hello, World!"
print(a[2:]) # this would print string from position 2 onward

b = " Hello, World!"
print(b.strip()) #strip() method removes any whitespaces from begning or from the end

a = "Hello, World!"
print(len(a)) # the len() method returns the length of a string

a = "Hello, World!"
print(a.lower()) # the lower method returns the string in lower case

a = "Hello, World!"
print(a.upper()) # the upper method returns the string in upper case

a = "Hello, World!"
print(a.replace("H","J")) # the replace method replaces a string with anotther string

s = "GREEKS FOR GREEKS"
t = "Greeks for Greeks"
u = "greeks for greeks"
print(s.isupper()) # isupper() functiopn is used to check if argument contain all upper case character
print(t.isupper()) # isupper() functiopn is used to check if argument contain all upper case character
print(u.isupper()) # isupper() functiopn is used to check if argument contain all upper case character

s = "GREEKS FOR GREEKS"
t = "Greeks for Greeks"
u = "greeks for greeks"
print(s.islower()) # islower() functiopn is used to check if argument contain all lower case character
print(t.islower()) # islower() functiopn is used to check if argument contain all lower case character
print(u.islower()) # islower() functiopn is used to check if argument contain all lower case character

x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x>3 and x<10)
print(x>3 or x<4)
print(not(x>3 and x<10))

x = ["apple" , "banana" , "cherry"]
y = ["apple" , "banana" , "cherry"]
z = x
print(x is z) # return true because x is same object as z
print(x is y) # return false because x is not the same object as y. Eventhough, they both have same content
print(x == z) # return true because both x and y got same elements
print(x is not z) # return false because x is same object as z
print(x is not y) # return true because x is not y

x = ["apple" , "banana"]
print("banana" in x) # returns true because  a sequence with the value "banana" is in the list
print("pineapple" not in x) # returns false because a sequence with the value "pineapple" is not in the list
