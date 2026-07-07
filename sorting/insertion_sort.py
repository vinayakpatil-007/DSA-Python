
num = [3,6,7,2,8,5]

def func (num) :
    n = len(num)

    for i in range(1,n) :
        key = num [i]

        for j in range(i-1,-1,-1) :
            if key < num[j] :
                num[j+1] = num [j]
            else :
                break
        num[j+1] = key
            
    print(num)


func(num)
