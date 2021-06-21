from sudoku.lib import try_me

def test_try_me():
    grid = [
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
    solved = try_me(grid)
    assert len(solved) == len(grid)
    for row in solved:
        assert len(row) == len(grid[0])
        for cell in row:
            assert cell in range(1, 10)