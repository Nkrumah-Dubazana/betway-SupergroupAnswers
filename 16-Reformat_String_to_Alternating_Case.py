#!/usr/bin/env python3


s = input("Enter the string to reformat: ")

result = []


alpha_index = 0


for char in s:
    if char.isalpha():
        
        if alpha_index % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())
        alpha_index += 1
    else:
        
        result.append(char)


reformatted_string = "".join(result)
print(reformatted_string)
