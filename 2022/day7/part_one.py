from typing import TextIO
from collections import defaultdict


def problem_solution():
    input = read_input()
    size_limit = 100000
    file_path = []
    directory_sizes = defaultdict(int)
    terminal_prompt = '$'
    cd_command = 'cd'
    root_directory = '/'
    preivous_dir = '..'
    dir_label = 'dir'

    for line in input:
        line = line.split(' ')
        print(line)
        if line[0] == terminal_prompt:
            if line[1] == cd_command:
                if line[2] == root_directory:
                    file_path = ['/']
                elif line[2] == preivous_dir:
                    file_path.pop()
                else:
                    file_path.append(line[2])
        elif line[0] != '':
            if line[0] != 'dir':
                size = int(line[0])
                for i in range(len(file_path)):
                    if i <= 1:
                        directory_sizes[file_path[i]] += size
                    else:
                        parent = file_path[i - 1]
                        current = file_path[i]
                        directory_key = f'{parent}/{current}'
                        directory_sizes[directory_key] += size
                         
    sum_of_sizes_less_than_limit = 0
    for size in directory_sizes.values():
        if size <= size_limit:
            sum_of_sizes_less_than_limit += size
        


    return sum_of_sizes_less_than_limit


def read_input():
    f = open('2022/day7/input.txt','r')
    output_txt = f.read()
    output = output_txt.split('\n')
    return output


answer = problem_solution()
print(answer)



