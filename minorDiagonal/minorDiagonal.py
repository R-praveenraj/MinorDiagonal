# You are given a N X N integer matrix. You have to find the sum of all the minor diagonal elements of A.
# Minor diagonal of a M X M matrix A is a collection of elements A[i, j] such that i + j = M + 1 (where i, j are 1-based).
# Input
# [  [1, -2, -3],
#    [-4, 5, -6],
#    [-7, -8, 9]  ]
# Output
# -5
def minor_diagonal(matrix,row,column):
    total=0
    j=column-1
    for i in range(row):
        total+=matrix[i][j]
        j-=1
    return total

matrix=[]
row=int(input())
column=int(input())
for i in range(row):
    matrix.append(list(map(int,input().split())))

print(minor_diagonal(matrix,row,column))