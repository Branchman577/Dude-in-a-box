import random

def d(nod,dtype):
    dlist =[]
    i = 0
    while i < nod:
        num = random.randint(1,dtype)
        dlist.append(num)
        i += 1
    return(dlist)
