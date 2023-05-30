def subset_sum(L, k):
    n = len(L)
    d = [[False] * (k + 1) for _ in range(n + 1)]

   
    for i in range(n + 1):
        d[i][0] = True

   
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if L[i - 1] <= j:
                d[i][j] = d[i - 1][j] or d[i - 1][j - L[i - 1]]
            else:
                d[i][j] = d[i - 1][j]

    # Check if a subset with sum k exists
    if d[n][k]:
        subset = []
        i = n
        j = k
        while i > 0 and j > 0:
            if d[i - 1][j]:
                i -= 1
            else:
                subset.append(L[i - 1])
                j -= L[i - 1]
                i -= 1

        return True, subset[::-1]  # Reverse the subset to maintain the original order
    else:
        return False, []
