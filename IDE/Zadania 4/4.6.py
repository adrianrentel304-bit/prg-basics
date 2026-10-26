def grade(a):
    if a >= 18:
        grade='Excellent'
    elif a>=14:
        grade='Good'
    elif a>=10:
        grade='Satisfactory'
    else:
        grade='Fail'

    return grade

a=int(input("Pts: "))
print(grade(a))