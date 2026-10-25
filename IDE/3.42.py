time_24 = input('Enter time: ')
hours_str, minutes_str = time_24.split(':')
hours = int(hours_str)
minutes = int(minutes_str)
if hours == 0:
    time_12 = f'12:{minutes:02d}am'
elif hours < 12:
    time_12 = f'{hours}:{minutes:02d}am'
elif hours == 12:
    time_12 = f'12:{minutes:02d}pm'
else:
    time_12 = f'{hours - 12}:{minutes:02d}pm'

print(f'Time in 12-hour format: {time_12}')