import os, time, csv, random
from tkinter import *
from tkinter.ttk import Combobox
from algs.bubble_sort import bubble_sort
from algs.quick_sort import quick_sort
from algs.insertion_sort import insertion
from algs.linear_search import linear
from algs.merge_sort import merge_sort
from algs.selection_sort import selection
from algs.binary_search import binary
from algs.opti_bubble_sort import opti_bubble
from algs.random_sort import random_sorts
from algs.shell_sort import shell
from algs.exponential_search import exponential
from algs import random_sort
from algs.counting_sort import counting
from algs.radix_sort import radixSort
from algs.cocktail_sort import cocktail
from pre import pre
from pre import pre1
from pre import pre2
from pre import pre3
from pre import pre4
from pre import pre5
import pandas as pd

# start a tkinter window
root = Tk()
widthr = 1700
heightr = 850

# set minsize
root.minsize(1600, 850)
root.config(bg="white")
root.title("Sorting algorithms visualization")

# vars
selected_alg = StringVar()
dades_pre = StringVar()
datamode_var = StringVar()
checkvar = IntVar()
data = []
trys = random_sort.trys
pre = pre.pre
pre1 = pre1.pre1
pre2 = pre2.pre2
pre3 = pre3.pre3
pre4 = pre4.pre4
pre5 = pre5.pre5
savedArr = []

# draw the rectangles
def drawdata(data, colorarray):
    canvas.delete("all")
    c_height = 700
    c_width = 1600
    x_width = c_width / (len(data) + 1)
    offset = 0
    spacing = 0
    normalizeddata = [i / max(data) for i in data]

    for i, height in enumerate(normalizeddata):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * c_height
        x1 = (i+1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorarray[i])

    root.update_idletasks() # update the triangles

# generate an array
def generate():
    global data, pre, pre1, pre2, pre3, pre4, pre5, size

    try:    # if the size is not valid, set a default
        size = int(sizeEntry.get())
    except ValueError:
        size = 0

    data = []

    # check if there's a default set selectet, if it is, append that data to the list
    pre_dict = {'Pre':pre, 'Pre1':pre1, 'Pre2':pre2, 'Pre3':pre3, 'Pre4':pre4, 'Pre5':pre5}

    if pre_det.get() != 'No Default':
        which_pre = pre_det.get()

        for u in pre_dict.get(which_pre):
            data.append(u)

    elif datamode_comb.get() != 'Normal':
        if datamode_comb.get() == 'Random':
            for n in range(1, size + 1):
                data.append(random.randint(1, size + 1))

        elif datamode_comb.get() =='Inverted':
            i = size
            while i:
                data.append(i)
                i -=1

        elif datamode_comb.get() == 'Repited':
            times = int(repited_times.get())
            num = size // times
            val = 1

            while times > 0:
                for i in range(num):
                    data.append(val)
                val += 1
                times -= 1
            random.shuffle(data)

    # if there's no defaul selected, create a random list with the size you selected
    else:
        for n in range(1, size + 1):
            data.append(n)
        random.shuffle(data)

    drawdata(data, ['black' for x in range(len(data)+1)]) # call the drawdata function and create the squares

def quit_func():
    quit()


def database(algtype, alg, size, sec, sdata, speed):
    # open the file and add a row in the corresponding database
    if algtype == 'sort':
        dfso = 'sorting-algs-visualization/db/sortdata.csv'
        with open(dfso, 'a') as df:
            w = csv.writer(df)
            w.writerow([alg, size, sec, speed])


    elif algtype == 'search':
        dfse = 'sorting-algs-visualization/db/searchdata.csv'
        with open(dfse, 'a') as df:
            w = csv.writer(df)
            w.writerow([alg, size, sec, sdata, speed])

def sorting_algs_func(alg_name, end, start, size, speed):
    timetext = str(f'{alg_name} {size} en {round(end - start, 5)} \n')
    crono.insert(0.0, str(timetext))
    time.sleep(1)
    database('sort', alg_name, size, round(end - start, 5), 'sdata', speed)


def Start_alg():
    global data, size, crono, speed_entry

    if checkvar.get() == 1:
        time.sleep(1)

    try:
        speed = float(speed_entry.get())
    except:
        speed = 0

    if alg_menu.get() == "Bubble Sort":     # if buble sort selected:
        start = time.perf_counter()         # start a timer
        bubble_sort(data, drawdata, speed)  # call the sort function
        end = time.perf_counter()           # stop the timer when the function ends
        sorting_algs_func('bubble', end, start, size, speed)

    elif alg_menu.get() == "Quick Sort":
        start = time.perf_counter()
        quick_sort(data, 0, len(data)-1, drawdata, speed)
        end = time.perf_counter()
        drawdata(data, ['green' for x in range(len(data))])
        sorting_algs_func('quick', end, start, size, speed)

    elif alg_menu.get() == "Insertion Sort":
        start = time.perf_counter()
        insertion(data, drawdata, speed)
        end = time.perf_counter()
        sorting_algs_func('insertion', end, start, size, speed)

    elif alg_menu.get() == "Merge Sort":
        start = time.perf_counter()
        merge_sort(data, drawdata, speed)
        end = time.perf_counter()
        sorting_algs_func('merge', end, start, size, speed)

    elif alg_menu.get() == "Selection Sort":
        start = time.perf_counter()
        selection(data, drawdata, speed)
        end = time.perf_counter()
        drawdata(data, ['green' for x in range(len(data))])
        sorting_algs_func('selection', end, start, size, speed)

    elif alg_menu.get() == "Opti Bubble Sort":
        start = time.perf_counter()
        opti_bubble(data, drawdata, speed)
        end = time.perf_counter()
        sorting_algs_func('optibubble', end, start, size, speed)

    elif alg_menu.get() == "Bogo Sort":
        start = time.perf_counter()
        random_sorts(data, drawdata, speed)
        end = time.perf_counter()
        sorting_algs_func('bogo', end, start, size, speed)

    elif alg_menu.get() == "Shell Sort":
        start = time.perf_counter()
        shell(data, drawdata, speed)
        end = time.perf_counter()
        drawdata(data, ['green' for x in range(len(data))])
        sorting_algs_func('shell', end, start, size, speed)

    elif alg_menu.get() == "Counting Sort":
        start = time.perf_counter()
        counting(data, drawdata, speed)
        end = time.perf_counter()
        sorting_algs_func('counting', end, start, size, speed)

    elif alg_menu.get() == "Radix Sort":
        start = time.perf_counter()
        radixSort(data, drawdata, speed)
        end = time.perf_counter()
        drawdata(data, ['green' for x in range(len(data))])
        sorting_algs_func('radix', end, start, size, speed)

    elif alg_menu.get() == "Cocktail Sort":
        start = time.perf_counter()
        cocktail(data, drawdata, speed)
        end = time.perf_counter()
        drawdata(data, ['green' for x in range(len(data))])
        sorting_algs_func('cocktail', end, start, size, speed)

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
            start = time.perf_counter()         # start timer
            linear(data, n, drawdata, speed)    # call the function
            end = time.perf_counter()           # stop timer
            timetext = str(f'Linear {n}, {size} en {round(end - start, 4)} \n')
            crono.insert(0.0, str(timetext))    # write the times in the screen
            database('search', 'linear', size, round(end - start, 5), n, speed)

        elif ser_menu.get() == "Binary Search":
            start = time.perf_counter()
            binary(data, n-1, 0, len(data)-1, drawdata, speed)
            end = time.perf_counter()
            timetext = str(f'Binary {n}, {size} en {round(end - start, 5)} \n')
            crono.insert(0.0, str(timetext))
            database('search', 'binary', size, round(end - start, 5), n, speed)

        elif ser_menu.get() == "Exponential Search":
            start = time.perf_counter()
            exponential(data, n-1, drawdata, speed)
            end = time.perf_counter()
            timetext = str(f'Exponential {n}, {size} en {round(end - start, 5)} \n')
            crono.insert(0.0, str(timetext))
            database('search', 'exponential', size, round(end - start, 5), n, speed)

def save_func():        # a function to save the array in a button and use it on the use_func
    global savedArr

    if len(data) == 0:
        textt = str('Gen data first\n')
        crono.insert(0.0, str(textt))
    else:
        savedArr = data
        textt = str('Successfuly saved\n')
        crono.insert(0.0, str(textt))

def use_func():         # save the data that the save_func has saved
    global savedArr

    drawdata(savedArr, ['black' for x in range(len(savedArr)+1)])

def dbinfo():   # open the new window with the database information
    from other.database_button import database_func
    database_func()


# frames
canvas = Canvas(root, width=1600, height=700, bg="white")
canvas.place(x=0, y=150)

# ui
alg_menu = Combobox(root, width=15, textvariable=selected_alg, values=['Algs' , 'Bubble Sort', 'Opti Bubble Sort', 'Bogo Sort', 'Selection Sort', 'Insertion Sort', 'Quick Sort', 'Merge Sort', 'Shell Sort', 'Counting Sort', 'Radix Sort', 'Cocktail Sort'])
alg_menu.place(x=290, y=20)
alg_menu.current([0])
ser_menu = Combobox(root, width=15, textvariable=selected_search, values=['Search Alg' ,'Linear Search', 'Binary Search', 'Exponential Search'])
ser_menu.place(x=290, y=50)
ser_menu.current([0])
Label(root, text="Search this: ", bg='white').place(x=290, y=90)
#ser_menu.current(2) # delete this after testing
nEntry = Entry(root, width=10)
nEntry.place(x=390, y=90)
#nEntry.insert(END, 30) #delete this after testing

order = Button(root, text='Order', font=("arial", 12), command=Start_alg, bg='red')
order.place(x=440, y=15)
order = Button(root, text=' Find ', font=("arial", 12),command=selected_search, bg='red')
order.place(x=440, y=50)

Label(root, text="# data: ", bg='white').place(x=50, y=20)
sizeEntry = Entry(root, width=15)
sizeEntry.place(x=110, y=20)

Button(root, text='Create', font=("arial", 12), command=generate, bg='white').place(x=160, y=80)

pre_det = Combobox(root, width=10, textvariable=dades_pre, values=['No Default', 'Pre', 'Pre1', 'Pre2', 'Pre3', 'Pre4', 'Pre5'])
pre_det.place(x=50, y=90)
pre_det.current([0])
#pre_det.current(1) # delete this after testing

#Text widget
crono = Text(root, width=35, height=6, state='normal')
crono.place(x=1200, y=20)

Label(root, text="Speed:", bg='white').place(x=50, y=50)
speed_entry = Entry(root, width=15)
speed_entry.place(x=110, y=50)


Label(root, text="Data mode:", bg='white').place(x=600, y=20)
datamode_comb = Combobox(root, width=10, textvariable=datamode_var, values=['Normal','Random', 'Repited', 'Inverted'])
datamode_comb.current(0)
datamode_comb.place(x=700, y=20)

Label(root, text="if repided, times?", bg="white").place(x=600, y=50)
repited_times = Entry(root, width=15)
repited_times.place(x=720, y=50)

quit_but = Button(root, text='Quit', font=("arial", 12), command=quit_func, bg='red')
quit_but.place(x=1100, y=15)

save_but = Button(root, text='Save', font=("arial", 12), command=save_func, bg='red')
save_but.place(x=900 ,y=15)

use_but = Button(root, text=' Use ', font=("arial", 12), command=use_func, bg='red')
use_but.place(x=900, y=50)

database_info_but = Button(root, text='Database', font=('arial', 12), command=dbinfo, bg='red')
database_info_but.place(x=980, y=15)

root.mainloop()
