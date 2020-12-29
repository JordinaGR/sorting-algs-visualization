import time

def selection(data, drawdata, speed):

    for i in range(len(data)):
        minV = i

        for j in range(i, len(data)):
            if data[j] < data[minV]:
                minV = j
                drawdata(data, ['red' if  x == minV else ['black'] for x in range(len(data))])
                time.sleep(speed)

        data[minV], data[i] = data[i], data[minV] 
        
        drawdata(data, ['yellow' if  x == data[i] else ['black'] for x in range(len(data))])
        time.sleep(speed)

    return data
