data = 'From mehdi.ahmed.2009@gmail.com Sat 05 July 09:14:2021'
#                            21         31

at_pos = data.find('@')
print(at_pos)  # 21

sp_pos = data.find(' ', at_pos)
print(sp_pos)  # 31

host = data[at_pos + 1: sp_pos]
print(host)  # gmail.com


data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(pos)  # 12
print(data[pos:pos+3])  # .ma
