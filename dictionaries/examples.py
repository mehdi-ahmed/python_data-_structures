purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissue'] = 75

print(purse)  # {'money': 12, 'candy': 3, 'tissue': 75}
print(purse['money'])  # 12

dictionary = {'Mehdi': 39, 'Svetlana': 33, 'Jan': 100}
print(dictionary)

# Counting with Dictionaries
print('----------------------')
counts = dict()
names = ['csev', 'cwen', 'csev', 'zquen', 'cwen']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1

print(counts)  # {'csev': 2, 'cwen': 2, 'zquen': 1}

#  Dictionaries and Files
print('----------------------')
d = {'Mehdi': 39, 'Svetlana': 33, 'Jan': 100}
# Retrieve list of keys
print(list(d))  # ['Mehdi', 'Svetlana', 'Jan']

# Retrieve list of values
print(d.values())  # dict_values([39, 33, 100])

# Retrieve both
print(d.items())  # dict_items([('Mehdi', 39), ('Svetlana', 33), ('Jan', 100)]) : Tuples

# For loop with two iteration variables

for i, j in d.items():
    print(i, j)

# Mehdi 39
# Svetlana 33
# Jan 100