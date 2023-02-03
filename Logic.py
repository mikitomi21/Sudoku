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

