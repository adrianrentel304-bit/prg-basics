speed = input("Enter car speed: ")
speedint = int(speed)
law = False
if speedint < 141 and speedint > 39:
    law = True
print(f"You are driving legally: {law}")