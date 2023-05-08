odd = int(input())
temp = odd
def aks(i): 
	global a
	a=0
	if(i>0):
		print(i)
		if i%2 == 1:
			a = a + 1
			print(a)
		aks(int(i/10))
aks(temp)
print(a)

