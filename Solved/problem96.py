#!/usr/bin/python2
import sys
import random





def TransposeMatrix(Matrix):
    NewMatrix=[[],[],[],[],[],[],[],[],[]]
    for i in xrange(9):
        for j in xrange(9):
             if i+1 in Matrix[j]:
                 NewMatrix[i].append(j+1)
    return NewMatrix
        
def Matrixify(PossibleList,housetype,number):
#Make a matrix from the possibleList
    Matrix=[]
    if housetype=="block":
        for x in xrange(3):
            for y in xrange(3):
                Matrix.append(PossibleList[(3*(number%3)+x)*9+(3*(number/3)+y)])
        return Matrix
            
    elif housetype=="row":
        for y in xrange(9):
            Matrix.append(PossibleList[number*9+y])
        return Matrix
            
    elif housetype=="collumn":
        for x in xrange(9):
            Matrix.append(PossibleList[x*9+number])
        return Matrix
        
def DeMatrixify(PossibleList,Matrix,housetype,number):
    if housetype=="block":
            
        for x in xrange(3):
            for y in xrange(3):
                PossibleList[(3*(number%3)+x)*9+(3*(number/3)+y)]=Matrix[x*3+y]
        return PossibleList
            
    elif housetype=="row":
        for y in xrange(9):
            PossibleList[number*9+y]=Matrix[y]
        return PossibleList
            
    elif housetype=="collumn":
        for x in xrange(9):
            PossibleList[x*9+number]=Matrix[x]
        return PossibleList
    
  

def CheckMissplacements(Board,CellNum=-1, Solver = 0):
    #checks if the numbers is correctly placed on the board so the solving can begin. e.g. There must not be the same number in the same block, row or collum twice.
#    return 0 if no errors, 1 if error in blocks, 2 if error in rows, and 3 if error in collums.
    #Second argument is a cell number. If given, we only check if its row collumn and block is valid
    #If the third argument given is 1,we return -1 on error
    #Check the blocks
    for x in xrange(3):
        for y in xrange(3):
            if not CellNum==-1:
                x=CellNum%3
                y=CellNum/27
            Blocknumbers=[]
            for i in xrange(3):
                for j in xrange (3):
                    if Solver == 0:
                        Blocknumbers+=[Board[(3*x+i)*9+(3*y+j)]]

                    else:
                        Blocknumbers+=[Board[(3*x+i)*9+(3*y+j)][0]]
            for l in xrange(1,10):
                if (Blocknumbers.count(l) > 1):
                    if(Solver == 0):
                        return (1, l, x, y, Blocknumbers.index(l))
                    else:
                        return -1
            if not CellNum==-1:
                break
        if not CellNum==-1:
            break
    # Check Rows
    for x in xrange(9):
        if not CellNum==-1:
            x=CellNum/9
        Rownumbers = []
        for y in xrange(9):
            if Solver == 0:
                Rownumbers+=[Board[x*9+y]]

            else:
                Rownumbers+=[Board[x*9+y][0]]

        for l in xrange(1,10):
            if (Rownumbers.count(l) > 1):
                if (Solver == 0):
                    return (2, l, x, y, Rownumbers.index(l))
                else:
                    return -1
                    
        if not CellNum==-1:
            break
    #Check Collums
    for y in xrange(9):
        if not CellNum==-1:
            y=CellNum%9
        Collumnumbers = []
        for x in xrange(9):
            if Solver == 0:
                Collumnumbers+=[(Board[x*9+y])]

            else:
                Collumnumbers+=[(Board[x*9+y][0])]
        for l in xrange(1,10):
            if (Collumnumbers.count(l) > 1):
                if Solver == 0:
                    return (3, l, y, x, Collumnumbers.index(l))
                else:
                    return -1
        if not CellNum==-1:
            break

    return 0

def FillCandidates(Board,OldBoard=0,CandList=0):
    #Fill in naked singles and makes a list of possible values for each cell
    #Make a list of changed cells

    if not OldBoard==0:
        CellList=[]
        CheckList=[]
        for i in xrange(81):
            if not Board[i]==OldBoard[i]:
                CellList.append(i)

        for l in CellList:
            row=l/9
            collumn=l%9
            boxX=l%3
            boxY=l/27
            for i in xrange(3):
                for j in xrange (3):
                    number=(3*boxX+i)*9+(3*boxY+j)
                    if not number in CheckList:
                        CheckList.append(number)
            for y in xrange(9):
                number=row*9+y
                if not number in CheckList:
                    CheckList.append(number)
                    
            for x in xrange(9):
                number=x*9+collumn
                if not number in CheckList:
                    CheckList.append(number)
    PossibleList=[""] * 81
        
    for i in xrange(81):
        if not OldBoard==0:
            if not i in CheckList:
                PossibleList[i]=CandList[i]
                continue
        if not Board[i][0] =="":
            PossibleList[i] = [Board[i][0]]
        else:
            PossibleList[i] = []
            for j in xrange(1,10):
                Board[i][0] = j
                if not CheckMissplacements(Board,i,1) == -1:
                    PossibleList[i].append(j)
            if len(PossibleList[i]) == 1:
                Board[i][0] = PossibleList[i][0]
                Board[i][1] = 1
            else:
                Board[i][0] = ""
    return (PossibleList)





def FindHiddenSingles(PossibleList,Board):
    #Check each row, collumn and block, and if a number only is candidate in one cell, it means that it must be that cell
    #Blocks:
    Changed = 0
    for x in xrange(3):
        for y in xrange(3):
            for num in xrange(1, 10): #check each number in this block
                cellList = []
                for i in xrange(3):
                    for j in xrange(3):
                        if PossibleList[(3*x+i)*9+(3*y+j)].count(num) == 1:
                            cellList.append((3*x+i)*9+(3*y+j))
                if len(cellList) == 1:
                    if Board[cellList[0]][0] == "":
                        Board[cellList[0]][0] = num
                        Board[cellList[0]][1] = 1
                        PossibleList[cellList[0]] = [num]
                        Changed = 1
                        #print "blok, num :"+str(num)+" celle "+str(cellList[0])
    #rows
    for x in xrange(9):
        for num in xrange(1,10):
            cellList = []
            for y in xrange(9):
                if PossibleList[x*9+y].count(num) == 1:
                    cellList.append(x*9+y)
            if len(cellList) == 1:
                if Board[cellList[0]][0] == "":
                    Board[cellList[0]][0] = num
                    Board[cellList[0]][1] = 1
                    PossibleList[cellList[0]] = [num]
                    Changed = 1
                    #print "raekke, num :"+str(num)+" celle"+str(cellList[0])
    #Collumns
    for y in xrange(9):
        for num in xrange(1,10):
            cellList = []
            for x in xrange(9):
                if PossibleList[x*9+y].count(num) == 1:
                    cellList.append(x*9+y)
            if len(cellList) == 1:
                if Board[cellList[0]][0] == "":
                    Board[cellList[0]][0] = num
                    Board[cellList[0]][1] = 1
                    PossibleList[cellList[0]] = [num]
                    Changed = 1

                    #print "kollone, num :"+str(num)+" celle"+str(cellList[0])
    return Changed

def FindNakedSingles(PossibleList,Board,Draw=1):
    check = 1
    Changed = 0
    while check == 1:
        check = 0
        for i in xrange(81):
            if not Board[i][1] == 1:
                if len(PossibleList[i]) == 1: #We have found a naked single
                    Changed = 1
                    Board[i][0] = PossibleList[i][0]
                    Board[i][1] = 1
                    Changed = 1
                    check = 1
    return Changed


def FindNakedPairsTripplesQuads(PossibleList):
    #If two cells in a group (row, collum, block) contains the same two candidates, these candidates can be removed from the rest of the cells in the group
    #loop through all cells, searching for a cell with two candidates
    Changed=0
    for checking in xrange(2,5):
        for i in xrange(81):
            if len(PossibleList[i]) == checking:
                current = PossibleList[i]
                #if we find one, search through block, row and collum for the same pair.
                row = i%9
                collumn = i/9
                #search through row
                cellList = [i]
                for l in xrange(9):
                    if not row+l*9 == i:
                        numbersfound = 0
                        for candidate in current:
                            if PossibleList[row+l*9].count(candidate) > 0:
                                numbersfound += 1
                        if numbersfound == len(PossibleList[row+l*9]):
                            cellList.append(row+l*9)

                if len(cellList) == checking: #we have found a naked pair/tripple/quad.
                    for l in xrange(9):
                        if not cellList.count(row+l*9) > 0: #check if we should delete in this cell
                            for candidate in current:
                                if PossibleList[row+l*9].count(candidate) == 1:
                                    PossibleList[row+l*9].remove(candidate)
                                    Changed = 1
                #search through collumn
                cellList = [i]
                for l in xrange(9):
                    if not collumn*9+l==i:
                        numbersfound=0
                        for candidate in current:
                            if PossibleList[collumn*9+l].count(candidate)>0:
                                numbersfound+=1
                        if numbersfound==len(PossibleList[collumn*9+l]):
                            cellList.append(collumn*9+l)

                if len(cellList)==checking: #we have found a naked pair/tripple/quad.
                    for l in xrange(9):
                        if not cellList.count(collumn*9+l)>0: #check if we should delete in this cell
                            for candidate in current:
                                if PossibleList[collumn*9+l].count(candidate)==1:
                                    PossibleList[collumn*9+l].remove(candidate)
                                    Changed=1
                #search through blocks
                cellList=[i]
                    #find out whick block we belongs to
                blockX=collumn/3
                blockY=row/3
                for x in xrange(3):
                    for y in xrange(3):
                        if not (blockX*3+x)*9+(blockY*3+y)==i:
                            numbersfound=0
                            for candidate in current:
                                if PossibleList[(blockX*3+x)*9+(blockY*3+y)].count(candidate)>0:
                                    numbersfound+=1
                            if numbersfound==len(PossibleList[(blockX*3+x)*9+(blockY*3+y)]):
                                cellList.append((blockX*3+x)*9+(blockY*3+y))

                if len(cellList)==checking: #we have found a naked pair/tripple/quad.
                    for x in xrange(3):
                        for y in xrange(3):
                            if not cellList.count((blockX*3+x)*9+(blockY*3+y))>0:
                                for candidate in current:
                                    if PossibleList[(blockX*3+x)*9+(blockY*3+y)].count(candidate)==1:
                                        PossibleList[(blockX*3+x)*9+(blockY*3+y)].remove(candidate)
                                        Changed=1
    return Changed






def FindHiddenPairsTripplesQuads(PossibleList):
    Changed=0
    for housetype in ["block","row","collumn"]:
        for i in xrange(9):
            Matrix=Matrixify(PossibleList,housetype,i)
            Matrix=TransposeMatrix(Matrix)
            for checking in xrange(2,5):
                ChangedTemp=0
                for j in xrange(9):
                    check=0
                    if len(Matrix[j])==checking:
                        check=1
                        current=Matrix[j]
                        cellList=[j]
                        for l in xrange(9):
                            if not l==j:
                                numbersfound=0
                                for candidate in current:
                                    if Matrix[l].count(candidate)>0:
                                        numbersfound+=1
                                if numbersfound==len(Matrix[l]):
                                    cellList.append(l)
                    if check:
                        if len(cellList)==checking: 
                            #we have found a hidden pair/tripple/quad.
                            for l in xrange(9):
                                if not cellList.count(l) >0:
                                    for candidate in current:
                                        if Matrix[l].count(candidate)==1:

                                            Matrix[l].remove(candidate)
                                            Changed=1
                                            ChangedTemp=1
            if ChangedTemp:
                PossibleList=DeMatrixify(PossibleList,TransposeMatrix(Matrix),housetype,i)
    return Changed
    

           
       
    


            
def FindPointingPairs(PossibleList):
    #If a candidate value inside a box only exists in one row or collumn, it can be removed from the same row or collumn in other boxes.
    Changed=0
    for x in xrange(3):
        for y in xrange(3):
            for num in xrange(1,10):
                CellList=[]
                for i in xrange(3):
                    for j in xrange(3):
                        if PossibleList[(3*x+i)*9+(3*y+j)].count(num)==1:
                            CellList.append((3*x+i,3*y+j))
                if len(CellList)==3 or len(CellList)==2:
                    #Check if number exist only in the same row or collumn
                    SameRow=1
                    SameCollumn=1
                    row=CellList[0][0]
                    collumn=CellList[0][1]

                    for cell in CellList[1:]:
                        if not cell[0]==row:
                            SameRow=0
                        if not cell[1]==collumn:
                            SameCollumn=0
                    if SameRow: #if the candidate only exist in the same row, delete candidate in the rest of the row
                        #Get coullmns we shouldn't delete in
                        skipThese=[]
                        for cell in CellList:
                            skipThese.append(cell[1])
                        #Delete in all others
                        for thiscollumn in xrange(9):
                            if not skipThese.count(thiscollumn)==1:
                                if PossibleList[row*9+thiscollumn].count(num)==1:
                                    PossibleList[row*9+thiscollumn].remove(num)
                                    Changed=1
                        #print "Pointing Pair at:"
                        #for cell in CellList:
                        #    print cell
                        #print "Nummer="+str(num)
                    elif SameCollumn: #if the candidate only exist in the same row, delete candidate in the rest of the row
                        skipThese=[]
                        for cell in CellList:
                            skipThese.append(cell[0])
                        #Delete in all others
                        for thisrow in xrange(9):
                            if not skipThese.count(thisrow)==1:
                                if PossibleList[thisrow*9+collumn].count(num)==1:
                                    PossibleList[thisrow*9+collumn].remove(num)
                                    Changed=1
                        #print "Pointing Pair at:"
                        #for cell in CellList:
                        #    print cell
                        #print "Nummer="+str(num)
    return Changed



def PrepareBoard(Board1,Draw = 1):
    #Make a copy of Board1 and put in board (this is neccesary for our bruteforcing
    Board=[]
    for i in xrange(81):
        Board.append([])
        for l in xrange (3):
            Board[i].append(Board1[i][l])
    if CurrentState[0]:
        PossibleList=FillCandidates(Board)
    else:
        #We fill all non-user entered cells with all candidates
        PossibleList=[""]*81
        for i in xrange(81):
            if Board[i][1] == 1:
                PossibleList[i] = [Board[i][0]]
            else:
                PossibleList[i] = [1,2,3,4,5,6,7,8,9]
    while True:
    
        OldBoard=[] #Make a copy of the board for comparrison
        for i in xrange(81):
            OldBoard.append([])
            for l in xrange (3):
                OldBoard[i].append(Board[i][l])
        while True:
            if Graphics and GetKeyEventsWSolving()==-1:
                return -2
            if CurrentState[5]:
                FindPointingPairs(PossibleList)
            if CurrentState[1]:
                naked=FindNakedSingles(PossibleList,Board)
            else:
                naked=0
            if CurrentState[2]:
                hidden=FindHiddenSingles(PossibleList,Board)
            else:
                hidden=0
            #SolvingBoard=checker[0]
            if Verbose:
                if CurrentState[1]:
                    print "naked : "+str(naked)
                if CurrentState[2]:
                    print "CrossCheck: "+str(hidden)

            if not (hidden==1 or naked==1):
                break
            else:
                if CurrentState[0]:
                    if Graphics and Draw:
                        DrawSolvingBoard(PossibleList)
                    if not Board==OldBoard:
                        PossibleList=FillCandidates(Board,OldBoard,PossibleList)
                if CurrentState[3]:
                    FindNakedPairsTripplesQuads(PossibleList)
                if CurrentState[4]:
                    FindHiddenPairsTripplesQuads(PossibleList)
                        
        while True:
            #copy PossibleList to tempboard
            TempList=[]
            for cell in xrange(len(PossibleList)):
                TempList.append([])
                for l in xrange(len(PossibleList[cell])):
                    TempList[cell].append(PossibleList[cell][l])
            if CurrentState[3]:        
                NakedGroups=FindNakedPairsTripplesQuads(PossibleList)
            else:
                NakedGroups=0
            if CurrentState[4]:
                HiddenGroups=FindHiddenPairsTripplesQuads(PossibleList)

            else:
                HiddenGroups=0
            if CurrentState[5]:
                PointingPairs=FindPointingPairs(PossibleList) #Should Be Working
            else:
                PointingPairs=0
            if  (TempList==PossibleList):
                break
            else:
                if Verbose:
                    print "Found Naked or Hidden groups or pointing pairs"
                if Graphics and Draw:
                    DrawSolvingBoard(PossibleList)
        if CurrentState[1]:
            naked=FindNakedSingles(PossibleList,Board)
        else:
            naked=0
        if CurrentState[2]:
            hidden=FindHiddenSingles(PossibleList,Board)
        else:
            hidden=0
        if Verbose:
            if CurrentState[1]:
                print "naked : "+str(naked)
            if CurrentState[2]:
                print "CrossCheck: "+str(hidden)
        if not(hidden==1 or naked==1):
            break
        else:
            if CurrentState[0]:        
                PossibleList=FillCandidates(Board)

    return(Board,PossibleList)

def CheckFaultyBoard(PossibleList):
    for candidates in PossibleList:
        if len(candidates)==0:
            return -1

    return 0

def BruteForceRandom(PossibleList,SolvingBoard,tryborder):
    #This is a specialised bruteforce. We select a random nonsolved field.
    #At this field we fill in the first candidate.
    #We try to solve using logic. If it fails we move on to the next candidate and tries again.
    #If we can't solve with any of the candidates, we select another field and does the same, but now with both fields.
    #We do this only down to 5 levels. It is probabaly more effective to use the standard bruteforce if we haven't solved at this point
    #(5 levels really means ~5^5)= tries
    #A list containing the cells we are trying on
    

    testing=0
    CellList=[]
    for i in xrange(4):
        while True:
            RandomCell=random.randint(0,80)
            if not SolvingBoard[RandomCell][1]==1 or RandomCell in CellList:
                CellList.append(RandomCell)
                break
    
    #We have now selected the cells to try on
    
                
    for candidate0 in [""]+PossibleList[CellList[0]]:
        SolvingBoard[CellList[0]][0]=candidate0
        if not candidate0=="":
            SolvingBoard[CellList[0]][1]=1
        for candidate1 in [""]+PossibleList[CellList[1]]:
            SolvingBoard[CellList[1]][0]=candidate1
            if not candidate1=="":
               SolvingBoard[CellList[1]][1]=1
            for candidate2 in [""]+PossibleList[CellList[2]]:
                SolvingBoard[CellList[2]][0]=candidate2
                if not candidate2=="":
                    SolvingBoard[CellList[2]][1]=1
                for candidate3 in [""]+PossibleList[CellList[3]]:
                    SolvingBoard[CellList[3]][0]=candidate3
                    SolvingBoard[CellList[3]][1]=1
                    testing+=1
                    if testing>tryborder: #may change this number.. Trying is taking too long. return and try with some other values
                        for i in xrange(4):
                            SolvingBoard[CellList[i]][0]=""
                            SolvingBoard[CellList[i]][1]=0
                        return -3
                    global Verbose
                    Verbosetemp=Verbose
                    Verbose=0
                    if not CheckMissplacements(SolvingBoard,-1,1)==-1:
                        TempList=PrepareBoard(SolvingBoard,0)
                    else:
                        TempList=(SolvingBoard,0)
                    Verbose=Verbosetemp
                      
                    if TempList==-2:
                        for i in xrange(4):
                            SolvingBoard[CellList[i]][0]=""
                            SolvingBoard[CellList[i]][1]=0
                     
                        return -2
                    if Graphics:
                        DrawSolvingBoard(PossibleList,SolvingBoard,TempList[0],0,CellList)
                    if Verbose:
                        print "Try number " +str(testing)
                    Solved=1
                    for tempcell in TempList[0]:
                        if tempcell[0]=="":
                            Solved=0
                            if Verbose:
                                print "error"
                            break
                        
                    if Solved:
                        if not CheckMissplacements(TempList[0],-1,1)==-1:
                            if Verbose:
                                print "solved"
                            TempList[0].append(testing)
                            return TempList[0]
    for i in xrange(4):
        SolvingBoard[CellList[i]][0]=""
        SolvingBoard[CellList[i]][1]=0
                       
    return -1               
def BruteForce(PossibleList,SolvingBoard):
#    print PossibleList
#    print SolvingBoard
    CurrentCell=-1
    BackStepped=0
    LastNotValid=0
    Jumps=0
    while True:
        Jumps+=1
        if Jumps%200==0:
            if Graphics:
                DrawSolvingBoard(PossibleList,SolvingBoard) #For fancy graphics and the lulz
                if(GetKeyEventsWSolving()==-1): #Cancel event occured
                    return -2
            if Verbose:
                print "Jumps = "+str(Jumps)
        while True: #add 1 to currentcell, and keep doing to we come to a uncertain cell
            CurrentCell+=1
            if CurrentCell>80:
                #return, the board is now solved
                #Return jumps too
                SolvingBoard.append(Jumps)
                return SolvingBoard

            if SolvingBoard[CurrentCell][1]==0: #break incrementing loop if we reach an unsolved cell
                break
        SolvingBoard[CurrentCell][2]=0
        SolvingBoard[CurrentCell][0]=PossibleList[CurrentCell][SolvingBoard[CurrentCell][2]]
        while True:
            if BackStepped: #we have just stepped a cell back. try the next candidate for the cell
                BackStepped=0
                if not SolvingBoard[CurrentCell][0]==PossibleList[CurrentCell][-1]: #check if we are at last candidate
                    SolvingBoard[CurrentCell][2]+=1
                    SolvingBoard[CurrentCell][0]=PossibleList[CurrentCell][SolvingBoard[CurrentCell][2]]
                else:
                    LastNotValid=1
            #print CheckMissplacements(SolvingBoard,1)
            #print SolvingBoard
            if CheckMissplacements(SolvingBoard,CurrentCell,1)==-1 or LastNotValid: #if cell don't fit, or we tried this before, we try the next possible value for the cell

                LastNotValid=0
                SolvingBoard[CurrentCell][2]+=1
                if not SolvingBoard[CurrentCell][2]+1 > len(PossibleList[CurrentCell]):
                    SolvingBoard[CurrentCell][0]=PossibleList[CurrentCell][SolvingBoard[CurrentCell][2]]
                else: #if we have tried all possibilities, go back to next unsolved cell
                    SolvingBoard[CurrentCell][0]=""
                    while True:
                        CurrentCell-=1
                        BackStepped=1
                        if CurrentCell<0:
                            return -1 #Board could not be solved
                        if not SolvingBoard[CurrentCell][1]==1:
                            break
            else: #break if cell fits
                break


def SolveBoard(Board):
    Solved=0
    #Here we solve the board
    #first we copy boardnumbers
    SolvingBoard=[""]*81
    for i in xrange(81):
            if not BoardNumbers[i]=="":
                SolvingBoard[i]=[BoardNumbers[i],1,0]
            else:
                SolvingBoard[i]=["",0,0]
    #print SolvingBoard


#We have now copied in the entered board. Solvingboard is now of a list of list.
#The list contains the following:
#[0] contains the value of the cell
#[1] Contains either the numbers 0 or 1
#0 means we should not edit this cell. These are the cells entered by the user, 0 means we are alowed to edit the cell
#We have also reformated it a bit. It is now one-dimensional. This makes things a bit easier later on.
#[2] contains the candidate which is currently active
    #We prepare for bruteforce.
    #We find some easy cells and make a list of candidates for each cell
    Temp=PrepareBoard(SolvingBoard)
    if Temp==-2:
        return -2
    PossibleList=Temp[1]
    SolvingBoard=Temp[0]
    if (CheckFaultyBoard(PossibleList)==-1): #check if a cell have no candidate
        return -1
    #Check if we are done solving
    Solved=1
    for cell in SolvingBoard:
        if cell[0]=="":
            Solved=0
            break
            
    if Solved:
        SolvingBoard.append(0)
        return SolvingBoard
    #brute force part
    #Here we use brute force to solve for the remaining cells.
    if CurrentState[6]:
        #We copy the board to a temp board (for displaying the correct colors when solved
        TempBoard=[]
        for i in xrange(81):
            TempBoard.append([])
            for l in xrange (3):
                TempBoard[i].append(SolvingBoard[i][l])
        nextNumberofTries=30
        tries=-nextNumberofTries
        SolvedBoard=-3
        while SolvedBoard==-3: #it took too long, try to call again, and keep doing so. (We should maybe stop if we have called it a certain numbe of times, or let it run to end after some tries)
            tries+=nextNumberofTries
            SolvedBoard=BruteForceRandom(PossibleList,SolvingBoard,nextNumberofTries)
            nextNumberofTries+=10
    
        if not SolvedBoard in (-1,-2):
            SolvedBoard[-1]+=tries
            #Correct the values in SolvedBoard[i][1] to those of Tempboard For drawing correct colors
            for i in xrange(81):
                SolvedBoard[i][1]=TempBoard[i][1]
            return SolvedBoard

            
            
    if CurrentState[7]:
        SolvedBoard=BruteForce(PossibleList,SolvingBoard)
    if not 1 in CurrentState[6:]:
        if Solved:
            return SolvingBoard
        else:
            return -1
        
    return SolvedBoard




def PrintBoard(Board): #Prints board to stdout
    for i in xrange(9):
        if i%3==0 and not i==0:
            print "---------------------------"
        counter=0
        for j in Board[(i*9):((i+1)*9)]:
            if counter%3==0 and not counter==0:
                print "|",
            if j in (1,2,3,4,5,6,7,8,9):
                if counter%3==2:
                    print j,
                else:
                    print str(j)+" ",
            else:
                print ". ",
            counter+=1
        print
    print "\n\n"



import time
BoardNumbers=[""] * 81
Graphics=0
global Verbose
Verbose=0
CurrentState=[1]*8
CurrentState[4]=0 #Not Working correctly
f=open('sudoku.txt')
lines=f.readlines()
Boards=[]
i=0
testinglines=[]
for line in lines:
    if i%10==0:
        i+=1
        continue
    if i%10==1:
        testinglines.append('')
    for char in line:
        if char in '0123456789':
            testinglines[i/10]+=char
    i+=1
#for line in testinglines:
#    print len(line)
starttime=time.time()
solvednumber=0
summe=0
for line in testinglines:
    GivenBoard=line
    current=0
    for char in GivenBoard:
        if char in ('0','1','2','3','4','5','6','7','8','9','.'):
            if current >80:
                break   #Break if we reach board limit
                 
            if char in ("1","2","3","4","5","6","7", "8", "9"):
                BoardNumbers[current]=int(char)
            else:
                BoardNumbers[current]=""
        current+=1
    #Solve
    Ready=CheckMissplacements(BoardNumbers,-1,0)
    #count number of entered numbers, we have to have at least 16 (comment out if you want to solve anyway!)
    numbers=[]
    for i in xrange(81):
        numbers.append(BoardNumbers[i])
    enteredNumbers=81-numbers.count("")
    if Ready==0:
        SolvedBoard=SolveBoard(BoardNumbers)
    if not SolvedBoard==-1:
        if Verbose:
            print  SolvedBoard[-1]
        Temp=[""]*81
        #Print the solved Board
        for i in xrange(81):
            Temp[i]=SolvedBoard[i][0]
        summe+= SolvedBoard[0][0]*100+SolvedBoard[1][0]*10+SolvedBoard[2][0]
        solvednumber+=1
        Curtime=time.time()-starttime
        averegatime=Curtime/solvednumber
        print "Boards Solved :" +str(solvednumber)
        print "Average time :" +str(averegatime)
        PrintBoard(Temp)
print summe
sys.exit()
