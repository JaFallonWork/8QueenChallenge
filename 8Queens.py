import random
import numpy as np
from copy import deepcopy
import requests
# url='https://lf8q0kx152.execute-api.us-east-2.amazonaws.com/default/computeFitnessScore'



# Initial Iterations

def display(Board):
    linestring = ""
    x = 0
    y = 0
    while( x < 8):
        print("_________________")
        linestring = "|"
        while( y < 8):
            if(Board[x][y] == 0):
                linestring = linestring+" |"
            elif(Board[x][y] == 1):
                linestring = linestring+"Q|"
            y = y + 1
        print(linestring)
        y = 0
        x = x + 1
    print("_________________")

def reformat(Board):
    # Board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    newBoard = []
    z = 0
    q = 0
    for index in Board:
        for x in index:

            if(Board[q][z] == 1):
                newBoard.append(z)
            z = z + 1

            if(z == 8):
                z = 0
        q = q + 1

    return(newBoard)

class Iteration:
    
    # Initialize empy board
    def __init__(self, Board, Score):
      self.Board = Board
      self.Score = Score
      # self.score = score

    def plotboard(self):

        queen1 = []
        queen2 = []
        queen3 = []
        queen4 = []
        queen5 = []
        queen6 = []
        queen7 = []
        queen8 = []
        queens = [queen1,queen2,queen3,queen4,queen5,queen6,queen7,queen8]
        Board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

        for each in queens:

            x = random.randrange(0,8)
            y = random.randrange(0,8)
            # print("X: ",x)
            # print("Y: ", y)
            each.append(x)
            each.append(y)

        for each in queens:

            YCord = each[0]
            XCord = each[1]

            if(Board[XCord][YCord] != 1):
                Board[XCord][YCord] = 1
            else:
                # If 2 have the same coordinate, call again
                while(Board[XCord][YCord] == 1):
                    YCord = random.randrange(0,8)
                    XCord = random.randrange(0,8)
                    if(Board[XCord][YCord] == 1):
                        pass
                    else:
                        Board[XCord][YCord] = 1
                        break

        self.Board = Board
        return (self.Board) 

    def scoreBoard(self):
        # Score = 0 - 64
        # 0 all collide
        # 64 is a solved puzzle
        temScore = 0
        indexX = 0
        indexY = 0
        col1 = 0
        col2 = 0 
        col3 = 0
        col4 = 0

        for x in self.Board:   
            for y in self.Board:
                # print(self.Board[indexX][indexY])

                # If the Board has a Queen at this X,Y position, then score it.
                if(self.Board[indexY][indexX] == 1):
                    cIndexX = indexX
                    cIndexY = indexY
                    # Check X Left
                    # X coordinate in not against wall
                    if(indexX != 0 ):
                        while(cIndexX != 0):
                            cIndexX = cIndexX -1
                            if(self.Board[cIndexY][cIndexX] == 1):
                                break
                                
                            elif(cIndexX == 0 & self.Board[cIndexY][cIndexX] != 1):
                                temScore = temScore + 1

                    # X coordinate is aginst the wall
                    else:
                        temScore = temScore+1  
                    # Check X Right
                    cIndexX = indexX
                    cIndexY = indexY
                    # Check X Left
                    # X coordinate in not against wall
                    if(indexX != 7 ):
                        while(cIndexX != 7):
                            cIndexX = cIndexX +1

                            if(self.Board[cIndexY][cIndexX] == 1):
                                break
                              
                            if(cIndexX == 7):
                                if(self.Board[cIndexY][cIndexX] == 0):
                                    temScore = temScore + 1
                                else:
                                    break

                    # X coordinate is aginst the wall
                    else:
                        temScore = temScore+1
                    # Check Y Up
                    cIndexX = indexX
                    cIndexY = indexY

                    # Y coordinate in not against wall
                    if(indexY != 0 ):
                        while(cIndexY != 0):
                            cIndexY = cIndexY -1

                            if(self.Board[cIndexY][cIndexX] == 1):
                                break
                              
                            if(cIndexY == 0):
                                if(self.Board[cIndexY][cIndexX] == 0):
                                    temScore = temScore + 1
                                else:
                                    break

                    # X coordinate is aginst the wall
                    else:
                        temScore = temScore+1
                    # Check Y Down
                    cIndexX = indexX
                    cIndexY = indexY

                    # Y coordinate in not against wall
                    if(indexY != 7 ):
                        while(cIndexY != 7):
                            cIndexY = cIndexY +1

                            if(self.Board[cIndexY][cIndexX] == 1):
                                break
                              
                            if(cIndexY == 7):
                                if(self.Board[cIndexY][cIndexX] == 0):
                                    
                                    temScore = temScore + 1
                                else:
                                    break

                    # X coordinate is aginst the wall
                    else:
                        temScore = temScore+1

                    # Check Diagonal ( X + 1) & ( Y + 1) ( To bottom right )
                    cIndexX = indexX
                    cIndexY = indexY           

                    if(indexY != 7 and cIndexX != 7):
                        while(cIndexY != 7 and cIndexX !=7):
                            cIndexY = cIndexY +1
                            cIndexX = cIndexX +1


                            if(self.Board[cIndexY][cIndexX] == 1):
                                col1 = col1 + 1
                                break
                            
                    # X or Y coordinate is aginst the wall
                    else:
                        pass

                    # Check Diagonal ( X + 1) & ( Y - 1)
                    cIndexX = indexX
                    cIndexY = indexY
                    
                    if(indexY != 0 and cIndexX != 7):
                        while(cIndexY != 0 and cIndexX !=7):
                            cIndexY = cIndexY -1
                            cIndexX = cIndexX +1

                            if(self.Board[cIndexY][cIndexX] == 1):
                                col2 = col2 + 1
                                break
                            
                    # X or Y coordinate is aginst the wall
                    else:
                        pass
                    # Check Diagonal ( X - 1) & ( Y + 1)
                    cIndexX = indexX
                    cIndexY = indexY
                    
                    if(indexY != 7 and cIndexX != 0):
                        while(cIndexY != 7 and cIndexX !=0):
                            cIndexY = cIndexY + 1
                            cIndexX = cIndexX - 1

                            if(self.Board[cIndexY][cIndexX] == 1):
                                col3 = col3 + 1
                                break
                            
                    # X or Y coordinate is aginst the wall
                    else:
                        pass
                    # Check Diagonal ( X - 1) & ( Y - 1)
                    cIndexX = indexX
                    cIndexY = indexY
                    
                    if(indexY != 0 and cIndexX != 0):
                        while(cIndexY != 0 and cIndexX !=0):
                            cIndexY = cIndexY - 1
                            cIndexX = cIndexX - 1

                            if(self.Board[cIndexY][cIndexX] == 1):
                                col4 = col4 + 1
                                break
                            
                    # X or Y coordinate is aginst the wall
                    else:
                        pass

                indexY = indexY+1
                if(indexY == 8):
                    indexY = 0
            
            indexX = indexX+1
        col1 = 8 - col1
        col2 = 8 - col2
        col3 = 8 - col3
        col4 = 8 - col4
        # Add scores
        temScore = temScore +col1+col2+col3+col4  
        self.Score = temScore
        return(self.Score)
    
def CrossMutate(board1, board2):

    newBoard = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    x1 = 0
    y1 = 0
    aListx = []
    aListy = []
    bListx = []
    bListy = []

    # Combine Top Instances
    for x in board1:   
        for each in x:
            if(each == 1):
                aListx.append(x1)
                aListy.append(y1)
                
            y1 = y1 + 1
            if(y1 == 8):
                y1 = 0
        x1 = x1 + 1

    x2 = 0
    y2 = 0
    # Combine Top Instances
    for x in board2:   
        for each in x:
            if(each == 1):
                bListx.append(x2)
                bListy.append(y2)
            y2 = y2 + 1
            if(y2 == 8):
                y2 = 0
        x2 = x2 + 1

    # Build new board
    # 50/50 split ( Randomize Split locations)
    randSplit = random.sample(range(0, 8), 8)
    index = 0
    newXCords = []
    newYCords = []

    for x in randSplit:
        #print(x)
        if(index < 4):  
            newXCords.append(aListx[x])
            newYCords.append(aListy[x])
            index = index + 1
            
        if(index >= 4 and index < 8):
            newXCords.append(bListx[x])
            newYCords.append(bListy[x])   
            index = index + 1
            
        if(index == 8):
            index = 8
            break

    # Map Coordinates to board
    index = 0
    for each in newXCords:
        x1 = newXCords[index]
        y1 = newYCords[index]

        if(newBoard[x1][y1] != 1):
            newBoard[x1][y1] = 1

        # Mutate if two of the same spots
        else:
            while(newBoard[x1][y1] == 1):
                x1 = random.randrange(0,8)
                y1 = random.randrange(0,8)
                if(newBoard[x1][y1] == 1):
                    pass
                else:
                    newBoard[x1][y1] = 1
                    break

        index = index + 1
        if(index == 8 ):
            break

    # Add Random chance to Mutate a random element 
    mutateRate = random.randrange(0,99)
    # 10% for now
    Q = True
    T = True
    if(mutateRate < 9):
        # TODO Replace Random 1 with 0
        while(Q == True):
            randomX = random.randrange(0,8)
            randomY = random.randrange(0,8)
            
            if(newBoard[randomX][randomY] == 1):
                newBoard[randomX][randomY] = 0
                while(T == True):
                    x1 = random.randrange(0,8)
                    y1 = random.randrange(0,8)
                    if(newBoard[x1][y1] == 1):
                        # newBoard[x1][y1] = 1
                        pass
                    else:
                        newBoard[x1][y1] = 1
                        T = False
                        Q = False    
            else:
                pass
        # Input in Random 1 value
    return(newBoard)

def main():
    # Initial empty state of board
    Board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    # topscore = 0
    # while(topscore != 64):

    epoch = 1
    force_mutate = 0    # Needed if it gets stuck at local minima
    hard_force = 0      # Odds both of complete mutations (Both Parents)

    # Initialize the population ( Population = 4 )
    It1 = Iteration(Board, 0)
    It1.plotboard()
    It2 = Iteration(Board, 0)
    It2.plotboard()
    It3 = Iteration(Board, 0)
    It3.plotboard()
    It4 = Iteration(Board, 0)
    It4.plotboard()
    # Score the initial population
    score1 = It1.scoreBoard()
    score2 = It2.scoreBoard()
    score3 = It3.scoreBoard()
    score4 = It4.scoreBoard()

    scorelist = [score1,score2,score3,score4]

    # Find top 2 members of population
    top_score = max(scorelist)
    top_index = scorelist.index(top_score)
    scorelist[top_index] = 0
    top_score2 = max(scorelist)
    top_index2 = scorelist.index(top_score2)
    scorelist[top_index2] = 0
    top2 = [top_index, top_index2]

    # Cross and Mutate top 2

    if(top2[0] == 0):
        # Iteration 1 is top
        if(top2[1] == 1):
            ChildBoard = CrossMutate(It1.Board, It2.Board)
            ItCT = Iteration(It2.Board,0)

        if(top2[1] == 2):
            ChildBoard = CrossMutate(It1.Board, It3.Board)
            ItCT = Iteration(It3.Board,0)
        
        if(top2[1] == 3):
            ChildBoard = CrossMutate(It1.Board, It4.Board)
            ItCT = Iteration(It4.Board,0)
            
    if(top2[0] == 1):
        # Iteration 2 is top
        if(top2[1] == 0):
            ChildBoard = CrossMutate(It2.Board, It1.Board)
            ItCT = Iteration(It2.Board,0)

        if(top2[1] == 2):
            ChildBoard = CrossMutate(It2.Board, It3.Board)
            ItCT = Iteration(It2.Board,0)

        if(top2[1] == 3):
            ChildBoard = CrossMutate(It2.Board, It4.Board)
            ItCT = Iteration(It2.Board,0)

    if(top2[0] == 2):
        # Iteration 3 is top
        if(top2[1] == 0):

            ChildBoard = CrossMutate(It3.Board, It1.Board)
            ItCT = Iteration(It1.Board,0)
        if(top2[1] == 1):
            ChildBoard = CrossMutate(It3.Board, It2.Board)
            ItCT = Iteration(It2.Board,0)
        if(top2[1] == 3):
            ChildBoard = CrossMutate(It3.Board, It4.Board)
            ItCT = Iteration(It4.Board,0)

    if(top2[0] == 3):
        # Iteration 4 is top

        if(top2[1] == 0):
            ChildBoard = CrossMutate(It4.Board, It1.Board)
            ItCT = Iteration(It1.Board,0)
        if(top2[1] == 1):
            ChildBoard = CrossMutate(It4.Board, It2.Board)
            ItCT = Iteration(It2.Board,0)
        if(top2[1] == 2):
            ChildBoard = CrossMutate(It4.Board, It3.Board)
            ItCT = Iteration(It3.Board,0)
        
    # Score Child Board    
    ItC = Iteration(ChildBoard, 0)
    scoreC = ItC.scoreBoard()

    # Win condition and future modifications
    while(True):
        if(scoreC == 64):
            # This is a pattern
            print("A solution has been found: ")
            break
        else:
            epoch = epoch + 1
            # Number of iterations
            print("Epoch: ", epoch)
            ItList = []

            # 4 Children created
            nextChildBoard1 = CrossMutate(ItC.Board, ItCT.Board)
            ItC1 = Iteration(nextChildBoard1, 0)


            ItList.append(ItC1)

            nextChildBoard2 = CrossMutate(ItC.Board, ItCT.Board)
            ItC2 = Iteration(nextChildBoard2, 0)

            ItList.append(ItC2)
        
            nextChildBoard3 = CrossMutate(ItC.Board, ItCT.Board)
            ItC3 = Iteration(nextChildBoard3, 0)

            ItList.append(ItC3)
        
            nextChildBoard4 = CrossMutate(ItC.Board, ItCT.Board)
            ItC4 = Iteration(nextChildBoard4, 0)

            ItList.append(ItC4)

            maxlist =[]
            for each in ItList:
                maxlist.append(each.scoreBoard())

            It_Max = max(maxlist)
            max_index = maxlist.index(It_Max)

            force_mutate = force_mutate + 1
            hard_force = hard_force + 1
            print(scoreC)
            # Take the strongest of the 4 children to cross
            if(max_index == 0):
                ItCT = Iteration(ItC1.Board, 0)
            
            if(max_index == 1):
                ItCT = Iteration(ItC2.Board, 0)
            
            if(max_index == 2):
                ItCT = Iteration(ItC3.Board, 0)
        
            if(max_index == 3):
                ItCT = Iteration(ItC4.Board, 0)           
                           
            # Keep top parent sequence
            if(scoreC < It_Max):
                scoreC = ItC.scoreBoard()
                force_mutate = 0
                hard_force = 0

                if(max_index == 0):
                    ItC = Iteration(ItC1.Board, 0)
                
                if(max_index == 1):
                    ItC = Iteration(ItC2.Board, 0)
                
                if(max_index == 2):
                    ItC = Iteration(ItC3.Board, 0)
            
                if(max_index == 3):
                    ItC = Iteration(ItC4.Board, 0)
            else:
                pass

            if(force_mutate == 300):       # If stalls at local minima for 200 Epochs , a completly mutated child inserted
                ItCT = Iteration(Board, 0)
                ItCT.plotboard() # New Plot
                force_mutate = 0        # Reset
            if(hard_force == 600):       # If stalls at local minima for 600 Epochs , Chromosome is completly shuffled
                ItC = Iteration(Board, 0)
                ItC.plotboard() # New Plot
                scoreC = ItC.scoreBoard()
                force_mutate = 0        # Reset 
                hard_force = 0          # Reset
    display(ItC.Board)

    # Desired output format
    form1 = reformat(ItC.Board)



    test1 = (str(form1).strip('[]'))
    params = test1.replace(',', '')

    print(params)

    #x=requests.post(url,json={"qconfig":params,"userID":843858,"githubLink":"<<git hub link>>"})
    #print(x.text)




if __name__ == "__main__":
    main()

