age=input("ile masz lat")
agen=int(age)
if agen > 17:
    print("pelnoletni")
else:
    print("dziecko")
if agen % 2 == 0:
    print("parzysta")
else:
    print("nie")
print(f"masz {agen} lat")
