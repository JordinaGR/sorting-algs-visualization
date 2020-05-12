import time

def insertion(data, drawdata, speed):
    k = 0
    for i in range(len(data) - 1):
        if data[k] > data[k + 1]:
            data[k], data[k + 1] = data[k + 1], data[k]
            drawdata(data, ['red' if x == k or x == k + 1 else ['black'] for x in range(len(data))])
            time.sleep(speed)
            k += 1
            for j in range(len(data[:k])):
                k = 0
                if data[k] > data[k + 1]:
                    data[k], data[k + 1] = data[k + 1], data[k]
                    drawdata(data, ['red' if x == k or x == k + 1 else ['black'] for x in range(len(data))])
                    time.sleep(speed)
                    k += 1
                else:
                    k += 1
                    return insertion(data, drawdata, speed)
        else:
            k += 1
    drawdata(data, ['green' for x in range(len(data))])
    time.sleep(speed)

'''    print(data)

data = [4, 2, 3, 1, 5, 2, 5, 6, 7, 3, 5, 7, 8, 4]
insertion(data)'''
