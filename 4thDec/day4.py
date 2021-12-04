"""
Advent of code

4. december
"""
import numpy as np

def dec4_part1():    
    numbers=np.loadtxt('day4_file.txt', dtype=int, max_rows=1, delimiter=",")
    boards=np.loadtxt('day4_file.txt', dtype=int, skiprows=1)

    flat_board=boards.flatten()
    marked_board=np.ones(len(flat_board))

    shape=(int(len(boards)/len(boards[0])), len(boards[0]), len(boards[0]))
    boards_reshaped=np.reshape(flat_board, shape)

    draw=0
    bingo=False
    while bingo==False:
        indices=np.where(flat_board==numbers[draw])
        marked_board[indices[0]]=0

        bingo, winner_board=check4bingo(np.reshape(marked_board, shape))
        draw+=1
    
    indices=np.reshape(marked_board, shape)[winner_board]

    return np.sum(boards_reshaped[winner_board]*indices)*numbers[draw-1]


def dec4_part2():    
    numbers=np.loadtxt('day4_file.txt', dtype=int, max_rows=1, delimiter=",")
    boards=np.loadtxt('day4_file.txt', dtype=int, skiprows=1)

    flat_board=boards.flatten()
    marked_board=np.ones(len(flat_board))

    shape=(int(len(boards)/len(boards[0])), len(boards[0]), len(boards[0]))
    boards_reshaped=np.reshape(flat_board, shape)

    draw=0
    bingo=False
    winner_board=-1
    while bingo==False:
        #Marks the correct numbers
        indices=np.where(marked_board==numbers[draw])

        #flat
        marked_board[indices[0]]=0
        #resahped
        marked_board=np.reshape(marked_board, (int(len(marked_board)/25),5,5))
        #Removing the winners
        if winner_board!=-1:
            #print(marked_board)
            marked_board=np.delete(marked_board,winner_board,axis=0)
            boards_reshaped=np.delete(boards_reshaped,winner_board,axis=0)

            #print(marked_board)

        bingo, winner_board=check4bingo_2(marked_board)
        marked_board=marked_board.flatten()

        print(bingo, winner_board)
        
        draw+=1
    
    mb_r=np.reshape(marked_board, (int(len(marked_board)/25),5,5))

    indices=mb_r[winner_board]

    return np.sum(boards_reshaped[winner_board]*indices)*numbers[draw-1]

def check4bingo_2(board):
    bingo=False
    winner=-1
    #print(board)
    current_winners=len(board)
    for j in range(len(board)):
        board_T=board[j].T
        for i in range(board[j].shape[0]):
            if np.sum(board[j][i])==0 or np.sum(board_T[i])==0:
                #print(winner)
                current_winners-=1
                winner=j
                #print(winner)
                if current_winners==1:
                    bingo=True
                    winner=j
                    
    return bingo, winner

def check4bingo(board):
    bingo=False
    winner=-1
    for j in range(len(board)):
        board_T=board[j].T
        for i in range(board[j].shape[0]):
            if np.sum(board[j][i])==0 or np.sum(board_T[i])==0:
                bingo=True
                winner=j
    
    return bingo, winner

print(dec4_part1())
print(dec4_part2())