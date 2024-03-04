import random
from itertools import permutations
import itertools

row1 = [0, 0, 0, 0, 0, 0]
row2 = [0, 0, 0, 0, 0, 0]
row3 = [0, 0, 0, 0, 0, 0]
row4 = [0, 0, 0, 0, 0, 0]
row5 = [0, 0, 0, 0, 0, 0]
row6 = [0, 0, 0, 0, 0, 0]
visable_left = [3, 0, 0, 6, 0, 3]
visable_right = [0, 4, 0, 0, 5, 3]
visable_top = [4, 0, 3, 3, 0, 0]
visable_bottom = [0, 0, 0, 4, 0, 0]

def check_row(row, vLeft, vRight):
        inRange = all(1 <= num <= 6 for num in row)
        noRepeats = len(row) == len(set(row))
        correctSum = sum(row) == 21
        correctVisable = False
        if vLeft == 0 and vRight != 0:
            correctVisable = visible_numbers_right(row) == vRight
        if vRight == 0 and vLeft != 0:
            correctVisable = visible_numbers_left(row) == vLeft
        if vLeft == 0 and vRight == 0:
            correctVisable = True
        if vLeft != 0 and vRight != 0:
            correctVisable = visible_numbers_left(row) == vLeft and visible_numbers_right(row) == vRight
        return inRange and noRepeats and correctSum and correctVisable

def visible_numbers_left(row):
    visible_count = 1
    if row[1] > row[0]:
        visible_count += 1
    if row[2] > row[1] and row[2] > row[0]:
        visible_count += 1
    if row[3] > row[2] and row[3] > row[1] and row[3] > row[0]:
        visible_count += 1
    if row[4] > row[3] and row[4] > row[2] and row[4] > row[1] and row[4] > row[0]:
        visible_count += 1
    if row[5] > row[4] and row[5] > row[3] and row[5] > row[2] and row[5] > row[1] and row[5] > row[0]:
        visible_count += 1
    return visible_count

def visible_numbers_right(row):
    visible_count = 1
    if row[4] > row[5]:
        visible_count += 1
    if row[3] > row[4] and row[3] > row[5]:
        visible_count += 1
    if row[2] > row[3] and row[2] > row[4] and row[2] > row[5]:
        visible_count += 1
    if row[1] > row[2] and row[1] > row[3] and row[1] > row[4] and row[1] > row[5]:
        visible_count += 1
    if row[0] > row[1] and row[0] > row[2] and row[0] > row[3] and row[0] > row[4] and row[0] > row[5]:
        visible_count += 1
    return visible_count

def visible_numbers_top(column):
    visible_count = 1
    if column[1] > column[0]:
        visible_count += 1
    if column[2] > column[1] and column[2] > column[0]:
        visible_count += 1
    if column[3] > column[2] and column[3] > column[1] and column[3] > column[0]:
        visible_count += 1
    if column[4] > column[3] and column[4] > column[2] and column[4] > column[1] and column[4] > column[0]:
        visible_count += 1
    if column[5] > column[4] and column[5] > column[3] and column[5] > column[2] and column[5] > column[1] and column[5] > column[0]:
        visible_count += 1
    return visible_count

def visible_numbers_bottom(column):
    visible_count = 1
    if column[4] > column[5]:
        visible_count += 1
    if column[3] > column[4] and column[3] > column[5]:
        visible_count += 1
    if column[2] > column[3] and column[2] > column[4] and column[2] > column[5]:
        visible_count += 1
    if column[1] > column[2] and column[1] > column[3] and column[1] > column[4] and column[1] > column[5]:
        visible_count += 1
    if column[0] > column[1] and column[0] > column[2] and column[0] > column[3] and column[0] > column[4] and column[0] > column[5]:
        visible_count += 1
    return visible_count

def check_column(column, vTop, vBottom):
    inRange = all(1 <= num <= 6 for num in column)
    noRepeats = len(column) == len(set(column))
    correctSum = sum(column) == 21
    correctVisable = False
    if vTop == 0 and vBottom != 0:
        correctVisable = visible_numbers_bottom(column) == vBottom
    if vBottom == 0 and vTop != 0:
        correctVisable = visible_numbers_top(column) == vTop
    if vTop == 0 and vBottom == 0:
        correctVisable = True
    if vTop != 0 and vBottom != 0:
        correctVisable = visible_numbers_top(column) == vTop and visible_numbers_bottom(column) == vBottom
    if inRange == False or noRepeats == False or correctSum == False or correctVisable == False:
        return False
    return inRange and noRepeats and correctSum and correctVisable

def check_columns(row1, row2, row3, row4, row5, row6, vTop, vBottom):
    for i in range(6):
        column = [row1[i], row2[i], row3[i], row4[i], row5[i], row6[i]]
        inRange = all(1 <= num <= 6 for num in column)
        noRepeats = len(column) == len(set(column))
        correctSum = sum(column) == 21
        correctVisable = False
        if vTop[i] == 0 and vBottom[i] != 0:
            correctVisable = visible_numbers_bottom(column) == vBottom
        if vBottom[i] == 0 and vTop[i] != 0:
            correctVisable = visible_numbers_top(column) == vTop
        if vTop[i] == 0 and vBottom[i] == 0:
            correctVisable = True
        if vTop[i] != 0 and vBottom[i] != 0:
            correctVisable = visible_numbers_top(column) == vTop and visible_numbers_bottom(column) == vBottom
        if inRange == False or noRepeats == False or correctSum == False or correctVisable == False:
            return False
    return inRange and noRepeats and correctSum and correctVisable

def organize_row(row, visable_left, visable_right):
    while check_row(row, visable_left, visable_right) != True:
        numbers = random.sample(range(1, 7), 6)
        for i in range(6):
            row[i] = numbers[i]
    print(row)
    return row

#while check_columns(row1, row2, row3, row4, row5, row6, visable_top, visable_bottom) != True:
    row1 = [0, 0, 0, 0, 0, 0]
    row2 = [0, 0, 0, 0, 0, 0]
    row3 = [0, 0, 0, 0, 0, 0]
    row4 = [0, 0, 0, 0, 0, 0]
    row5 = [0, 0, 0, 0, 0, 0]
    row6 = [0, 0, 0, 0, 0, 0]
    organize_row(row1, visable_left[0], visable_right[0])
    organize_row(row2, visable_left[1], visable_right[1])
    organize_row(row3, visable_left[2], visable_right[2])
    organize_row(row4, visable_left[3], visable_right[3])
    organize_row(row5, visable_left[4], visable_right[4])
    organize_row(row6, visable_left[5], visable_right[5])
    print("-----------------")
print("Done! Answer:")
print(row1)
print(row2)
print(row3)
print(row4)
print(row5)
print(row6)

def find_all_rows(vLeft, vRight):
    possible_rows = []
    for row in permutations(range(1, 7)):
        if check_row(list(row), vLeft, vRight):
            possible_rows.append(list(row))
    return possible_rows

def find_all_columns(vTop, vBottom):
    possible_columns = []
    for column in permutations(range(1, 7)):
        if check_column(list(column), vTop, vBottom):
            possible_columns.append(list(column))
    return possible_columns

def check_game(rows, columns, vTop, vBottom):
    for i in range(6):
        column = [row[i] for row in rows]
        if not check_column(column, vTop[i], vBottom[i]):
            return False
    return True

def cross_reference(possible_rows, possible_columns):
    solutions = []
    counter = 0
    total = len(possible_rows)**6 * len(possible_columns)**6
    for rows in itertools.product(*possible_rows):
        for columns in itertools.product(*possible_columns):
            counter += 1
            print(f"Checking possibility {counter} of {total}")
            if check_game(rows, columns, visable_top, visable_bottom):
                solutions.append((rows, columns))
                print("Solution found!")
    return solutions

possible_rows = [find_all_rows(visable_left[i], visable_right[i]) for i in range(6)]
possible_columns = [find_all_columns(visable_top[i], visable_bottom[i]) for i in range(6)]
solutions = cross_reference(possible_rows, possible_columns)

for solution in solutions:
    print("Solution:")
    for row in solution[0]:
        print(row)
    print("-----------------")