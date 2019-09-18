a = "Hello, World!"
print(a[0])
print(a[5])

a = "Hello, World!"
print(a[2:5])

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
