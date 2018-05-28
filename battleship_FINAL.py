import getpass
import sys
wincondition = True
def playagain():
    gameon = input('Do you want to play again(Y/N)?')            
    while (gameon != 'Y') and (gameon != 'N'):    
        gameon = input('Do you want to play again(Y/N)?')
        if gameon == 'Y' or gameon == 'N':
            break        
    if gameon == 'Y':
       global wincondition 
       wincondition = False
    elif gameon == 'N':
            sys.exit()      
def shooting(player):    
    while wincondition == True:    
        while  True:
            try:
                n = int(input("Your first shoot coordinate:"))
                m = int(input("Your second shoot coordinate:"))
            except ValueError:
                print('not a number')
                continue
            if n > 5 or n < 1 or m > 5 or m < 1:
                print('wrong input')
                continue 
            else:
                break 
        if player == "player_one":
            print("\033[1;44m{}'s board:\033[1;m".format(player_two_name))
            if (n, m) != ship3:
                playertwo_board[n-1][m-1] = missed                
                print_board(playertwo_board)                
            if (n, m) == ship3:
                playertwo_board[n-1][m-1] = found                
                print_board(playertwo_board)
                print('\033[1;31mCongratulation {} you won!\033[1;m'.format(player_one_name))
                playagain()                                                
        if player == "player_two":
            print("\033[1;41m{}'s board:\033[1;m".format(player_one_name))
            if (n, m) != ship1:
                playerone_board[n-1][m-1] = missed            
                print_board(playerone_board)                
            if (n, m) == ship1:
                playerone_board[n-1][m-1] = found            
                print_board(playerone_board)
                print('\033[1;31mCongratulation {} you won!\033[1;m'.format(player_two_name))
                playagain()
        break                                                    
def print_board(board):
    print(1, 2, 3, 4, 5)    
    for row in board:
        print((" ").join(row))    
def setship():
    while True:
        try:
            a = int(getpass.getpass("Your ship's coordinate (row): "))
            b = int(getpass.getpass("Your ship's coordinate (column): "))
        except ValueError:
            print('wrong input')
            continue
        if ((a >= 1) and (a <= 5)) and  ((b >= 1) and (b <= 5)):
            return a, b
            break
        else:
            print('wrong input')            
player_one_name = input("Player One, type your name in: ")
player_two_name = input("Player Two, type your name in: ")
while True:      
    wincondition = True  
    playerone_board = []
    playertwo_board = []
    for x in range(5):
        playerone_board.append(['\033[1;36m~\033[1;m'] * 5)
    for x in range(5):
        playertwo_board.append(['\033[1;34m~\033[1;m'] * 5)
    for i in range(len(playerone_board)):
            playerone_board[i].append(str(i+1))
    for i in range(len(playertwo_board)):
            playertwo_board[i].append(str(i+1))
    print("{} set your ship:".format(player_one_name))
    ship1 = (setship())
    print("{} set your ship:".format(player_two_name))
    ship3 = (setship())
    missed = '\033[1;32m0\033[1;m'
    found = '\033[1;31mX\033[1;m'
    player_one_turn = True
    player_two_turn = False
    turn_count = 0       
    while wincondition == True:            
        if player_one_turn == True:
            shooting("player_one")
            player_one_turn = False
            player_two_turn = True
            turn_count += 1
        if player_two_turn == True:
            shooting("player_two")
            player_two_turn = False
            player_one_turn = True
            turn_count += 1
        if turn_count == 26:
            print("\033[1;33mYou are both out of turns. It's a draw!\033[1;m")
            playagain()
            break