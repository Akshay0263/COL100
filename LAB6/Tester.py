l=[x for x in input().split(" ")]
city=[[i for i in input().split(" ")] for j in range(int(l[0]))]

for i in range(int(l[2])):
    q=[x for x in input().split(" ")]
    x=int(q[0])-1
    y=int(q[1])-1
    if(city[x][y]=='1'):
        city[x][y]='0'
        if(x<=int(l[0])-1):
            if(x>0):
                 if(city[x-1][y]=='1'): city[x-1][y]='0'
            if(x<int(l[0])-1):
                if(city[x+1][y]=='1'): city[x+1][y]='0'
        if(y<=int(l[1])-1):
            if(y>0):
                 if(city[x][y-1]=='1'): city[x][y-1]='0'
            if(y<int(l[0])-1):
                if(city[x][y+1]=='1'): city[x][y+1]='0'
    c=0
    for i in range(len(city)):
        for x in city[i]:
            if x=='1': c+=1
    print(c)