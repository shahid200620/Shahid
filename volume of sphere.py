#volume of sphere 
import math
r=int(input('Enter the radius value: '))
v=(4/3)*math.pi*math.pow(r,3)
print('The volume of sphere is :',v)
#round to a decimal using round fn
print('The volume of sphere is :',round(v,3))
#using format method
print('The volume of sphere is :{:.3f}'.format(v))