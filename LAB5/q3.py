num = int(input())
temp=num
sum=0

while(temp>0):
	sum = sum + (temp%10)**len(str(num))
	temp = int(temp/10)
if sum == num:
	print("Armstrong")
else:
	print("Not Armstrong")
