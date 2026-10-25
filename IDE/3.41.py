total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ')
extra_rinse = input('Extra rinse? (y/n): ') == 'y'
extra_spin = input('Extra spin? (y/n): ') == 'y'

if program == 'j':
    total_washing_time += 40
elif program == 'u':
    total_washing_time += 70
elif program == 's':
    total_washing_time += 20

if extra_rinse:
    total_washing_time += 15
if extra_spin:
    total_washing_time += 9

print(f'Total washing time: {total_washing_time} minutes')