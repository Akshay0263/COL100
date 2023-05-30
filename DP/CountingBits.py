
def binarycounter(lst,n):
   
   if n==0: return 0
   if lst[n]!=-1: return lst[n]
   else:
    lst[n]= n%2 + binarycounter(lst,n//2)
    return lst[n]

def countBits(n):
    ans =[]
    for i in range(n+1):
        lst = [-1 for _ in range(i+1)]
        ans.append(binarycounter(lst,i))
    return ans

print(countBits(5))