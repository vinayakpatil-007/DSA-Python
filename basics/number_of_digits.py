n = 1234;
count=0;
while(n > 0):

    count+=1;
    n = n // 10;

print("no. of digits",count);


# note :-1. time complexity = O(log10(N))      N-> nuber ,not no. of digits
#        2. space complexity = O(1)
 

# import math;
# n=1234
# digits= int(math.log10(n)+1)

# print(digits)


# # Edge Case: Number = 0
# n = 0

# if n == 0:
#     print(1)
# else:
#     count = 0
#     while n > 0:
#         count += 1
#         n //= 10
#     print(count)