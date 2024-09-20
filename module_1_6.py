my_dict = {'Sasha': 1990, 'Alex': 1989, 'Misha': 1992}
print(my_dict)
print(my_dict['Sasha'])
my_dict['John'] = 1972
print(my_dict['John'])
my_dict.update({'Jack': 1999, 'Don': 2003})
d = my_dict.pop('Don')
print(d)
print(my_dict)

my_set = {1, 'aple', 1, 'aple', 2, 2}
print(my_set)
my_set.update({'peach', 5})
my_set.discard(1)
print(my_set)
