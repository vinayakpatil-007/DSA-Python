num = 1234
n = num
sum = 0

while n > 0 :
    i = n % 10
    sum +=i
    n //= 10

print(sum)