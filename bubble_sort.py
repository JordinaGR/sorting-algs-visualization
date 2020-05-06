import time

def bubble_sort(data, drawdata, speed):

    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawdata(data, ['red' if x == j or x == j+1 else ['black'] for x in range(len(data))])
                time.sleep(speed)
    drawdata(data, ['green' for x in range(len(data))])
