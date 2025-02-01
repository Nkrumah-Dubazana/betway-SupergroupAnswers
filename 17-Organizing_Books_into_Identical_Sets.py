#!/usr/bin/env python3



import math


shelf = [1234567, 1234567, 2345678, 2345678, 3456789, 3456789, 1234567,
         2345678, 3456789, 4567890, 4567890, 5678901, 5678901, 6789012,
         12345678, 3456789, 4567890, 5678901, 4567890, 5678901]

counts = {}
for book in shelf:
    if book in counts:
        counts[book] += 1
    else:
        counts[book] = 1

gcd_value = None
for count in counts.values():
    if gcd_value is None:
        gcd_value = count
    else:
        gcd_value = math.gcd(gcd_value, count)

if gcd_value is not None and gcd_value >= 2:
    print("YES")
else:
    print("NO")

