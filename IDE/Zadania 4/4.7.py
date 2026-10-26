def day_n(a):
    if a == 1:
        b="monday"
    elif a ==2:
        b="tuesday"
    elif a == 3:
        b='wendsday'
    elif a == 4:
        b='thursday'
    elif a== 5:
        b = "friday"
    elif a== 6:
        b = 'saturday'
    elif a==7:
        b = "sunday"
    else:
        b = 'invalid'

    return b

a=int(input("Day number"))
print(day_n(a))