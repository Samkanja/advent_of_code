from typing import TextIO
from collections import defaultdict


def problem_solution(f:TextIO):
    input = read_input(f)
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
                         
    unused_space = 70000000 - directory_sizes['/']
    min_free_space = 30000000 - unused_space
    sorted_direcrory_sizes = sorted(directory_sizes.items(), key=lambda x:x[1])

    for _, size in sorted_direcrory_sizes:
        if size >= min_free_space:
            return size

def read_input(f:TextIO):
    
    output_txt = f.read()
    output = output_txt.split('\n')
    return output

with open('2022/day7/input.txt') as f:
    print(problem_solution(f))