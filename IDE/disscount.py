price = input("Name price: ")
disscount = input("Disscount: ")
priceint = int(price)
percent = int(disscount)
new_price = priceint - (priceint * (percent/100))
diff = priceint - new_price
print(f"Price = {price}, disscount = {disscount} %, disscounted price = {new_price}, diffrence {diff}")

