# Part one: Read file and put all the word in a dictionary with their frequency
f_hand = open('romeo.txt')
counts = dict()

for line in f_hand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)

# {'But': 1, 'soft': 1, 'what': 1, 'light': 1, 'through': 1, 'yonder': 1, 'window': 1, 'breaks': 1, 'It': 1, 'is': 3,
# 'the': 3, 'east': 1, 'and': 3, 'Juliet': 1, 'sun': 2, 'Arise': 1, 'fair': 1, 'kill': 1

# Part 2 : Extract data for dictionary and create a reversed tuple(instead of key value)
lst = list()
for key, val in counts.items():
    new_tuple = (val, key)
    lst.append(new_tuple)

lst = sorted(lst, reverse=True)
for val, key in lst[:10]:  # slicing for the first 10
    print(key, val)

# the 3
# is 3
# and 3
# sun 2
# yonder 1
# with 1
# window 1
# what 1
# through 1
# soft 1


# Part 2 can be replaced with:
c = {'a': 10, 'b': 1, 'c': 22}
print(sorted([(v, k) for k, v in c.items()]))

# [(1, 'b'), (10, 'a'), (22, 'c')]
