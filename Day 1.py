'''
Advent of code 2025
Day 1
by Jolyon Everett
3/12/25
'''
import sys
import os

position = 50
password = 0
def solve(filepath):
    global position
    global password

    lineNo = 0;
    file = open(filepath).readlines()
    for line in file:
        lineNo += 1
        direction = line[0]
        number = int(line[1:])
        if direction == 'L':
            step = -1
        elif direction == 'R':
            step = 1
        else:
            raise ValueError(f"Invalid Direction: {direction}")
        for n in range(number):
            position = (position + step) % 100
            if position == 0:
                password += 1
        
solve(sys.argv[1])
print(f"The password is {password}")