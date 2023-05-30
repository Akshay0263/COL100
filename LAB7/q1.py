def fourth_smallest(L):
	count = 0
	
	for _ in range(3):
		smol=99999
		for i in L:
			smol = i if smol>i else smol
		L.pop(L.index(smol))
	smol=99999
	for i in L:
			
			smol = i if smol>i else smol
	return smol


#  oo_tggtgogggot_
