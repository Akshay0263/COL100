x=int(input())
c,n,sum=0,x,0
while(n>0):
    c+=1
    n=n//10
n=x
while(n>0):
    y=n%10
    sum+=y**c
    n=n//10
if(sum==x): print("Armstrong")
else: print("Not Armstrong")