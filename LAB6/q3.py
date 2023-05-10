# q3.py

def transposer(A):
    B = []
    for i in range(len(A[0])):
        temp = []
        for j in range(len(A)):
            temp.append(A[j][i])
        B.append(temp)
    return B

def rotate_matrix(A):
    A = transposer(A)
    B = []
    for i in range(len(A)):
        temp = []
        for j in range(len(A)):
             temp.append(A[i][-j-1])
        B.append(temp)
    return(B)



print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
