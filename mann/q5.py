n=int(input())
m=int(input())
r=n%m
x,y=m,n
while(r>0):
    n = m
    m = r
    r = n%m
print(int(x*y/m))