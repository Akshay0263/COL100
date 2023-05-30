def lcs_dp(s1, s2):
    m = len(s1)
    n = len(s2)
    
    d = [[0]*(n+1)]*(m+1)

    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                d[i+1][j+1] = d[i][j] + 1
            else:
                d[i+1][j+1] = max(d[i][j+1], d[i+1][j])

    # Backtrack to reconstruct the LCS
    lcs = ""
    i = m
    j = n
    while i >=1 and j >=1:
        if s1[i - 1] == s2[j - 1]:
            lcs = s1[i - 1] + lcs
            i -= 1
            j -= 1
        elif d[i - 1][j] > d[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return d[m][n], lcs
