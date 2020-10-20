import time

def opti_bubble(data, drawdata, speed):

        n = len(data)
        update = True
        j = 0
        while (update==True and n > 1):
            update = False
            for i in range(len(data)-j -1):
                if data[i] > data[i+1]:
                    data[i], data[i+1] = data[i+1], data[i]
                    drawdata(data, ['red' if x == i or x == i+1 else ['black'] for x in range(len(data))])
                    time.sleep(speed)
                    update = True
                else:
                    i += 1
            n -= 1
            j += 1
        drawdata(data, ['green' for x in range(len(data))])

        return data