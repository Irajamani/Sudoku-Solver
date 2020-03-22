#!/usr/bin/env python3


value_dict = {}
prev = []
box_values=[]
def solver(lst_of_lsts):
    size = len(lst_of_lsts)
    value_updater(lst_of_lsts, size)
    generate_box_values(size)
    for i in range(0, size):
        for j in range(0, size):
            if lst_of_lsts[i][j] == 0:
                counter = True
                while(counter):
                    check = value_dict.get(i*size+j)
                    if check == size + 1:
                        update_to_one(i, j, size)
                        update_prev(lst_of_lsts, size)
                    elif row_check(lst_of_lsts, check, size, i, j) and col_check(lst_of_lsts, check, size, i, j) and box_checker(lst_of_lsts, check, size, i, j):
                        lst_of_lsts[i][j] = check
                        update_value(i, j, size)
                        prev.append(i*size+j)
                        counter = False
                    else:
                        update_value(i, j, size)
    return None






def value_updater(lst_of_lsts, size):
    for i in range(0, size):
        for j in range(0, size):
            if lst_of_lsts[i][j] == 0:
                value_dict[i*size+j] = 1
    return None

def row_check(lst, check, size, row_no, col_no):
    for i in range(0, col_no):
        if lst[row_no][i] == check:
            return False
    for i in range(col_no+1, size):
        if lst[row_no][i] == check:
            return False
    return True

def col_check(lst, check, size, row_no, col_no):
    for i in range(0, row_no):
        if lst[i][col_no] == check:
            return False
    for i in range(row_no + 1, size):
        if lst[i][col_no] == check:
            return False
    return True

def update_value(i, j, size):
    value_dict[i*size+j] = value_dict[i*size+j] + 1 
    return None

def update_to_one(i, j, size):
    value_dict[i*size+j] = 1

def update_prev(lst, size):
    c = prev.pop()
    i = c // size
    j = c % size
    counter = True
    while(counter):
        check = value_dict.get(i*size+j)
        if check == size + 1:
            update_to_one(i, j, size)
            lst[i][j] = 0
            update_prev(lst, size)
        elif row_check(lst, check, size, i, j) and col_check(lst, check, size, i, j) and box_checker(lst, check, size, i, j):
            lst[i][j] = check
            update_value(i, j, size)
            prev.append(i*size+j)
            counter = False
        else:
            update_value(i, j, size)

def generate_box_values(size):
    step_row = size // 3
    step_column = size // 3
    for i in range(0, size, step_row):
        for j in range(0, size, step_column):
            c = i * size
            lst = [c+j,c+j+1,c+j+2,c+j+9,c+j+10,c+j+11,c+j+18,c+j+19,c+j+20]
            box_values.append(lst)

def box_checker(lst, check, size, i, j):
    c = i*size+j
    a = []
    for i in range(0, size):
        if c in box_values[i]:
            a = box_values[i]
            break
    for i in a:
       k = i // size
       m = i % size
       if lst[k][m] == check:
           return False
    return True   





a = [[5,0,0,0,0,0,0,0,0], [1,8,0,0,0,0,0,6,0],[0,0,0,3,4,0,2,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,7,0],
[0,9,0,0,1,8,0,0,0],[0,0,0,4,0,0,0,0,0],[0,0,0,0,0,0,0,0,1],[0,0,3,7,0,0,5,0,0]]
solver(a)
print(a)