# Sudokusolver
import tkinter as tk

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    
    row, col = empty_cell
    for num in map(str, range(1, 10)):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = '0'
    
    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '0':
                return (i, j)
    return None

def clear_board():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            entries[i][j].insert(0, '0')

def solve_puzzle():
    for i in range(9):
        for j in range(9):
            if entries[i][j].get() not in map(str, range(1, 10)):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, '0')
    
    sudoku_board = [[entries[i][j].get() for j in range(9)] for i in range(9)]
    
    if solve_sudoku(sudoku_board):
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, sudoku_board[i][j])
    else:
        print("No solution exists.")

root = tk.Tk()
root.title("Sudoku Solver")

# Create a 9x9 grid using Entry widgets
entries = [[tk.Entry(root, width=2) for _ in range(9)] for _ in range(9)]

# Place the grid in the GUI
for i in range(9):
    for j in range(9):
        entries[i][j].grid(row=i, column=j)

# Create a "Solve" button
solve_button = tk.Button(root, text="Solve", command=solve_puzzle)
solve_button.grid(row=9, column=4)

# Create a "Clear" button
clear_button = tk.Button(root, text="Clear", command=clear_board)
clear_button.grid(row=9, column=5)

# Run the GUI
root.mainloop()
