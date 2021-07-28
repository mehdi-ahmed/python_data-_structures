friends = ["Aymen", "Mokhtar", "Francisco", "Yuri"]

#  Strings are immutable - We cannot change the content, we must create a new String
#  Lists are mutable - we can change an element of the list using index

print(friends)
friends[2] = 'Jaime'
print(friends)

# Size with len() - Works with Strings too
print(len(friends))  # 4

# Range - Returns a list of numbers that range from zero to one less than the parameter
print(range(4))

# Loops
for friend in friends:
    print('hey', friend)
print('-----------------')
for i in range(len(friends)):
    friend = friends[i]
    print(friend)

# Lists can be sliced - Up to but not including
print('-----------------')
t = [1, 3, 99, 54, 77, 12, 46]
print(t[1:3])  # [3, 99]
print(t[:5])  # [1, 3, 99, 54, 77]
print(t[5:])  # [12, 46]
print(t[:])  # [1, 3, 99, 54, 77, 12, 46]
print(t[2:3])  # [99]

print('-----------------')
x = list()
print(dir(x))

#  You can add elements with append()
# Order is respected, new elements appended are placed at the end
print('-----------------')
stuff = list()
stuff.append(-7777)
stuff.append('book')

print(stuff)  # [-7777, 'book']

# element in ?
print('-----------------')
print('book' in stuff)  # True

# Other functions len(), max(), min(), sum(), split()
# Examples:
# split() : Breaks a String into multiples items based on space by default
print('-----------------')
abc = 'One two Three'
stuff = abc.split()
print(stuff)  # ['One', 'two', 'Three']
dce = 'One,two,Three'
stuff = abc.split(',')
print(stuff)  # ['One two Three']
