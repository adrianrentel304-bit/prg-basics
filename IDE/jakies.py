total = 8000000000
north = 7200000000
totalf = float(total)
northf = float(north)
south = totalf - northf
print("World population: ", total)
print("Northern Hemisphere: ", north)
print("Northern Hemisphere in %: ", north/total*100)
print("South: ", south)
print('South % ', south/total*100)