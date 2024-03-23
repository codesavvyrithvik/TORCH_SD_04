def is_valid_move(board, row, col, num):
  # Check if the number is already in the row
  if num in board[row]:
      return False

  # Check if the number is already in the column
  if num in [board[i][col] for i in range(9)]:
      return False

  # Check if the number is already in the 3x3 box
  start_row, start_col = 3 * (row // 3), 3 * (col // 3)
  for i in range(start_row, start_row + 3):
      for j in range(start_col, start_col + 3):
          if board[i][j] == num:
              return False

  return True

def solve_sudoku(board):
  empty_cell = find_empty_cell(board)
  if not empty_cell:
      return True

  row, col = empty_cell
  for num in range(1, 10):
      if is_valid_move(board, row, col, num):
          board[row][col] = num
          if solve_sudoku(board):
              return True
          board[row][col] = 0

  return False

def find_empty_cell(board):
  for i in range(9):
      for j in range(9):
          if board[i][j] == 0:
              return (i, j)
  return None

def print_board(board):
  for row in board:
      print(row)

def main():
  board = [[0 for _ in range(9)] for _ in range(9)]

  print("Enter the Sudoku puzzle (use '0' for empty cells):")
  for i in range(9):
      row = list(map(int, input().split()))
      board[i] = row

  if solve_sudoku(board):
      print("\nSolution:")
      print_board(board)
  else:
      print("\nNo solution exists.")

if __name__ == "__main__":
  main()
