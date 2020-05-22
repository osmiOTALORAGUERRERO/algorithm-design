class Chess:

    def createBoard(self,n):
        board = [[0 for i in range(n)] for j in range(n)]
        return board
    def __init__(self,n):
        self.board = self.createBoard(n)
        self.solutions = []
        self.size = n
        self.solutionCount = 0

    def isSafe(self,row,col):
        for i in range(col):
            if self.board[row][i] == 1:
                return False
        for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
            if self.board[i][j] == 1:
                return False
        for i,j in zip(range(row,self.size,1),range(col,-1,-1)):
            if self.board[i][j] == 1:
                return False
        return True

    '''close enough to O(n!)'''
    def solveBackTracking(self, col, show=False):
        if show:
            self.showBoardGui(self.board, False)

        if col >= self.size:
            if show : self.showBoardGui(self.board, True)
            self.solutions.append(self.board)
            return True

        for i in range(self.size):
            if self.isSafe(i,col):
                self.board[i][col] = 1
                if self.solveBackTracking(col+1, show) == True:
                    return True

            self.board[i][col] = 0

        return False
    def solveHorseMovement(self, col=0, row=1, moves=0, show=False):
        print(row, col, moves)
        if self.size <= 2:
            return False

        if moves == self.size:
            for row in self.board:
                print(row)
            print("")
            return True

        if moves == 0:
            self.board[row][col] = 1
            self.solveHorseMovement(col+1, row+2, moves+1, show)

        if moves+1 <= int(self.size/2):
            self.board[row][col] = 1
            if moves+1 != int(self.size/2):
                self.solveHorseMovement(col+1, row+2, moves+1, show)
            else:
                newCol = int((self.size/2)+1) if self.size%2 == 0 else int(self.size/2)
                self.solveHorseMovement(newCol ,0, moves+1, show)
        else:
            if self.size%2 == 0:
                self.board[row][col] = 1
                print(moves+1)
                # if self.size > 9
                newCol = (col-1) if (moves+1)%2 != 0 else (col+3)
                self.solveHorseMovement(newCol, row+2, moves+1, show)
            else:
                self.board[row][col] = 1
                self.solveHorseMovement(col+1, row+2, moves+1, show)

    def getAllSolutions(self,col):

        if col >= self.size:
            # self.solutions.append(self.board)
            self.solutionCount+=1
            # for row in self.board:
            #     print(row)
            # print("")
            return True

        solutionFound = False
        for i in range(self.size):
            if self.isSafe(i,col):
                self.board[i][col] = 1
                solutionFound = self.getAllSolutions(col+1)
            self.board[i][col] = 0

        return solutionFound


    def reportBackTrackingTime(self):
        import os
        from time import time
        start = time()
        self.solveBackTracking(0)
        end = time()
        with open(os.getcwd()+'\\files\\nqueen\\'+"Single_BackTrackingResults.txt","a") as file:
            file.write('Dimension : '+str(self.size)+' elapsed time: '+str(end-start)+"\n")

    def reportAllSolutionsTime(self):
        import os
        from time import time
        start = time()
        self.getAllSolutions(0)
        end = time()
        with open(os.getcwd()+'\\files\\nqueen\\'+"All_BackTrackingResults.txt","a") as file:
            file.write('Dimension : '+str(self.size)+' elapsed time: '+str(end-start)+"\n")


    def showBoardGui(self,board, final = False):
        import pygame
        import time

        def printSquare(n, squareSize, surface):
            blue = (0,0,255)
            colors = [(255,255,255), (100,100,100)]
            for row in range(n):
                colorIndex = row % 2
                for col in range(n):
                    square = (col*squareSize, row*squareSize, squareSize, squareSize)
                    if board[row][col] == 1:
                        surface.fill(blue,square)
                    else:
                        surface.fill(colors[colorIndex], square)
                    colorIndex = (colorIndex + 1) % 2

            pygame.display.update()

        pygame.init()
        n = len(board[0])
        surfaceSize = 500
        squareSize = surfaceSize // n
        surfaceSize = n * squareSize
        surface = pygame.display.set_mode((surfaceSize, surfaceSize))
        if not final:
            printSquare(n, squareSize, surface)
            pygame.time.delay(250)
        else:
            while True:
                ev = pygame.event.poll()
                if ev.type == pygame.QUIT:
                    break
                printSquare(n, squareSize, surface)
            pygame.quit()
