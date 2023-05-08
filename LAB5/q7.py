A = input()
B= True
C = 0;

def inter(i):
	if A[i] == "+" or "-":
		B = True if A[i]=="+" else "False"
		print(A[i])
	else:
		C = C*10 + int(A[i])
		if i !=0:
			inter(i-1)
inter(len(A)-1)
print(C)
		
		
