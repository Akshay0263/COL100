def GCD(a,b):
	if b ==0:
		return a
	else:
		return GCD(b,a%b)

a = int(input())
b = int(input())

print(int(a*b/GCD(a,b)))


