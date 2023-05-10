
def reverse_k_row(A, k):
   # print(A, "AKA", k)
	# A is a list of lists and k is an integer
	# return the modified matrix B (list of lists)
    for i in range(1,len(A)+1):
    #    print("ran here", i)
        if k*i<=len(A):
            A[k*i-1] = A[k*i-1][::-1]
        else: 
    #        print(A)
            return A
    #    print(A)
    return A
    

""" # sample code to test your implementation
print(reverse_k_row([[1, 2], [3, 4]], 2)) # should print [[1, 2], [4, 3]]
print(reverse_k_row([[1, 2], [3, 4]], 1)) # should print [[2, 1], [4, 3]]
print(reverse_k_row([[1, 2], [3, 4]], 10)) # should print [[1, 2], [3, 4]] """
