immutable_var = ([1, 2, 3], 5, 6, 'салют, бродяги', True)
print(immutable_var)
print('Содержимое кортежей относится к неизменяемому типу. Тоесть, невозможно изменить содержмое кортежей.'
      ' Исключением является наличие внутри кортежа изменяемых объектов, например - список. Однако нельзя,'
      ' к примеру удалить из кортежа сам список или заменить его на другой объект, допустимо лишь изменить'
      ' содержимое списка, как на примере ниже.')
immutable_var [0] [0] = 4
immutable_var [0] [2] = 7
print(immutable_var)
mutable_list = ['ракета', 'торт', 9, 6, 8, False]
print(mutable_list)
mutable_list [0] = True
mutable_list [1] = 'string'
mutable_list. remove(False)
mutable_list. append('list')
mutable_list. extend(['Python', 1])
print(mutable_list)
