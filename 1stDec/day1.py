"""
Advent of code

1. december
"""

def dec1_part1():

    with open('day1_file.txt') as f:
        lines = f.readlines()
        list_int = list(map(int, lines))
        
    count=0
    x=max(list_int)

    for i in list_int:
        if x<i:
            count+=1
        x=i
    return count


def dec1_part2():
    with open('day1_file.txt') as f:
        lines = f.readlines()
        list_int = list(map(int, lines))

    sums_list=[]
    for i in range(len(list_int)-2):
        sums_list.append(list_int[i]+list_int[i+1]+list_int[i+2])

    x=max(list_int)
    count=0
    for i in sums_list:
        if x<i:
            count+=1
        x=i

    return count

print(dec1_part1())
print(dec1_part2())


