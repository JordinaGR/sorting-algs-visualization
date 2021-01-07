import time

def cocktail(data, drawdata, speed):

    for i in range(len(data)-1):

        for j in range(len(data)-1, 0, -1):
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
                drawdata(data, ['red' if x == j else ['black'] for x in range(len(data))])
                time.sleep(speed)

        for k in range(len(data)-1):
            if data[k] > data[k+1]:
                data[k], data[k+1] = data[k+1], data[k]
                drawdata(data, ['blue' if x == k else ['black'] for x in range(len(data))])
                time.sleep(speed)

    return data
