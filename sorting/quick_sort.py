num = [6, 3, 8, 2, 7, 5, 1, 4]

def quick_sort(num):
    if len(num) <= 1:
        return num

    pivot = num[0]

    left = []
    right = []

    for i in range(1, len(num)):
        if num[i] <= pivot:
            left.append(num[i])
        else:
            right.append(num[i])

    return quick_sort(left) + [pivot] + quick_sort(right)

result = quick_sort(num)
print(result)