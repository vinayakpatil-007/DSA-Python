# left = [2, 5, 8]
# right = [1, 5, 7]

# def merge_func(left, right):
#     n = len(left)
#     m = len(right)
#     result = []

#     i, j = 0, 0

#     while i < n and j < m:
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < n:
#         result.append(left[i])
#         i += 1

#     while j < m:
#         result.append(right[j])
#         j += 1

#     return result

# result = merge_func(left, right)
# print(result)


num = [6, 3, 8, 2, 7, 5, 1, 4]

def merge_sort(num):

    if len(num) <= 1: 
        return num

    mid = len(num) // 2

    left = merge_sort(num[:mid])
    right = merge_sort(num[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


result = merge_sort(num)
print(result)