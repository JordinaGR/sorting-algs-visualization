import time


def binary(data, n, drawdata, speed):
    while True:
        if len(data) == 0 or (len(data) == 1 and data[0] != n):
            return False

        mid = data[len(data) // 2]

        if mid == n:
            drawdata(data, getcolorarray(len(data), n))
            time.sleep(speed)
            break

        elif mid > n:
            drawdata(data, getcolorarray(len(data), n))
            time.sleep(speed)
            data = data[:len(data) // 2]


        elif mid < n:
            drawdata(data, getcolorarray(len(data), n))
            time.sleep(speed)
            data = data[len(data) // 2 + 1:]



def getcolorarray(datalen, n):
    colorarray = []

    for i in range(datalen):
        if i >= n and i <= n:
            colorarray.append("gray")
        else:
            colorarray.append('black')

        if i == n:
            colorarray[i] = 'green'
        elif i < n:
            colorarray[i] = 'red'
        elif i > n:
            colorarray[i] = 'yellow'

    return colorarray