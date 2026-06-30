def sum (s,i,n) :
    if (i>n):
        print(s)
        return
    sum(s+i,i+1,n)

sum(0,1,10)