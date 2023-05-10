
def alphabet_vector(str):
	# string is a python string
	# return the alphabet vector (list of integers)
	a2z = 'abcdefghijklmnopqrstuvwxyz'
	alpha_vector = [0]*26
	for i in str:
		if i in a2z: alpha_vector[ord(i)-97] = 1
	return alpha_vector

#(s1,s2) = (x.strip().strip("\"") for x in input().split(","))

def subtract_vector(s1, s2):
	return [alphabet_vector(s1)[i]-alphabet_vector(s2)[i] for i in range(26) ]
	#return alphabet_vector(s1)-alphabet_vector(s2)

#print(subtract_vector(s1,s2))