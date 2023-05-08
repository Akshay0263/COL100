T=int(input())
if(T<=10 and T>=1):
    for i in range(1,T+1):
        A=input()
        B=input()
        a=len(A)
        b=len(B)
        X=[]
        Y=[]

        for x in range(a):
            X.append(A[x])
        for y in range(b):
            Y.append(B[y])  
            
        while(X.count(' ')!=0):
            X.remove(' ') #remove white spaces
        while(Y.count(' ')!=0):
            Y.remove(' ')
        j=0      
        while(j<len(X)):
            k=0
            while(k<len(Y)):
                if(X[j]==Y[k]):
                    X.pop(j)
                    Y.pop(k)
                    j-=1
                    break
                k+=1
            j+=1        
        if(len(X)==0 and len(Y)!=0):
            print("You lose some.")
        elif(len(Y)==0 and len(X)!=0):
            print("You win some.")
        else:
            print("You draw some.")