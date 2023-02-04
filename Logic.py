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
    for col in range(SIZE_OF_BOARD):
        listColumn=[]
        for i in range(SIZE_OF_BOARD):
            listColumn.append(board[i][col])
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


def emptySquare(board):
    empty = 0
    for row in board:
        for digit in row:
            if digit == 0:
                empty+=1
    return empty


def notUsedDigits(square):
    notUsed=[1,2,3,4,5,6,7,8,9]
    for digit in square:
        if digit == 0:
            continue
        notUsed.pop(notUsed.index(digit))
    return notUsed


def solveSudoku(board):
    for row in range(SIZE_OF_BOARD):
        notUsed = notUsedDigits(board[row])
        if not notUsed:
            continue
        for digit in range(SIZE_OF_BOARD):
            if board[row][digit] != 0:
                continue
            for notUsedDigit in notUsed:
                board[row][digit] = notUsedDigit
                if isValidSudoku(board):
                    notUsed.pop(notUsed.index(notUsedDigit))
                    break
    return board
