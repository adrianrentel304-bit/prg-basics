def sum_digits(a):
    a=abs(a)
    temp=str(a)
    total=0

    for t in temp:
        total=total+int(t)
    return total

num=int(input("enter number: "))
sum=sum_digits(num)
print(f'The sum of digits in the number {num} is {sum}')