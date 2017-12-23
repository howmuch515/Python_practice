from math import pi

def sphereArea(r):
    return 4 * pi * r ** 2

def sphereVolume(r):
    return (4 / 3) * pi * r ** 3

r = 10
print("r:{}, Area:{}, Volume:{}".format(r, sphereArea(r), sphereVolume(r)))
