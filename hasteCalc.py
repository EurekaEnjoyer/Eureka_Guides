#Determine the GCD including haste for a job
import math


def GlobalCD(l_sub, S, l_div):
    return (math.floor(G * (1 - 0.01 * n) * (100 + (math.ceil(130 * (l_sub - S) / l_div)) / 10))) / 100


l_sub = 380
S = 991
l_div = 1300
n = 15
G = 2.8
print(GlobalCD(l_sub, S, l_div))
