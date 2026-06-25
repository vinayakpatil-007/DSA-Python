original= 121
n = original
reverse = 0

while n > 0 :
    id = n % 10
    reverse = reverse * 10 + id
    n //= 10

if(original == reverse):
    print("Palindrome")


else:
    print("Not Palindrome")



# note :-1. time complexity = O(log10(N))      N-> nuber ,not no. of digits
#        2. space complexity = O(1)