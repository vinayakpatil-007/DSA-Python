num = 20
n = num 
a = []


#using List

# for i in range(1,n+1):
#     if(n%i == 0):
#         a.append(i)
# print(a)

# TC :- O(N)
# SC :- O(K)

# for i in range(1,n+1):
#     if(n % i == 0):
#         print(i)


# optimized

# for i in range( 1 , n//2+1):
#     if(n % i == 0):
#         a.append(i)

# a.append(n)

# print(a)

# TC :- O(1/2N) => O(N)
# SC :- O(K)



# Efficient Way to Print Divisors (√n)
import math
for i in range(1, int(math.sqrt(n)) + 1):
    if(n % i == 0):
        a.append(i)

        if(n // i != i):
            a.append(n) 

print(a)
