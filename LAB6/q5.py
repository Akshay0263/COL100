def alphabet_vector(str):
	# string is a python string
	# return the alphabet vector (list of integers)
	a2z = 'abcdefghijklmnopqrstuvwxyz'
	alpha_vector = [0]*26
	for i in str:
		if i in a2z: alpha_vector[ord(i)-97] = 1
	return alpha_vector

""" a = input()
print(alphabet_vector(a)) """