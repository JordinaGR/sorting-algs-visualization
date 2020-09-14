import time
import sys

sys.setrecursionlimit(100000000)

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
