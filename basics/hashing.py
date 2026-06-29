n = [1,2,4,3,2,4,6,4,9,8,7,9,8,6,8,3,2,4,10,6,3,2,2,5,6,4,3,2,3,5,6,7,5,4]
m = [2,10,33,12,3,7,6,111]

# hash_mapping = [0,0,0,0,0,0,0,0,0,0,0]

# for i in n :
#     hash_mapping[i] = hash_mapping[i]+1

# print(hash_mapping)

# for i in m :
#     if(i<0 or i>10) :
#         print(i , 0)
#     else :
#         print(i , hash_mapping[i] )



dict ={}

for i in n :
    if i in dict :
        dict [i] = dict[i]+1
    else :
        dict[i] = 1

for i in m :
    if 1<=i and 10>=i :
        print(i , dict[i])
    else :
        print(i ,0)
