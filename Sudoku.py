SIZE_OF_SQUARE=3
SIZE_OF_BOARD=9

def checkList(listSu):
    listSu = sorted(listSu)
    for i in range(len(listSu)-1):
        if listSu[i]==0:
            continue
        if listSu[i]==listSu[i+1]:
            return False
    return True

def isValidSudoku(board):
    #check rows
    for row in board:
        if not checkList(row):
            return False

    #check columns
    for row in board:
        listColumn=[]
        for i in range(SIZE_OF_BOARD):
            listColumn.append(row[i])
        if not checkList(listColumn):
            return False

    # check squares
    for i in range(SIZE_OF_BOARD):
        listSquare = []
        for j in range(SIZE_OF_SQUARE):
            listSquare += board[int(i/3)*3+j%3][(i%3)*3:(i%3)*3+3]
        if not checkList(listSquare):
            return False

    return True


board = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]]

print(isValidSudoku(board))