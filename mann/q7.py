s=input()
if s[0]=="+": s1=s.replace("+", "")
else: s1=s.replace("-", "")
count=-1
def fun(s1,c):
    if(c==len(s1)-1): return ""
    else:
        c += 1
        return s1[c]+fun(s1,c)
print(fun(s1,count))

