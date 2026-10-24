time_24 = input('Enter time (24-hour format hh:mm): ')
hours, minutes = map(int, time_24.split(':'))

if hours == 0:
    time_12 = f'12:{minutes:02d}am'
elif hours < 12:
    time_12 = f'{hours}:{minutes:02d}am'
elif hours == 12:
    time_12 = f'12:{minutes:02d}pm'
else:
    time_12 = f'{hours - 12}:{minutes:02d}pm'

print(f'Time in 12-hour format: {time_12}')