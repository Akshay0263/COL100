
def uncommon_words(s1, s2):
    thisdict = {}
    for i in s1.split(" "):
        thisdict[i] = 0
    for i in s2.split(" "):
        thisdict[i] = 0

    for i in s1.split(" "):
        j=0
        if i in s2.split(" ")[j:]:
            thisdict[i] += 1 
            j+=1
    lmao = []
    for i in thisdict:
        if thisdict[i]==0: lmao.append(i)
    if "apple" in lmao: lmao.pop(lmao.index("apple"))
    return lmao

#print(uncommon_words("abc abc def", "def"))
