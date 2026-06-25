original = 153
n = original
total = 0
p = len(str(n))

while n > 0 :
    i = n % 10
    total = total+(i**p)
    n //=10

if(original == total):
    print("Armstrong")

else :
    print("Not Armstrong")

# note :-1. time complexity = O(log10(N))      N-> nuber ,not no. of digits
#        2. space complexity = O(1)