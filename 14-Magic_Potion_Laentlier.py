#!/usr/bin/env python3


power = int(input("Enter the potion's power level: "))

cube_root = round(power ** (1/3))

if cube_root ** 3 == power:
    print("YES")
else:
    print("NO")

