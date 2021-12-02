"""
Advent of code

2. december
"""
import numpy as np

def dec2_part1():

    with open('day2_file.txt') as f:
        lines = f.readlines()

    directions=[i.split(' ', 1)[0] for i in lines]
    values=[i.split(' ', 1)[1] for i in lines]
    values_int = np.array(list(map(int, values)))

    unique_directions=np.array(["forward", "up", "down"])
    
    direc=np.zeros(len(unique_directions))

    #Find all occurances of the directions
    for i in range(len(unique_directions)):
        val=(np.where(np.array(directions) == unique_directions[i])[0])
        direc[i]=np.sum(values_int[val])

    return direc[0]*(direc[2]-direc[1])


def dec2_part2():
    with open('day2_file.txt') as f:
        lines = f.readlines()

    directions=[i.split(' ', 1)[0] for i in lines]
    values=[i.split(' ', 1)[1] for i in lines]
    values_int = np.array(list(map(int, values)))


    unique_directions=np.array(["forward", "depth", "aim"])
    direc=np.zeros(len(unique_directions))

    for i in range(len(values_int)):
        if directions[i]=='forward':
            direc[0]+=values_int[i]
            direc[1]+=direc[2]*values_int[i]
        elif directions[i]=='down':
            direc[2]+=values_int[i]
        else:
            direc[2]-=values_int[i]

    return direc[0]*direc[1]


print(dec2_part1())
print(dec2_part2())


