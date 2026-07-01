num =[3,5,6,3,2,5,7,3,6]

def func(num) :
    n = len(num)
    
    for i in range (0 , n) :
        min_index = i
        for j in range(i+1,n) :
            if num[min_index] > num [j] :
                min_index = j
        num [min_index] ,num [i] = num [i] ,num[min_index]
    print(num)

func(num)


# tc -> O((n+1)/2) -> n*n 
# sc -> O(1)