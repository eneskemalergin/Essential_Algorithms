# Least Common Multiplier for multiple inputs
# Author: Enes Kemal Ergin

from lcm import lcm
def lcmm(*args):
    return reduce(lcm, args)


print lcmm(12,3,6,4)