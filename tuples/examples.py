x = ('Mehdi', 'Khaled', 'Leila', 'Amira')
print(x[2])  # Leila

y = (1, 2, 3)
print(y)  # (1, 2, 3)

# Lists are Mutable, Tuples are Immutable

z = [86, 96, 77]
z[0] = -777
print(z)  # [-777, 96, 77]

t = (55, 99, 66)
# t[0] = -777  # TypeError: 'tuple' object does not support item assignment

# Other examples
(x, y) = (4, 'ABC')
print(y)  # ABC

# Tuples in dictionaries
d = dict()
d['csev'] = 2
d['cwen'] = 4

for (k, v) in d.items():
    print(k, v)

# csev 2
# cwen 4

# Tuples comparison - Compares first numbers, and so on..
var = (1, 2, 1000) > (0, 5555555, 999999)
print(var)  # True

var2 = ('Mehdi', 'Ammar') < ('Mehdi', 'Ahmed')
print(var2)  # False M is greater than H

# Sorting tuples - Sorted by keys !!
print('--------------')
t = {'a': 14, 'c': 89, 'b': 65}
print(t.items())  # dict_items([('a', 14), ('c', 89), ('b', 65)])
print(sorted(t.items()))  # [('a', 14), ('b', 65), ('c', 89)]

#  Sorting by Value - We construct a list of tuples, we could sort by value
print('--------------')
c = {'a': 22, 'b': 11, 'c': '99'}
tmp = list()

for k, v in c.items():
    tmp.append((v, k))  # we reverse the value key

print(tmp)  # [(22, 'a'), (11, 'b'), ('99', 'c')]
tmp = sorted(tmp, reverse=True)
# print(tmp)  # [(22, 'a'), (11, 'b'), ('99', 'c')] TypeError: '<' not supported between instances of 'str' and 'int'