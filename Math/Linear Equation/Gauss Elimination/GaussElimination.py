import sys

from numpy import true_divide

def printMatrix(matrix):
    for i in matrix:
        print(i)


def swapTheZero(matrix,index):
    count = 0

    if index==len(matrix): return matrix

    while matrix[index][index] == 0:
        count+=1

        if(count>=len(matrix)):
            print("NO SOLUTION!")
            sys.exit()

        matrix[index+count], matrix[index] = matrix[index], matrix[index+count]
    return matrix


def gaussElimination(matrix):
    """Solve n*n equations with gauss elimination method

    Args:
        matrix (array): A two dimensional array representing the system of equation or matrix.
        ex -> [ 2 3 10 3 ],
              [ 1 0 -6 1 ],
              [ 9 2 -5 5 ]

    Returns:
        array: Return an upper triangular matrix which representated in a two dimensional array.
        ex -> [ 2 3 10 3 ],
              [ 0 1 -2 1 ],
              [ 0 0 -2 8 ]
    """


    for i in range(len(matrix[0])):
        matrix = swapTheZero(matrix,i)

        for j in range(i+1,len(matrix)):

            multiplier = matrix[j][i]/matrix[i][i]

            if(multiplier!=0):
                matrix[j][i] -= multiplier*matrix[i][i]
                for k in range(i+1, len(matrix[0])):
                    matrix[j][k] -= multiplier*matrix[i][k]

    return matrix


def checkUpperTriangularMatrix(matrix):
    for i in range(len(matrix)-1):
        for j in range(i):
            if matrix[i][j] != 0: return False
    return True


def backwardSubsitution(matrix):
    """Solve an upper triangular matrix of equation system.

    Args:
        matrix (array): An upper triangular matrix.
        ex -> [ 2 3 10 3 ],
              [ 0 1 -2 1 ],
              [ 0 0 -2 8 ]

    Returns:
        array: Return the solutions of equation system in array.
    """

    if not checkUpperTriangularMatrix(matrix): return "NOT Upper Triangular Matrix!"

    result = []
    for i in range (len(matrix)-1,-1,-1):
        count = 0
        for j in range (len(matrix[i])-2,-1,-1):
            if matrix[i][j] == 0: continue
            # print("i,j:",i,j,"|result:",matrix[i][j])

            if(j==i):
                result.append(matrix[i][len(matrix[i])-1]/matrix[i][j])
            else:
                matrix[i][len(matrix[i])-1]-=matrix[i][j]*result[count]
                count+=1

    result.reverse()
    return result


linearEquationSolution = lambda matrix: backwardSubsitution(gaussElimination(matrix))

# BUG
A = [
        [1,0,-2,1,2],
        [0,1,27,0,5],
        [1,1,0,5,-1],
        [10,3,0,3,10],
    ]

B = [
        [10,3,0,3,10],
        [1,1,0,5,-1],
        [0,1,27,0,5],
        [1,0,-2,1,2],
    ]

C = [
        [0,1,27,0,5],
        [10,3,0,3,10],
        [1,1,0,5,-1],
        [1,0,-2,1,2],
    ]

matrixB = [
    [0,0,2,1,-5],
    [1,2,3,4,-26],
    [0,0,0,-3,21],
    [0,1,1,1,-9],
]

matrixC = [
    [1,-1,2,4],
    [2,-2,-2,2],
    [0,1,-10,-7]
]


print(linearEquationSolution(A))
print(linearEquationSolution(B))
print(linearEquationSolution(C))
# printMatrix(gaussElimination(matrixA))
# printMatrix(swapTheZero(matrixA,0))
