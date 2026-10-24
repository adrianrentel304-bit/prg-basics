name = input('Enter name: ')
if name.endswith('a') and name.toLowerCase() != 'kuba':
    print(f'{name} -- Polish female name')
else:
    print(f'{name} -- Not a typical Polish female name')