x_file = open('mbox.txt', 'r')  # Whether we want to read data from the file or write data to the file
for line in x_file:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

# From: random stuff in line 1
# From: This is it? Don't get too excited.


# Read all file ans store data in a string
print('--------------------')
f_hand = open('mbox.txt')
inp = f_hand.read()
print(inp)
