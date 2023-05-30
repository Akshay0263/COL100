def get_intersection(A, B, C):
    i,j,k = 0,0,0
    ls = []
    while i<len(A) and j<len(B) and k<len(C) :
        if A[i]==B[j]==C[k]: ls.append(A[i]) ; i,j,k = i+1,j+1,k+1
        elif A[i]<=C[k] and A[i]<=B[j]: i+=1
        elif B[j]<=C[k] and B[j]<=A[i]: j+=1
        elif C[k]<=B[j] and C[k]<=A[i]: k+=1
    return ls

print(get_intersection([1, 5, 10, 20, 40, 80],[6, 7, 20, 80, 100],[3, 4, 15, 20, 30, 70, 80, 120]))