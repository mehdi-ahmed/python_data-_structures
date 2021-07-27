count = 0
total = 0
fh = None

# Use the file name mbox-short.txt as the file name
f_name = input("Enter file name: ")
try:
    fh = open(f_name)
except FileNotFoundError:
    print('File not found')

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    first_section = line.find(":")
    second_section = line[first_section + 1:]
    count = count + 1
    total = total + float(second_section.lstrip())

print("Average spam confidence:", total / count)
