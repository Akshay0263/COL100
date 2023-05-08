n=int(input())
m=int(input())
r=n%m
while(r>0):
    n = m
    m = r
    r = n%m
print(m)