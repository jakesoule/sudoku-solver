#Jake Soule
#Python sudoku solver with visualizer
#Uses backtracking algorithm to efficiently solve the sudoku board

def main():
    board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]   
    
    printBoard(board)
    solve(board)
    print('******************')
    printBoard(board)
    




def printBoard(bo: list[list[int]]) -> None:
    
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - -')
        
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')
            
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + ' ', end='')
                
                
def solve(bo):
    empty = findEmpty(bo)
    
    if empty is None:
        return True

    else:
        row, col = empty
    
    for i in range(1, 10):
        if isValid(bo, i, row, col):
            bo[row][col] = i
            if solve(bo):
                return True
        
        bo[row][col] = 0
    
    return False 


        
                
                
#find next available empty square in sudoku board from left to right, descending order 
#if function returns None we can conclude that the board is solved               
def findEmpty(bo: list[list[int]]) -> tuple:
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return(i, j)
            
    return None

#check row, column and subgroup to ensure that number placement does not break the board
def isValid(bo: list[list[int]], value: int, row: int, col: int) -> bool:
    #check row
    for i in range(len(bo[0])):
        if bo[row][i] == value:
            return False
    
    #check column
    for i in range(len(bo)):
        if bo[i][col] == value:
            return False
    
    #check subgroup
    if row >= 0 and row <= 2:
        rowBox = (0, 1, 2)
    elif row >= 3 and row <= 5:
        rowBox = (3, 4, 5)
    else:
        rowBox = (6, 7, 8)
    
    if col >= 0 and col <= 2:
        colBox = (0, 1, 2)
    elif col >= 3 and col <= 5:
        colBox = (3, 4, 5)
    else: colBox = (6, 7, 8)
    
    
    for i in rowBox:
        for j in colBox:
            if bo[i][j] == value:
                return False
    
    return True





if __name__ == "__main__":
    main()