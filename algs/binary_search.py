import time

def find(data, n, head, tail, drawdata, speed):

    mid = (head + tail) // 2

    drawdata(data, color_func(len(data), head, tail, mid))
    time.sleep(speed)

    return mid

def binary(data, n, head, tail, drawdata, speed):
    findinx = find(data, n, head, tail, drawdata, speed)

    if findinx == n:
        drawdata(data, ['green' if x == n else ['black'] for x in range(len(data))])
        time.sleep(speed)
        return findinx

    elif n < findinx:
        #left
        binary(data, n, head, findinx-1, drawdata, speed)
    else:
        #right
        binary(data, n, findinx+1, tail, drawdata, speed)


def color_func(datalen, head, tail, mid):
    colorarray = []
    for i in range(datalen):
        if i >= head and i <= tail:
            colorarray.append("grey")
        else:
            colorarray.append('black')

        if i == mid:
            colorarray[i] = 'red'

    return colorarray