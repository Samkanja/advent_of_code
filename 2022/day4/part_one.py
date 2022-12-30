from typing import Set


def is_subclass(set_1:Set[int], set_2:Set[int]) -> bool:
    return set_1.issubset(set_2) or set_2.issubset(set_1)

def create_sets(line:str):
    list_a = line.split(',')
    group_sets= [i.split('-') for i in list_a]
    final_set = [set(range(int(i[0]),int(i[-1])+1)) for i in group_sets]
    return final_set   




def read_input():
    count = 0
    while True:
        line = f.readline().strip()
        if line =="":
            return count
        list_s = create_sets(line)
        if is_subclass(*list_s):
            count += 1

          

        



with open('2022/day4/input.txt') as f:
    print(read_input())