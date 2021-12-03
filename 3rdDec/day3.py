"""
Advent of code

3. december
"""
import numpy as np
from bitstring import BitArray

def dec3_part1():

    with open('day3_file.txt') as f:
        lines = f.readlines()

    #Loading the data into a matrix
    binary_matrix=np.zeros((len(lines), len(lines[0])), dtype=int)
    for index, number in enumerate(lines):
        binary=number.split(' ')
        indexes=[i for i,x in enumerate(binary[0]) if x=='1']
        binary_matrix[index][indexes]=1

    #Finding the most occured bits:
    final_int=['','']
    for i in range(len(binary_matrix.T)-1):
        most_frequent=np.bincount(binary_matrix.T[i]).argmax()

        if most_frequent==0:
            final_int[0]+='0'
            final_int[1]+='1'
        else:
            final_int[0]+='1'
            final_int[1]+='0'

    float_number_1= float(int(final_int[0], 2))
    float_number_2= float(int(final_int[1], 2))

    return float_number_1*float_number_2, np.delete(binary_matrix, -1, axis=1)



def dec3_part2():
    trash, matrix=dec3_part1()

    matrix_oxy=np.copy(matrix.T)
    matrix_co2=np.copy(matrix.T)

    for i in range(len(matrix_oxy)):
        most_frequent_oxy=np.bincount(matrix_oxy[i])
        least_frequent_co2=np.bincount(matrix_co2[i])

        if most_frequent_oxy[0] != most_frequent_oxy[1]:
            #delete coloumns without the value
            indexes_oxy=np.where(matrix_oxy[i]==most_frequent_oxy.argmin())
            matrix_oxy = np.delete(matrix_oxy.T, indexes_oxy, axis=0)
            matrix_oxy=matrix_oxy.T 
        else:
            indexes_oxy=np.where(matrix_oxy[i]==0)
            matrix_oxy = np.delete(matrix_oxy.T, indexes_oxy, axis=0)
            matrix_oxy=matrix_oxy.T

        if len(matrix_co2[0])>1:
            if  least_frequent_co2[0] != least_frequent_co2[1]:
                indexes_co2=np.where(matrix_co2[i]==least_frequent_co2.argmax())
                matrix_co2 = np.delete(matrix_co2.T, indexes_co2, axis=0)
                matrix_co2=matrix_co2.T

            else:
                indexes_co2=np.where(matrix_co2[i]==1)
                matrix_co2 = np.delete(matrix_co2.T, indexes_co2, axis=0)
                matrix_co2=matrix_co2.T

    oxy = BitArray(matrix_oxy.flatten())
    oxy_rate=oxy.uint

    co2 = BitArray(matrix_co2.flatten())
    co2_rate=co2.uint

    return oxy_rate*co2_rate


print(dec3_part1())
print(dec3_part2())