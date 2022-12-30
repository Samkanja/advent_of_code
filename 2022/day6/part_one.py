
def read_input():
        line = f.readline().strip()
        for i in range(len(line)):
            if len(line[i:i+4]) == len(set(line[i:i+4])):
                return i + 4

with open('2022/day6/input.txt') as f:
    print(read_input())

