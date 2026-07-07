# num =[3,5,6,3]

# def func (num) :
#     n = len(num)
#     for i in range (n-1) :
#         for j in range (n-i-1):
#             # print(i,j)
#             if num [j] > num [j+1] :
#                 num [j] , num [j+1] =  num [j+1] , num [j] 
#         print(i)
#     print(num)

# func(num)

num = [3, 5, 6, 3]

def func(num):
    n = len(num)
    for i in range(n-2 ,0,-1) :
        for j in range (0,i+1) :
            if num[j] > num[j+1] :
                num[j] , num[j+1] = num[j+1] > num[j]
    print(num)

func(num)




