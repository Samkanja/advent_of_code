from typing import Set,List

def sets_intersect(set_1:Set[int],set_2:Set[int]) -> bool:
    return bool(set_1.intersection(set_2))

def create_list_sets(line:str) -> List[Set[int]]:
    list_a = line.split(',')
    list_b = [i.split('-') for i in list_a]
    list_c = [set(range(int(i[0]),int(i[-1])+1)) for i in list_b]
    return list_c
    

def read_input():
    count = 0
    while True:
        line = f.readline().strip()
        if line == '':
            return count 
        sets = create_list_sets(line)
        if sets_intersect(*sets):
            count += 1


with open('2022/day4/input.txt') as f:
    print(read_input())