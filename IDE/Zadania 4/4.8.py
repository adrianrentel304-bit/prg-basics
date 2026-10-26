def time_string(a,b,c):
    temp=' '
    if c == '12':
        temp = 'am'
        if a == 12:
            temp = 'pm'
        elif a ==24:
            temp = 'am'
            a=a-12
        elif a > 12:
            a=a-12
            temp = 'pm'
    return print(f'In given format its: {a}:{b} {temp}')
a=int(input("Hour"))
b=int(input("Min"))
c=input("format 12/24:")
time_string(a,b,c)
