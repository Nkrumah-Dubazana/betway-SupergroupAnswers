#!/usr/bin/env python3


outcomes = [123456, 234567, 123347, 456789, 567890, 678901, 789012, 890123,
            901234, 112233, 223344, 334455, 789012, 222234, 123347]

counts = {}

for outcome in outcomes:
    if outcome in counts:
        counts[outcome] += 1
    else:
        counts[outcome] = 1

duplicates = []
for outcome, count in counts.items():
    if count > 1:
        duplicates.append(outcome)

print(duplicates)

