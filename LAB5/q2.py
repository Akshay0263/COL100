s1 = input()
s2 = input()
s3 =""


for i in s1:
	isthere = False
	for j in range(0,len(s2)):
		if i == s2[j]:
			isthere = True
	if isthere == False:
		s3 = s3 + i

for i in s2:
	isthere = False
	for j in range(0,len(s1)):
		if i == s1[j]:
			isthere = True
	if isthere == False:
		s3 = s3 + i
print(s3)
