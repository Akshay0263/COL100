t = int(input())
for k in range(t):
    alice = [x for x in input()]
    bob = [x for x in input()]#converts it to list of characters
    while(bob.count(' ')!=0):
        bob.remove(' ') #remove white spaces
    while(alice.count(' ')!=0):
        alice.remove(' ')
    for i in alice[:]: #alice[:] used notice
        if i in bob:
            if type(i)== None: continue
            print(type(i))
            while(i in bob or i in alice):
                bob = bob.remove(i)
                bob = alice.remove(i)
    if len(bob)==0:
        if len(alice==0):print("you draw some.")
        else: print("you win some.")
    
    if len(alice)==0:
        if len(bob!=0):print("you lose some.")
            


