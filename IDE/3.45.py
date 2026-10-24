num = int(input('Enter decimal number: '))
original = num
binary = ''

if num == 0:
    binary = '0'
else:
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2

print(f'{original}(10) = {binary}(2)')