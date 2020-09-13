import time

def merge_sort(data, drawdata, speed):
    merge_sort2(data, 0, len(data)-1, drawdata, speed)
    
def merge_sort2(data, left, right, drawdata, speed):
    if left < right:
        middle = (left + right) // 2
        merge_sort2(data, left, middle, drawdata, speed)
        merge_sort2(data, middle+1, right, drawdata, speed)
        merge(data, left, middle, right, drawdata, speed)

def merge(data, left, middle, right, drawdata, speed):
    drawdata(data, color(len(data), left, middle, right))
    time.sleep(speed)

    left_side = data[left:middle+1]
    right_side = data[middle+1:right+1]

    i, j = 0, 0

    for k in range(left, right+1):
        if i < len(left_side) and j < len(right_side):
            if left_side[i] <= right_side[j]:
                data[k] = left_side[i]
                i += 1
            else:
                data[k] = right_side[j]
                j += 1

        elif i < len(left_side):
            data[k] = left_side[i]
            i += 1
        else:
            data[k] = right_side[j]
            j += 1
    
    drawdata(data, ["green" if x >= left and x <= right else "black" for x in range(len(data))])
    time.sleep(speed)

def color(lenn, left, middle, right):
    color_list = []

    for i in range(lenn):
        if i >= left and i <= right:
            color_list.append('red')
            if i <= left and i >= middle:
                color_list.append('red')
            else:
                color_list.append('red')
        else:
            color_list.append('black')

    return color_list
