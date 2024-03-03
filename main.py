def printBoard(XState,OState):
    zero='X' if XState[0] else ('O' if OState[0] else '0') 
    one='X' if XState[1] else ('O' if OState[1] else '1') 
    two='X' if XState[2] else ('O' if OState[2] else '2') 
    three='X' if XState[3] else ('O' if OState[3] else '3') 
    four='X' if XState[4] else ('O' if OState[4] else '4') 
    five='X' if XState[5] else ('O' if OState[5] else '5') 
    six='X' if XState[6] else ('O' if OState[6] else '6') 
    seven='X' if XState[7] else ('O' if OState[7] else '7') 
    eight='X' if XState[8] else ('O' if OState[8] else '8') 

    print(f" {zero}    |  {one}   | {two}    ")
    print()
    print(f"------|------|------")
    print()
    print(f" {three}    |  {four}   | {five}    ")
    print()
    print(f"------|------|------")
    print()
    print(f" {six}    |  {seven}   | {eight}    ")
    print()
    print(f"------|------|------")
   
def checkWin(XState , OState):
    Xwins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[2,4,6]]
    for i in Xwins:
        if(XState[i[0]]+XState[i[1]]+XState[i[2]] == 3):
            print("X wins ")
            return 1
    
    Owins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[2,4,6]]
    for i in Owins:
        if(OState[i[0]]+OState[i[1]]+OState[i[2]] == 3):
            print("O wins ") 
            return 1
if __name__=="__main__":
    XState = [0,0,0,0,0,0,0,0,0]
    OState = [0,0,0,0,0,0,0,0,0]
    index = [0,0,0,0,0,0,0,0,0]
    turn = 0
    print("Welcome to Tic tac toe")
    printBoard(XState,OState)
    while(turn<9):
        if(turn>4):
            if(checkWin(XState,OState)):
                break

        if(turn%2==0):
            print("O's Chance ")
            value=int(input("Please enter a value :"))
            if(index[value]==1 or value>8):
                print(" Try Another value")
                continue
            OState[value]=1
            index[value]=1
       
        else:
            print("X's Chance  ")
            value=int(input("Please enter a value :"))
            if(index[value]==1 or value>8):
                print(" Try Another value")
                continue
            XState[value]=1
            index[value]=1
        
        turn=turn+1
        printBoard(XState,OState)
    print(" Match Over ")  
