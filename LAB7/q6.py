def get_triplet(L):
	count = 0
	ls = []
	for _ in range(3):
		smol=0
		for i in L:
			smol = i if smol<i else smol
		ls.append(L.pop(L.index(smol)))
	return (x for x in ls)
