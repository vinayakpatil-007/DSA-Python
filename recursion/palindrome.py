n = "vinggniv"

def func (n, l , r ) :
    if l >= r :
        return True 
    
    if n[l] != n[r] :
        return False
    
    return func( n , l+1 ,r-1)

m = func(n,0,len(n)-1)
print(m)



# n = "vinggniv"

# def func(n,l,r):
#     while l < r:
#         if n[l] != n[r] :
#             return False
#         l+=1
#         r-=1
#     return True

# m=func(n,0,7)
# print(m)

# n = "vingigniv"

# def func(n, l, r):
#     while l < r:
#         if n[l] != n[r]:
#             return False
#         l += 1
#         r -= 1
#     return True

# print(func(n, 0, len(n) - 1))