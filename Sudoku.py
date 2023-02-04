from Logic import solveSudoku, SIZE_OF_BOARD

#input your board
#default boards are in sudoku_boards.txt file
board = []
for i in range(SIZE_OF_BOARD):
  row = []
  digits = input()
  for sign in digits:
    row.append(int(sign))
  board.append(row)


print(solveSudoku(board))
