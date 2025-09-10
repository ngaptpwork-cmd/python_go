#Bai tap su dung every function
language_list = ['Vietnamese', 'English', 'Japanese', 'Chinese']
print(language_list)

language_list.append('Hawaian')
print(language_list)

language_list.insert(4,'French')
print(language_list)

del language_list[-1]
print(language_list)

language_list.pop(4)
print(language_list)

language_list.remove('Chinese')
print(language_list)

print(sorted(language_list))

print(sorted(language_list, reverse=True))

language_list.reverse()
print(language_list)

language_list.reverse()
print(language_list)

language_list.sort()
print(language_list)

print(len(language_list))
