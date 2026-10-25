ean = input('Article number: ')

if len(ean) == 13 and ean.isdigit():
    print('Article number is correct')
    if ean.startswith('590'):
        print('Article manufactured in Poland')
else:
    print('Article number is incorrect')