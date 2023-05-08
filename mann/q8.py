count=0
x=int(input())
def oddf(n,c):
    if(n<=0):
        return c
    else:
        if(n%2!=0): c+=1
        return(oddf(n//10,c))
print(oddf(x,count))
