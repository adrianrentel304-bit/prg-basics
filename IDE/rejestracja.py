car_number = input('Enter car registration number')
is_krakow = False
if car_number[0:2] == 'KR' or car_number[0:2] == 'KK':
    is_krakow = True
print(f'Car is from Krakow: {is_krakow}')