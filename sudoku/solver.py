def solve(grid):
    """Sudoku solver"""
    if not is_grid_format_valid(grid):
        return None
    return _solve(grid)

def is_grid_format_valid(grid):
    def is_row_format_valid(row):
        return isinstance(row, list) and len(row) == 9
    return (
        isinstance(grid, list)
        and len(grid) == 9
        and all(is_row_format_valid(row) for row in grid)
    )

def _solve(grid, current_coord = (0,0)):
    """Attempts to complete grid starting at current_coord,
    returns None when grid cannot be solved
    """
    if reject(grid):
        return None
    if accept(grid):
        return grid
    (row_index, col_index) = current_coord
    if grid[row_index][col_index] != 0:
        return _solve(grid, next_cell_coord(current_coord))
    for num in range(1, 10):
        grid[row_index][col_index] = num
        solved = _solve(grid, next_cell_coord(current_coord))
        if solved:
            return solved
    grid[row_index][col_index] = 0
    return None

def next_cell_coord(coord):
    (row_index, col_index) = coord
    if col_index < 8:
        return (row_index, col_index + 1)
    if row_index < 8:
        return (row_index + 1, 0)
    return None

def reject(grid):
    return (
        any(seq_has_duplicates(row) for row in each_grid_rows(grid))
        or any(seq_has_duplicates(col) for col in each_grid_cols(grid))
        or any(seq_has_duplicates(sqr_cells(sqr)) for sqr in each_grid_sqrs(grid))
    )

def accept(grid):
    return (
        all(seq_is_complete(row) for row in each_grid_rows(grid))
        and all(seq_is_complete(col) for col in each_grid_cols(grid))
        and all(seq_is_complete(sqr_cells(sqr)) for sqr in each_grid_sqrs(grid))
    )

def grid_rows(grid):
    return grid

def grid_cols(grid):
    return [
        [row[col_index] for row in grid]
        for col_index in range(0, 9)
    ]

def grid_sqrs(grid):
    return [
        grid_sqr(grid, row_index, col_index)
        for col_index in range(0, 3)
        for row_index in range(0, 3)
    ]

def grid_sqr(grid, row_index, col_index):
    return [
        row[col_index*3:(col_index+1)*3]
        for row in grid[row_index*3:(row_index+1)*3]
    ]

def each_grid_rows(grid):
    for row in grid:
        yield(row) 

def each_grid_cols(grid):
    for col_index in range(0, 9):
        yield([row[col_index] for row in grid])

def each_grid_sqrs(grid):
    for col_index in range(0, 3):
        for row_index in range(0, 3):
            yield(grid_sqr(grid, row_index, col_index))

def sqr_cells(sqr):
    return [cell for row in sqr for cell in row]

def seq_has_duplicates(seq):
    return any(seq.count(num) > 1 for num in range(1, 10))

def seq_is_complete(seq):
    return all(num in seq for num in range(1, 10))

def grid_as_str(grid):
    return '\n'.join(' '.join(str(cell) for cell in row) for row in grid)

if __name__ == '__main__':
    input_grid = [
            [7,0,0,  0,0,0,  0,0,6],
            [0,0,0,  6,0,0,  0,4,0],
            [0,0,2,  0,0,8,  0,0,0],
            [0,0,8,  0,0,0,  0,0,0],
            [0,5,0,  8,0,6,  0,0,0],
            [0,0,0,  0,2,0,  0,0,0],
            [0,0,0,  0,0,0,  0,1,0],
            [0,4,0,  5,0,0,  0,0,0],
            [0,0,5,  0,0,7,  0,0,4]
        ]
    print('Input grid:')
    print(grid_as_str(input_grid))
    solved_grid = solve(input_grid)
    if solved_grid:
        print('Solved grid:')
        print(grid_as_str(solved_grid))
    else:
        print("Cannot solve")
