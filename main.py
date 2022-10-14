#!/usr/bin/env python3

from useful_package import polynom_3, hyperbola
import sys

x = float(sys.argv[1])
print(f'Input is {x}')
print(f'Polynom3 value is {polynom_3(x)}')
print(f'Hyperbola value is {hyperbola(x)}')
