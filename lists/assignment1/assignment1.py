file = open('romeo.txt', 'r')

list_words = list()
for line in file:
    words = line.split()
    for word in words:
        if word not in list_words:
            list_words.append(word)

list_words.sort()
print(list_words)
