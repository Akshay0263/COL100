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


