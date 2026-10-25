a, b = 0, 1

for i in range(20):
    print(f'{a}')
    temp = a
    a = b
    b = temp + b

print()