# Selective import
''' 
   Gerenal import, like import math, make all functionally from math package available to you. However, if you decide to only use a specific part of a package,
   you can always make your import more selective:
    from math import pi
   Let's say the Moon's orbit around planet Earth is a perfect circle, with a radius r(in km) tha is defined in the script
'''

#Instructions
    # I - Perform a selective import from the math package where you only import the radians function.
    # II - Calculate the distance travelled by the Moon over 12 degrees of its orbit. Assign the result to dist. You can calculate this as r * phi,
    # where r is the radius and phi is the angle in radians. To convert an angle in degrees to an angle in radians, use the radians() function, which you just imported.
    # III - Print out dist.


# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
phi = 12
dist = radians(r* phi)

# Print out dist
print(dist)