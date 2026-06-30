# Tail Recursion 

# print n times name

def name(n):
    if ( n == 0 ) :
        return
    name(n-1)
    print("vinayak")

name(5)