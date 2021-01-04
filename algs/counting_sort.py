import time

def counting(data, drawdata, speed):
    mval = 0
    for i in range(len(data)):
        drawdata(data, ['red' if x == i else ['black'] for x in range(len(data))])
        time.sleep(speed)
        if data[i] > mval:
            mval = data[i]

    buckets = [0 for i in range(mval + 1)]

    for i in data:
        buckets[i] += 1

    i = 0
    for j in range(mval + 1):
        for _ in range(buckets[j]):
            data[i] = j
            i += 1

    drawdata(data, ['green' for x in range(len(data))])
    time.sleep(speed)

    return data
