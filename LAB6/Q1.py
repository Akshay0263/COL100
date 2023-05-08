def reverse_k_row(A, k):
	# A is a list of lists and k is an integer
	# return the modified matrix B (list of lists)
    if k<=len(A):
        A[k-1] = A[k-1][::-1]
        return A
    else: return A

# sample code to test your implementation
print(reverse_k_row([[1, 2], [3, 4]], 2)) # should print [[1, 2], [4, 3]]
print(reverse_k_row([[1, 2], [3, 4]], 1)) # should print [[2, 1], [4, 3]]
print(reverse_k_row([[1, 2], [3, 4]], 10)) # should print [[1, 2], [3, 4]]