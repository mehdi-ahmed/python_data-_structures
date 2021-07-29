name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

senders = dict()
for line in handle:
    if line.startswith('From '):
        line_split = line.split()
        sender = line_split[1]
        senders[sender] = senders.get(sender, 0) + 1

# print(senders)

# Option1 - without Loop
# print(max(senders, key=senders.get), max(senders.values()))

# Option2 - with Loop

largest_sender = None
emails_sent = None
for sender, count in senders.items():
    # print(sender, count)
    if largest_sender is None:
        largest_sender = sender
        emails_sent = count

    elif count > emails_sent:
        largest_sender = sender
        emails_sent = count

# print('----------')
print(largest_sender, emails_sent)
