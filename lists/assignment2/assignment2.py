f_name = input("Enter file name: ")
if len(f_name) < 1:
    f_name = "mbox-short.txt"

emails = list()
fh = open(f_name)
for line in fh:
    if line.startswith('From:'):
        continue
    elif line.startswith('From'):
        line_split = line.split()
        emails.append(line_split[1])

for email in emails:
    print(email)
print("There were", len(emails), "lines in the file with From as the first word")
