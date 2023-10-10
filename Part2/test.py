def solve_sudoku(board):
    def is_valid_move(row, col, num):
        # 检查行约束
        if num in board[row]:
            return False

        # 检查列约束
        if num in [board[i][col] for i in range(9)]:
            return False

        # 检查宫约束
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def solve(row, col):
        if row == 9:
            return True

        next_row = row + 1 if col == 8 else row
        next_col = (col + 1) % 9

        if board[row][col] != 0:
            return solve(next_row, next_col)

        for num in range(1, 10):
            if is_valid_move(row, col, num):
                board[row][col] = num
                if solve(next_row, next_col):
                    return True
                board[row][col] = 0  # 回溯

        return False

    solve(0, 0)
    return board


# 数独问题的初始棋盘，0 表示未填写数字的位置
sudoku_board = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 3, 6, 0, 0, 0, 0, 0],
                [0, 7, 0, 0, 9, 0, 2, 0, 0],
                [0, 5, 0, 0, 0, 7, 0, 0, 0],
                [0, 0, 0, 0, 4, 5, 7, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 3, 0],
                [0, 0, 1, 0, 0, 0, 0, 6, 8],
                [0, 0, 8, 0, 0, 0, 0, 1, 0],
                [0, 9, 0, 0, 0, 0, 4, 0, 0]]

solution = solve_sudoku(sudoku_board)

if solution:
    print("解决的数独：")
    for row in solution:
        print(row)
else:
    print("无解")
