import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    isEven = (n % 2 == 0)
    isEvenAndInRange2_5 = (isEven and 2 <= n <= 5)
    isEvenAndInRange6_20 = (isEven and 6 <= n <= 20)
    isEvenAndGreaterThan20 = (isEven and n > 20)

    if isEvenAndGreaterThan20:
        print('Not Weird')
    elif isEvenAndInRange6_20:
        print('Weird')
    elif isEvenAndInRange2_5:
        print('Not Weird')
    else:
        print('Weird')


