
def plain_print(table):
    for row in range(9):
        for col in range(9):
            if (col != 8):
                print(table[row][col], end='')
            else:
                print(table[row][col])


def fancy_print(table):
    for j in range(9):
        if (j % 3 == 0):
            print('-' * 37)
        row_list = list(table[j])
        for j in range(9):
            if (row_list[j] == 0):
                row_list[j] = ' '
            else:
                row_list[j] = int(row_list[j])
        print('|', row_list[0], ' ', row_list[1], ' ', row_list[2], '|',
              row_list[3], ' ', row_list[4], ' ', row_list[5], '|',
              row_list[6], ' ', row_list[7], ' ', row_list[8], '|')
    print('-' * 37)
