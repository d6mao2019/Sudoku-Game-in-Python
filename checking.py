
def row_check(table, row_index):
    """checks if the specified row of a given is valid."""
    assert(row_index >= 0)
    assert(row_index <= 8)
    row = table[row_index]
    nums = row[row != 0]
    return len(set(nums)) == len(nums)


def col_check(table, col_index):
    """checks if the specified col of a given is valid."""
    assert(col_index >= 0)
    assert(col_index <= 8)
    col = table[:, col_index]
    nums = col[col != 0]
    return len(set(nums)) == len(nums)


def blo_check(table, blo_index):
    """checks if the specified blo of a given is valid."""
    assert(blo_index >= 0)
    assert(blo_index <= 8)
    blo = table[(blo_index // 3) * 3: (blo_index // 3) * 3 + 3,
                (blo_index % 3) * 3: (blo_index % 3) * 3 + 3]
    blo.flatten()
    nums = blo[blo != 0]
    return len(set(nums)) == len(nums)


def cell_check(table, row_index, col_index):
    blo_index = (row_index // 3) * 3 + (col_index // 3)
    return (row_check(table, row_index) and
            col_check(table, col_index) and
            blo_check(table, blo_index))


def is_empty(table, row_index, col_index):
    return table[row_index][col_index] == 0


def is_full(table):
    a = table.flatten()
    assert(len(a) == 81)
    for j in range(81):
        if (a[j] == 0):
            return False
    return True


def is_solved(table):
    assert(is_full(table))
    for j in range(9):
        if not (row_check(table, j) and
                col_check(table, j) and
                blo_check(table, j)):
            return False
    return True
