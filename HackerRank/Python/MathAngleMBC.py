# https://www.hackerrank.com/challenges/find-angle/problem

from math import atan
from math import sqrt
from math import cos
from math import asin
from math import sin
from math import pi

def sol1():
    side_AB = int(input())
    side_BC = int(input())

    angle_BCA = atan(side_AB/side_BC)
    side_AC = sqrt(side_AB**2 + side_BC**2)
    side_MC = side_AC / 2
    side_MB = sqrt(side_MC**2 + side_BC**2 - 2*side_MC*side_BC*cos(angle_BCA))
    angle_MBC = asin(side_MC * sin(angle_BCA) / side_MB)
    angle_MBC_deg = round(angle_MBC * 180 / pi)

    print(f"{angle_MBC_deg}\N{DEGREE SIGN}")

# mathematically, angle BCM or angle BCA = angle CBM
def sol2():
    a, b = int(input()), int(input())
    phi = atan(a/b)
    print(round((phi*360)/(2*pi)), "\u00b0", sep='')