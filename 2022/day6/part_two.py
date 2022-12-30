def read_input():
        line = f.readline().strip()
        for i in range(len(line)):
            if len(line[i:i+14]) == len(set(line[i:i+14])):
                return i + 14

with open('2022/day6/input.txt') as f:
    print(read_input())