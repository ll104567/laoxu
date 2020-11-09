#!/usr/bin/python3
import random

def gene():
    x = random.choice(range(10,99))
    y = random.choice(range(100,999))
    if random.choice(range(10)) > 8:
        return '{}x{}=  '.format(x,y)
    else:
        return '{}x{}=  '.format(y,x)

for i in range(4):
    print('{}\t\t{}\t\t{}\t\t'.format(gene(),gene(),gene()))
