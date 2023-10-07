# /* Substitution box
# Randomly pick a letter
import random
def main():
    # sbox = [['C', 'Q'],
    #         ['R', 'T'],
    #         ['A', 'W'],
    #         ['Q', 'E'],
    #         ['W', 'C'],
    #         ['X', 'R'],
    #         ['V', 'Y'],
    #         ['Y', 'V'],
    #         ['T', 'A'],
    #         ['E', 'X']]
    # Dictionary
    # sbox = {['C', 'Q'],
    #         ['R', 'T'],
    #         ['A', 'W'],
    #         ['Q', 'E'],
    #         ['W', 'C'],
    #         ['X', 'R'],
    #         ['V', 'Y'],
    #         ['Y', 'V'],
    #         ['T', 'A'],
    #         ['E', 'X']}
    #
    pText = 'CRATERAWVARRATERAYCX'
    # Column Size of 4
    Matrix = [['C', 'R', 'A', 'T'],
              ['E', 'R', 'A', 'W'],
              ['V', 'A', 'R', 'R'],
              ['A', 'T', 'E', 'R'],
              ['A', 'Y', 'C', 'X']]
    sbox = {}
    sbox['C'] = 'Q'
    sbox['R'] = 'T'
    sbox['A'] = 'W'
    sbox['Q'] = 'E'
    sbox['W'] = 'C'
    sbox['X'] = 'R'
    sbox['V'] = 'Y'
    sbox['Y'] = 'V'
    sbox['T'] = 'A'
    sbox['E'] = 'X'

    print(Matrix)
    for r in range(len(Matrix)):
        for c in range(len(Matrix[0])):
            # Test conversion
            # print(Matrix[r][c], end=' ')
            # print(sbox[Matrix[r][c]])
            Matrix[r][c] = sbox[Matrix[r][c]]
    print(Matrix)






main()