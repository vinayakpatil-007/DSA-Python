# using head recursion

# def num (n):
#     if (n==0) :
#         return
#     print(n)
#     num(n-1)

# num(5)

# def num(i,n):
#     if i>n :
#         return
#     print(n)
#     num(i,n-1)

# num(1,5)


# printing 1 to n using tail recursion

def num(i,n):
    if i>n :
        return
    num(i+1,n)
    print(i)

num(1,5)