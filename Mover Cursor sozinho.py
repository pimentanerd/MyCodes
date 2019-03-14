import autopy
import time
from random import randint

l = [1,1,10,10,1000, 2000, 5, 789, 89, 69, 21]
rl = l[randint(0, 10)]

while True:
    autopy.mouse.smooth_move(rl, rl)
    time.sleep(5)
    autopy.mouse.smooth_move(rl, rl)
    time.sleep(5)