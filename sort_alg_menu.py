import os
from tkinter import *
from tkinter.ttk import Combobox
import time
import random
from algs.bubble_sort import bubble_sort
from algs.quick_sort import quick_sort
from algs.insertion_sort import insertion
from algs.linear_search import linear
from algs.merge_sort import merge_sort
from algs.selection_sort import selection
from algs.binary_search import binary
from algs.opti_bubble_sort import opti_bubble
from algs.random_sort import random_sorts
from algs import random_sort
from pre import pre1
from pre import pre15
from pre import pre20
from pre import pre30
from pre import pre40
from pre import pre50


# start a tkinter window
menu = Tk()
root = Tk()
widthr = root.winfo_screenwidth()
heightr = root.winfo_screenheight()
# set minsize
menu.minsize(400, 200)
menu.config(bg="lightblue1")
menu.title("Sorting algorithms visualization menu")

root.maxsize(root.winfo_screenwidth(), root.winfo_screenheight())
root.minsize(root.winfo_screenwidth(), root.winfo_screenheight())
root.config(bg="black")
root.title("Sorting algorithms visualization")


# vars
selected_alg = StringVar()
dades_pre = StringVar()
data = []
trys = random_sort.trys
pre1 = pre1.pre1
pre15 = pre15.pre15
pre20 = pre20.pre20
pre30 = pre30.pre30
pre40 = pre40.pre40
pre50 = pre50.pre50

# draw the rectangles
def drawdata(data, colorarray):
    global widthr, heightr

    canvas.delete("all")
    c_height = (heightr/3.25)*3
    c_width = widthr
    x_width = c_width / (len(data) + 1)
    offset = 0
    spacing = 0
    normalizeddata = [i / max(data) for i in data]

    for i, height in enumerate(normalizeddata):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * ((heightr/2.3)+(heightr/2.3))
        x1 = (i+1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorarray[i])

    root.update_idletasks() # update the triangles

# generate an array
def generate():
    global data, pre1, pre15, pre20, pre30, pre40, pre50, size

    try:    # if the size is not valid, set a default
        size = int(sizeEntry.get())
    except ValueError:
        size = 0

    data = []

    # check if there's a default set selectet, if it is, append that data to the list
    pre_dict = {'Pre1':pre1, 'Pre15':pre15, 'Pre20':pre20, 'Pre30':pre30, 'Pre40':pre40, 'Pre50':pre50}

    if pre_det.get() != 'No':
        which_pre = pre_det.get()

        for u in pre_dict.get(which_pre):
            data.append(u)
    # if there's no defaul selected, create a random list with the size you selected
    else:
        for n in range(1, size + 1):
            data.append(n)
        random.shuffle(data)

    drawdata(data, ['black' for x in range(len(data)+1)]) # call the drawdata function and create the squares

def Start_alg():
    global data, size, crono, speed_entry

    try:
        speed = float(speed_entry.get())
    except:
        speed = 0

    if alg_menu.get() == "Bubble Sort": # if buble sort selected:
        start = time.perf_counter() # start a timer
        bubble_sort(data, drawdata, speed)  # call the sort function
        end = time.perf_counter()   # stop the timer when the function ends
        timetext = str(f'Bubble {size} en {round(end - start, 2)} \n')  # write the timing in the program
        crono.insert(0.0, str(timetext))    

    elif alg_menu.get() == "Quick Sort":
        start = time.perf_counter()
        quick_sort(data, 0, len(data)-1, drawdata, speed)
        drawdata(data, ['green' for x in range(len(data))])
        end = time.perf_counter()
        timetext = str(f'Quick {size} en {round(end - start, 2)} \n')
        crono.insert(0.0, str(timetext))

    elif alg_menu.get() == "Insertion Sort":
        start = time.perf_counter()
        insertion(data, drawdata, speed)
        end = time.perf_counter()
        timetext = str(f'Insertion {size} en {round(end - start, 2)} \n')
        crono.insert(0.0, str(timetext))

    elif alg_menu.get() == "Merge Sort":
        start = time.perf_counter()
        merge_sort(data, drawdata, speed)
        end = time.perf_counter()
        timetext = str(f'Merge {size} en {round(end - start, 2)} \n')
        crono.insert(0.0, str(timetext))

    elif alg_menu.get() == "Selection Sort":
        start = time.perf_counter()
        selection(data, drawdata, speed)
        drawdata(data, ['green' for x in range(len(data))])
        end = time.perf_counter()
        timetext = str(f'Selection {size} en {round(end - start, 2)} \n')
        crono.insert(0.0, str(timetext))

    elif alg_menu.get() == "Opti Bubble Sort":
        start = time.perf_counter()
        opti_bubble(data, drawdata, speed)
        end = time.perf_counter()
        timetext = str(f'Opti bubble {size} en {round(end - start, 2)} \n')
        crono.insert(0.0, str(timetext))

    elif alg_menu.get() == "Random Sort":
        start = time.perf_counter()
        random_sorts(data, drawdata, speed)
        end = time.perf_counter()
        timetext = str(f'Random {size} en {round(end - start, 2)} i {len(trys)} intents \n')
        crono.insert(0.0, str(timetext))
    
    else:
        pass

def selected_search():
    global nEntry, ser_menu, data, size, speed_entry

    # check if the value is correct, if it's not, set a defaul of 2
    try:
        n = int(nEntry.get())
    except:
        n = 2

    try:
        speed = float(speed_entry.get())
    except:
        speed = 0

    if int(nEntry.get()) > len(data):
        crono.insert(0.0, 'The data is not in here \n')

    else:
        if ser_menu.get() == "Linear Search":
            start = time.perf_counter() # start timer
            linear(data, n, drawdata, speed)    # call the function
            end = time.perf_counter()   # stop timer
            timetext = str(f'Linear {n}, {size} en {round(end - start, 5)} \n')
            crono.insert(0.0, str(timetext))    # write the times in the screen

        elif ser_menu.get() == "Binary Search":
            start = time.perf_counter()
            binary(data, n-1, 0, len(data)-1, drawdata, speed)
            end = time.perf_counter()
            timetext = str(f'Binary {n}, {size} en {round(end - start, 5)} \n')
            crono.insert(0.0, str(timetext))

# frames
canvas = Canvas(root, width=widthr, height=heightr, bg="white")
canvas.grid(row=2, column=0, padx=10, pady=2)

# ui
Label(menu, text="Algs:", bg="lightblue1").grid(row=0, column=0, padx=0, pady=0)
alg_menu = Combobox(menu, textvariable=selected_alg, values=['No' , 'Bubble Sort', 'Opti Bubble Sort', 'Random Sort', 'Selection Sort', 'Insertion Sort', 'Quick Sort', 'Merge Sort'])
alg_menu.grid(row=0, column=1, padx=2, pady=2)
alg_menu.current([0])
Button(menu, text='Create', font=("arial", 13), command=generate, bg='white').grid(row=0, column=2, padx=5, pady=5)

Label(menu, text="Search:", bg="lightblue1").grid(row=1, column=0, padx=5, pady=5)
ser_menu = Combobox(menu, textvariable=selected_search, values=['No' ,'Linear Search', 'Binary Search'])
ser_menu.grid(row=1, column=1, padx=2, pady=2)
ser_menu.current([0])
#ser_menu.current(2) # delete this after testing
nEntry = Entry(menu, width=10)
nEntry.grid(row=1, column=2, padx=2, pady=2, sticky=W)
#nEntry.insert(END, 30) #delete this after testing

Label(menu, text="Number of data ", bg='lightblue1').grid(row=2, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Entry(menu, width=15)
sizeEntry.grid(row=2, column=1, padx=2, pady=2, sticky=W)

pre_det = Combobox(menu, textvariable=dades_pre, values=['No', 'Pre1', 'Pre15', 'Pre20', 'Pre30', 'Pre40', 'Pre50'])
pre_det.grid(row=1, column=3, padx=2, pady=2)
pre_det.current([0])
#pre_det.current(1) # delete this after testing

crono = Text(menu, width=35, height=6, state='normal')
crono.grid(row=0, column=3)

order = Button(menu, text='Order!', font=("arial", 18), command=Start_alg, bg='red')
order.grid(row=2, column=2, padx=2, pady=2)
order = Button(menu, text='Find', font=("arial", 18), command=selected_search, bg='red')
order.grid(row=2, column=3, padx=2, pady=2)


Label(menu, text="      Speed:", bg='lightblue1').grid(row=3, column=0, padx=5, pady=5, sticky=W)
speed_entry = Entry(menu, width=15)
speed_entry.grid(row=3, column=1, padx=2, pady=2, sticky=W)

menu.mainloop()
root.mainloop()