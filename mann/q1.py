a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
t=float(input())
g=int(input())
while ((a*(g**4)+b*(g**3)+c*g*g+d*g+e)>t or (a*(g**4)+b*(g**3)+c*g*g+d*g+e)<-t):
    g=g-((a*(g**4)+b*(g**3)+c*g*g+d*g+e)/(4*a*(g**3)+3*b*g*g+2*c*g+d))
print(g)