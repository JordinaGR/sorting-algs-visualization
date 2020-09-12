def merge(left,right):
    sort = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sort.append(left[i])
            i += 1
        else:
            sort.append(right[j])
            j += 1

    sort += left[i:]
    sort += right[j:]
    return sort

def merge_sort(data):
    if len(data) == 1:
        return data
    middle = len(data) // 2
    left_data = merge_sort(data[:middle])
    right_data = merge_sort(data[middle:])
    return merge(left_data, right_data)


data = [10,5,2,3,7,4,8,9] 
print(merge_sort(data))