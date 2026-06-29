num = [2,5,4,1,3,5,7,7,6,2,5,8,2,1] 
n = len(num)
dict = {}

# for i in num :
#     if i in dict :
#         dict[i]+=1
#     else :
#         dict[i] = 1
# print(dict)

# using dictionary
# for i in num :
#     dict[i] = dict.get(i,0)+1 

# print(dict)


# note :-1. time complexity = O(N)   
#        2. space complexity = O(N) 



# charactors frequency mapping

# using dictionary
m = "vinayak"
# for i in m :
#     if i in dict :
#         dict[i]+=1
#     else :
#         dict[i] = 1
# print(dict)

# using list
list = [0]*26
for i in m :
    index = ord(i) - ord("a")
    list[index] +=1

print(list)


