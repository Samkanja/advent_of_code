from typing import List
def solve_problem(line:List[str]):
    rows = len(line)
    columns = len(line[0])

    visible_trees = rows * 2 + (columns - 2) *  2
    for row in range(1,rows-1):
        for col in range(1,columns-1):
            tree = line[row][col]
            left = [line[row][col-i] for i in range(1,col+1)]
            right = [line[row][col+i] for i in range(1,columns-col)]
            up = [line[row-i][col] for i in range(1,row+1)]
            down = [line[row+i][col] for i in range(1,rows - row)]

            if max(left) < tree or max(up) < tree or max(right) <tree or max(down) < tree:
                visible_trees +=1

    return visible_trees

with open('2022/day8/input.txt') as f:
    line = [row.strip() for row in f.readlines()]
    print(solve_problem(line))
   