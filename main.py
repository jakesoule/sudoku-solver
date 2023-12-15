#visualizer for Sudoku solver
import sys
import pygame
import solve

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
pygame.init()

#constants
WINDOW_WIDTH, WINDOW_HEIGHT = 450, 450
GRID_SIZE = 9
CELL_SIZE = WINDOW_WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def drawBoard(screen):
    screen.fill(WHITE)
    
    for i in range(GRID_SIZE + 1):
        
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WINDOW_WIDTH, i * CELL_SIZE), 2)
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_HEIGHT), 2)
    
    font = pygame.font.Font(None, 36)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] != 0:
                numberText = font.render(str(board[i][j]), True, BLACK)
                screen.blit(numberText, (j * CELL_SIZE + 20, i* CELL_SIZE + 15))
        
#pygame setup
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sudoku Solver with Visualizer")
clock = pygame.time.Clock()

#main loop 
running = True
solved = False


def solveStepByStep(bo):
    empty = solve.findEmpty(bo)
    if empty is None:
        return True
    else:
        row, col = empty
        for i in range(1, 10):
            bo[row][col] = i
            drawBoard(screen)
            pygame.display.flip()
            clock.tick(10)
            pygame.event.pump()
            bo[row][col] = 0
            if solve.isValid(bo, i, row, col):
                bo[row][col] = i
                
                drawBoard(screen)
                pygame.display.flip()
                clock.tick(10)
                pygame.event.pump()
                
                if solveStepByStep(bo):
                    return True
                bo[row][col] = 0
                drawBoard(screen)
                pygame.display.flip()
                clock.tick(10)
                pygame.event.pump()
            clock.tick(10)
            pygame.event.pump()
        return False




while running:
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)
    
    if not solved:
        empty = solve.findEmpty(board)
        if empty is None:
            solved = True
        
        if solveStepByStep(board):
            drawBoard(screen)
            pygame.display.flip()
        else:
            solved = True
            
    
    


pygame.quit()
sys.exit()





def main():
    pass

if __name__ == '__main__':
    main()
    
