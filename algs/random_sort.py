import random
import time

trys = []

def random_sorts(data, drawdata, speed):
    
    random.shuffle(data)
    drawdata(data, [['black'] for x in range(len(data))])
    time.sleep(speed)

    for i in range(len(data)-1):
        if data[i] > data[i+1]:
            trys.append(1)
            random_sorts(data, drawdata, speed)

    drawdata(data, ['green' for x in range(len(data))])
