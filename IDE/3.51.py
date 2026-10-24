correct_pin = '0805'
attempts = 3

while attempts > 0:
    entered_pin = input('Enter the PIN code: ')
    if entered_pin == correct_pin:
        print('Correct! Access granted.')
        break
    else:
        attempts -= 1
        print('Incorrect...')
else:
    print('Sorry, your payment card has been blocked.')