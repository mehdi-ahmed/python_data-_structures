#  count word frequency in a Text file

# Part 1 : Read file and put word and their frequency in a dictionary
name = input('File Name: ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)  # {'Sunisa': 1, 'Lee': 2, 'of': 2, 'Team': 3, 'USA': 3, 'has': 2,...etc.

# part 2 - Print the highest word present in the dictionary

big_count = None
big_word = None
for word, count in counts.items():
    if big_count is None or count > big_count:
        big_word = word
        big_count = count

print(big_word, big_count)  # the 16
