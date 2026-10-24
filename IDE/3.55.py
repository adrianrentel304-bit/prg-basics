for row in range(1, 8):
    for col in range(0, 7):
        val = row + (col * 7)
        print(f'{val:2d}', end=' ')
    print()