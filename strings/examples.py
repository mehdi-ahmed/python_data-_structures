str1 = 'hello'
str2 = "there"
greetings = str1 + " " + str2
print(greetings)

# Example 1
fruit = 'banana'
letter = fruit[1]
print(letter)  # a

# Length function
print('------------------')
size = len(fruit)
print(size)  # 6

# Looping through Strings
print('------------------')
fruit = "Mongo"
for letter in fruit:
    print(letter)

# Slicing Strings - doesn't include the last letter corresponding to the index
print('------------------')
s = 'Monty Python'
print(s[1:4])  # ont
print(s[6:9])  # Pyt
print(s[6:20])  # Python
print(s[4:])  # y Python
print(s[:3])  # Mon

# Using logical operations
print('------------------')
fruit = 'Orange'
print('O' in fruit)  # True
print('Z' in fruit)  # False

# Built in function
random_string = 'this is in lower case'
print(random_string.upper())  # THIS IS IN LOWER CASE
print(type(random_string))  # <class 'str'>

# Find: Returns index
pos = random_string.find('lower')
print(pos)  # 11
pos = random_string.find('not')
print(pos)  # -1

# Search and Replace
greet = 'Hello Mehdi Ahmed'
new_str = greet.replace('Ahmed', 'Ammar')
new_str2 = greet.replace('A', 'X')
print(new_str)  # Hello Mehdi Ammar
print(new_str2)  # Hello Mehdi Xhmed

# Stripping white space
greet = 'Hello Mehdi     '
print(greet.strip())  # Hello Mehdi

# Prefixes
greets = 'Please let let me know'
print(greets.startswith('Please'))  # True
print(greets.startswith('Please!'))  # False
