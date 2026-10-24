
light_switch1 = True   # Switch 1 lights 1 bulb
light_switch2 = True   # Switch 2 lights 2 bulbs
bulbs_on = 0

if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 2

print(f'Total bulbs lit: {bulbs_on}')