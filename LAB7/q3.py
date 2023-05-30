def get_minima(L):
	milgyalesgoo = False
	poynter = int(len(L)/2)
	l_pointer = 0
	r_pointer = int(len(L)-1)
	while milgyalesgoo == False:
		if L[poynter-1] <= L[poynter] <= L[poynter+1]: r_pointer = poynter ; poynter = int(poynter/2 ); 
		elif L[poynter-1] >= L[poynter] >= L[poynter+1]: l_pointer = poynter ; poynter = poynter + int((r_pointer - poynter)/2)
		else :poynter = L.index(min(L[poynter-1],L[poynter],L[poynter+1])) ; milgyalesgoo = True
		
	return L[poynter]

#print(get_minima([20, 15, 11, 8, 7, 11, 13, 19, 21, 31]))