r = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]

def place(column, value):
    for i in range (5,-1, -1):
        if r[i][column] == 0:
            r[i][column] = value
            return i

def findInRow(value):
    for i in range (0, 6):
        count = 0
        for j in range (1, 7):
            if r[i][j] == value:
                if r[i][j-1] == value:
                    if count == 0:
                        count = 2
                    else:
                        count = count + 1
                if count == 4:
                    return True
            else:
                count = 0
    return False

def findInColumn(value):
    for j in range (0, 7):
        count = 0
        for i in range (1, 6):
            if r[i][j] == value:
                if r[i-1][j] == value:
                    if count == 0:
                        count = 2
                    else:
                        count = count + 1
                if count == 4:
                    return True
            else:
                count = 0
    return False

def findInDownDiagonal(value, row, col):
    count = 0
    j = col
    for i in range (row, 6):
        if r[i][j] == value:
            count = count + 1
            if count == 4:
                return True
            if j == 6:
                break
            else:
                j = j + 1
        else:
            break
    if row == 5 or col == 0:
        return False
    j = col - 1
    for i in range (row - 1, -1, -1):
        if r[i][j] == value:
            count = count + 1
            if count == 4:
                return True
            if j == 0:
                break
            else:
                j = j - 1
        else:
            break
    return False

def findInUpDiagonal(value, row, col):
    count = 0
    j = col
    for i in range (row, 6):
        if r[i][j] == value:
            count = count + 1
            if count == 4:
                return True
            if j == 0:
                break
            else:
                j = j - 1
        else:
            break
    if row == 5 or col == 6:
        return False
    j = col + 1
    for i in range (row-1, -1, -1):
        if r[i][j] == value:
            count = count + 1
            if count == 4:
                return True
            if j == 6:
                break
            else:
                j = j + 1
        else:
            break
    return False

print("Welcome to connect 4!")
print("The player who connects 4 in a row wins")
name1 = input("Enter player 1 name: ")
name2 = input("Enter player 2 name: ")
names = [name1, name2]
print("Hi "+name1+" and "+name2+"!")
gameOver = False
col = -1
x = 0
while (gameOver is not True):
    while (col < 0 or col > 8):
        col = int(input(names[x]+", pick your column: "))
        col = col - 1
    row = place(col, x+1)
    for i in range (0, 6):
        print(r[i])
    gameOver = findInRow(x+1) or findInColumn(x+1) or findInUpDiagonal(x+1, row, col) or findInDownDiagonal(x+1, row, col)
    if gameOver:
        print(names[x], "won!")
    if x == 0:
        x = 1
    else:
        x = 0
    col = -1