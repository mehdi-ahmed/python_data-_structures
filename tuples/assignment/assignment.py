name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

dict_hours = dict()
for line in handle:
    if line.startswith('From '):
        date_pos = line.find('  ')
        split_time_pos = line[date_pos:]
        time = split_time_pos.split()[1]
        hour = time.split(':')[0]
        dict_hours[hour] = dict_hours.get(hour, 0) + 1

# print(dict_hours)

# Sorting dictionary by key
dict_hours_sorted = dict(sorted(dict_hours.items()))

for hour, count in dict_hours_sorted.items():
    print(hour, count)
