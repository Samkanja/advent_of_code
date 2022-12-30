from typing import TextIO
import string

def read_input(f:TextIO,group_size:int=3):
    while True:
        yield [f.readline().strip() for _ in range(group_size)]


def calculation_of_priorities(f:TextIO):
    groups_str = read_input(f)
    total = 0
    while True:
        badges = next(groups_str)
        if not any(badges):
            return total
        char = list(set(badges[0]) & set(badges[1]) & set(badges[2]))[0]
        total += string.ascii_letters.index(char) +1 

with open('2022/day3/input.txt') as f:
    print(calculation_of_priorities(f))
   