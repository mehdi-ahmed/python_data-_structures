# Use words.txt as the file name
f_name = input("Enter file name: ")
try:
    fh = open(f_name, 'r')
except FileNotFoundError:
    print('File not found')

for line in fh:
    line = line.rstrip()
    print(line.upper())
