n = "vinggniv"

def func(n,l,r):
    while l < r:
        if n[l] != n[r] :
            return False
        l+=1
        r-=1
    return True

m=func(n,0,7)
print(m)
