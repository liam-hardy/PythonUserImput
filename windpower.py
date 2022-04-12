print('variables for Pmax:')
windspeed = input('enter windspeed ')
windspeed = float(windspeed)
bladeradius = input('enter bladeradius ')
bladeradius = float(bladeradius)
p = 1.2
print(f'Area = {3.14159265 * bladeradius ** 2}')
Area = 3.14159265 * bladeradius ** 2
print(f'Pmax =  {0.5 * p * Area * windspeed ** 3 }')
Pmax = 0.5 * p * Area * windspeed ** 3
efficiency = input('enter efficiency ')
efficiency = float(efficiency)
print(f'Actual P = {Pmax * (efficiency / 100)}')
