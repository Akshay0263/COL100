def is_symmetric(A):
    B = []
    for i in range(len(A[0])):
        temp = []
        for j in range(len(A)):
            temp.append(A[j][i])
        B.append(temp)
    print(B)
    if A == B:
        return True
    else: return False

print(is_symmetric([[1,2,3],[4,5,6]]))
