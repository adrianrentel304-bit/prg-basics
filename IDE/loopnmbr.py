name = input("Name: ")
astr = 0
a = int(astr)
b=len(name)
while a != b:
    print(f"The letter {name[a]} is assigned to the number {ord(name[a])}")
    a=a+1
