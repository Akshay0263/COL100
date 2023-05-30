import math
def range_sum(L,N):
    isPrime = {}
    for i in range(N+1):
        isPrime[i] = True
        isPrime[0]= isPrime[1] = False
    for i in isPrime:
        if isPrime[i]==False: continue
        else:
#            print(i)
            for j in range(i,math.ceil(N/i)):
                isPrime[i*j] = False
    lr = [isPrime[x] for x in isPrime]
    summer = 0
    for i in L:
        for j in range(i[0],i[1]+1):
            if lr[j]: summer += j
    return summer
    #print(lr)
#print(range_sum([(24, 28)], 30))     
