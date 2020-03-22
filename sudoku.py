#!/usr/bin/env python3


value_dict = {}
prev = []
def solver(lst_of_lsts):
    size = len(lst_of_lsts)
    value_updater(lst_of_lsts, size)
    for i in range(0, size):
        for j in range(0, size):
            if lst_of_lsts[i][j] == 0:
                counter = True
                while(counter):
                    check = value_dict.get(i*size+j)
                    if check == size + 1:
                        update_to_one(i, j, size)
                        update_prev(size)
                    elif row_check(lst_of_lsts, check, size, i, j) and col_check(lst_of_lsts, check, size, i, j):
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

def update_prev(size):
    c = prev.pop()
    i = c // size
    j = c % size
    










a = [[0, 0, 1],[1, 0, 0],[2, 0, 3]]
solver(a)
print(a)