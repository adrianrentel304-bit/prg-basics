current_price = 140.00
previous_price = 200.00
discount_percentage = ((previous_price - current_price) / previous_price) * 100

print(f'Current product price: {current_price:.2f}')
print(f'Previous product price: {previous_price:.2f}')

if discount_percentage >= 10:
    print('Buy the product!!')
    print(f'Product price reduced by {int(discount_percentage)}%')