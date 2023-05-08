s1=input()
s2=input()
x=s1+s2
d={}
for a in x:
    if a in d: d[a]+=1
    else: d[a]=1
for a in x:
    if(d[a]==1):
        print(a,end="")
