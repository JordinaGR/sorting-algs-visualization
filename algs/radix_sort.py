import time

def countingSort(data, exp1, drawdata, speed): 

    n = len(data)

    output = [0] * (n) 
    count = [0] * (10)

    for i in range(0, n):
        index = (data[i] / exp1) 
        count[int(index % 10)] += 1

    for i in range(1, 10): 
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0: 
        index = (data[i] / exp1) 
        output[count[int(index % 10)] - 1] = data[i] 
        count[int(index % 10)] -= 1
        i -= 1

    for i in range(0, len(data)): 
        data[i] = output[i]

    drawdata(data, ['black' for x in range(len(data))])
    time.sleep(speed + 0.3)

def radixSort(data, drawdata, speed): 

    max1 = max(data)

    exp = 1
    numss = len(str(max(data)))

    while numss != 0: 
        countingSort(data, exp, drawdata, speed) 
        exp *= 10
        numss -= 1

    return data