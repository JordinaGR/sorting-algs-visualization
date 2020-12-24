import time

def shell(data, drawdata, speed): 
  
    n = len(data)
    gap = n//2

    while gap > 0: 
  
        for i in range(gap,n): 

            temp = data[i] 
            j = i 

            while  j >= gap and data[j-gap] >temp: 
                data[j] = data[j-gap] 
                drawdata(data, ['red' if x == data[j] or x == data[j-gap] else ['black'] for x in range(len(data))])
                time.sleep(speed)
                j -= gap 

            data[j] = temp
            drawdata(data, ['red' if x == data[j] or x == temp else ['black'] for x in range(len(data))])
            time.sleep(speed)

        gap //= 2
    
    return data

