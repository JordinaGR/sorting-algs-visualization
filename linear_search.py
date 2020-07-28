import time

def linear(data, n, drawdata, speed):
    for i, item in enumerate(data):
        drawdata(data, ['red' if x == i else ['black'] for x in range(len(data))])
        time.sleep(speed)
        if item == n:
            drawdata(data, ['green' if x == i else ['black'] for x in range(len(data))])
            time.sleep(speed)
            return i
    return None