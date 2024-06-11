my_dict = {'Disk C': [117, 446], 'Disk D': [339, 931], 'Disk F': [3, 16.2]}
print(my_dict)
print(my_dict.get('Disk C'))
print(my_dict.get('Disk J', 'Такого диска не обнаружено'))
my_dict.update({'Disk A': [223, 747], 'Disk Y': [0, 947]})
disk = my_dict.pop('Disk F')
print(disk)
print(my_dict)
my_set = {1, 1, 1, 4, 5, 'Action', (1, 2, 3), (1, 2, 3)}
print(my_set)
my_set.add('Boat')
my_set.add(6)
my_set.discard((1, 2, 3))
print(my_set)