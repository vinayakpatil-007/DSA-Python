n = [3,5,2,5,7,4,2,4,7,9,6]
 
def reverse(n , l , r):
    if l >= r :
        return
    
    n[l] , n[r] = n[r] , n[l]
    reverse(n , l+1 ,r-1)

reverse(n , 4 ,6)
print(n)