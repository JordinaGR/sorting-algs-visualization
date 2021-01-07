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
import csv
import pandas as pd

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

#menu.geometry('735x200+20+0')

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
    global data, pre, pre1, pre2, pre3, pre4, pre5, size

    try:    # if the size is not valid, set a default
        size = int(sizeEntry.get())
    except ValueError:
        size = 0

    data = []

    # check if there's a default set selectet, if it is, append that data to the list
    pre_dict = {'Pre':pre, 'Pre1':pre1, 'Pre2':pre2, 'Pre3':pre3, 'Pre4':pre4, 'Pre5':pre5}

    if pre_det.get() != 'No':
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

    if algtype == 'sort':
        dfso = '/home/jordina/Desktop/programes python/sorting_alg/db/sortdata.csv'
        with open(dfso, 'a') as df:
            w = csv.writer(df)
            w.writerow([alg, size, sec, speed])


    elif algtype == 'search':
        dfse = '/home/jordina/Desktop/programes python/sorting_alg/db/searchdata.csv'
        with open(dfse, 'a') as df:
            w = csv.writer(df)
            w.writerow([alg, size, sec, sdata, speed])

def Start_alg():
    global data, size, crono, speed_entry

    if checkvar.get() == 1:
        menu.iconify()
        time.sleep(1)

    try:
        speed = float(speed_entry.get())
    except:
        speed = 0

    if alg_menu.get() == "Bubble Sort": # if buble sort selected:
        start = time.perf_counter() # start a timer
        bubble_sort(data, drawdata, speed)  # call the sort function
        end = time.perf_counter()   # stop the timer when the function ends
        timetext = str(f'Bubble {size} en {round(end - start, 5)} \n')  # write the timing in the program
        crono.insert(0.0, str(timetext))
        time.sleep(1)
        menu.deiconify()
        database('sort', 'bubble', size, round(end - start, 5), 'sdata', speed)

    elif alg_menu.get() == "Quick Sort":
        start = time.perf_counter()
        quick_sort(data, 0, len(data)-1, drawdata, speed)
        end = time.perf_counter()
        drawdata(data, ['green' for x in range(len(data))])
        timetext = str(f'Quick {size} en {round(end - start, 5)} \n')
        crono.insert(0.0, str(timetext))
        time.sleep(1)
        menu.deiconify() 
        database('sort', 'quick', size, round(end - start, 5), 'sdata', speed)

    elif alg_menu.get() == "Insertion Sort":
        start = time.perf_counter()
        insertion(data, drawdata, speed)
        end = time.perf_counter()
        timetext = str(f'Insertion {size} en {round(end - start, 5)} \n')
        crono.insert(0.0, str(timetext))
        time.sleep(1)
        menu.deiconify() 
        database('sort', 'insertion', size, round(end - start, 5), 'sdata', speed)

    elif alg_menu.get() == "Merge Sort":
        start = time.perf_counter()
        merge_sort(data, drawdata, speed)
        end = time.perf_counter()
        timetext = str(f'Merge {size} en {round(end - start, 5)} \n')
        crono.insert(0.0, str(timetext))
        time.sleep(1)
        menu.deiconify() 
        database('sort', 'merge', size, round(end - start, 5), 'sdata', speed)

    elif alg_menu.get() == "Selection Sort":
        start = time.perf_counter()
        selection(data, drawdata, speed)
        end = time.perf_counter()
        drawdata(data, ['green' for x in range(len(data))])
        timetext = str(f'Selection {size} en {round(end - start, 5)} \n')
        crono.insert(0.0, str(timetext))
        time.sleep(1)
        menu.deiconify() 
        database('sort', 'selection', size, round(end - start, 5), 'sdata', speed)

    elif alg_menu.get() == "Opti Bubble Sort":
        start = time.perf_counter()
        opti_bubble(data, drawdata, speed)
        end = time.perf_counter()
        timetext = str(f'Opti bubble {size} en {round(end - start, 5)} \n')
        crono.insert(0.0, str(timetext))
        time.sleep(1)
        menu.deiconify() 
        database('sort', 'optibubble', size, round(end - start, 5), 'sdata', speed)

    elif alg_menu.get() == "Random Sort":
        start = time.perf_counter()
        random_sorts(data, drawdata, speed)
        end = time.perf_counter()
        timetext = str(f'Random {size} en {round(end - start, 5)} i {len(trys)} intents \n')
        crono.insert(0.0, str(timetext))
        time.sleep(1)
        menu.deiconify()
        database('sort', 'bogo', size, round(end - start, 5), 'sdata', speed)

    elif alg_menu.get() == "Shell Sort":
        start = time.perf_counter()
        shell(data, drawdata, speed)
        end = time.perf_counter()
        drawdata(data, ['green' for x in range(len(data))])
        timetext = str(f'Shell {size} en {round(end - start, 5)} \n')
        crono.insert(0.0, str(timetext))
        time.sleep(1)
        menu.deiconify()
        database('sort', 'shell', size, round(end - start, 5), 'sdata', speed)

    elif alg_menu.get() == "Counting Sort":
        start = time.perf_counter()
        counting(data, drawdata, speed)
        end = time.perf_counter()
        timetext = str(f'Counting {size} en {round(end - start, 5)} \n')
        crono.insert(0.0, str(timetext))
        time.sleep(1)
        menu.deiconify()
        database('sort', 'counting', size, round(end - start, 5), 'sdata', speed)

    elif alg_menu.get() == "Radix Sort":
        start = time.perf_counter()
        radixSort(data, drawdata, speed)
        end = time.perf_counter()
        drawdata(data, ['green' for x in range(len(data))])
        timetext = str(f'Radix {size} en {round(end - start, 5)} \n')
        crono.insert(0.0, str(timetext))
        time.sleep(1)
        menu.deiconify()
        database('sort', 'radix', size, round(end - start, 5), 'sdata', speed)

    elif alg_menu.get() == "Cocktail Sort":
        start = time.perf_counter()
        cocktail(data, drawdata, speed)
        end = time.perf_counter()
        drawdata(data, ['green' for x in range(len(data))])
        timetext = str(f'Cocktail {size} en {round(end - start, 5)} \n')
        crono.insert(0.0, str(timetext))
        time.sleep(1)
        menu.deiconify()
        database('sort', 'cocktail', size, round(end - start, 5), 'sdata', speed)

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

        if checkvar.get() == 1:
            menu.iconify()
            time.sleep(1)

        if ser_menu.get() == "Linear Search":
            start = time.perf_counter() # start timer
            linear(data, n, drawdata, speed)    # call the function
            end = time.perf_counter()   # stop timer
            timetext = str(f'Linear {n}, {size} en {round(end - start, 4)} \n')
            crono.insert(0.0, str(timetext))    # write the times in the screen
            time.sleep(1)
            menu.deiconify() 
            database('search', 'linear', size, round(end - start, 5), n, speed)

        elif ser_menu.get() == "Binary Search":
            start = time.perf_counter()
            binary(data, n-1, 0, len(data)-1, drawdata, speed)
            end = time.perf_counter()
            timetext = str(f'Binary {n}, {size} en {round(end - start, 5)} \n')
            crono.insert(0.0, str(timetext))
            time.sleep(1)
            menu.deiconify()
            database('search', 'binary', size, round(end - start, 5), n, speed)

        elif ser_menu.get() == "Exponential Search":
            start = time.perf_counter()
            exponential(data, n-1, drawdata, speed)
            end = time.perf_counter()
            timetext = str(f'Exponential {n}, {size} en {round(end - start, 5)} \n')
            crono.insert(0.0, str(timetext))
            time.sleep(1)
            menu.deiconify()
            database('search', 'exponential', size, round(end - start, 5), n, speed)

def save_func():
    global savedArr

    if len(data) == 0:
        textt = str('Gen data first\n')
        crono.insert(0.0, str(textt))
    else:
        savedArr = data
        textt = str('Successfuly saved\n')
        crono.insert(0.0, str(textt))

def use_func():
    global savedArr

    drawdata(savedArr, ['black' for x in range(len(savedArr)+1)])

def dbinfo():
    from other.database_button import database_func
    database_func()


# frames
canvas = Canvas(root, width=widthr, height=heightr, bg="white")
canvas.grid(row=2, column=0, padx=10, pady=2)

# ui
Label(menu, text="Algs:", bg="lightblue1").grid(row=0, column=0, padx=0, pady=0)
alg_menu = Combobox(menu, textvariable=selected_alg, values=['No' , 'Bubble Sort', 'Opti Bubble Sort', 'Random Sort', 'Selection Sort', 'Insertion Sort', 'Quick Sort', 'Merge Sort', 'Shell Sort', 'Counting Sort', 'Radix Sort', 'Cocktail Sort'])
alg_menu.grid(row=0, column=1, padx=2, pady=2)
alg_menu.current([0])
Button(menu, text='Create', font=("arial", 13), command=generate, bg='white').grid(row=0, column=2, padx=5, pady=5)

Label(menu, text="Search:", bg="lightblue1").grid(row=1, column=0, padx=5, pady=5)
ser_menu = Combobox(menu, textvariable=selected_search, values=['No' ,'Linear Search', 'Binary Search', 'Exponential Search'])
ser_menu.grid(row=1, column=1, padx=2, pady=2)
ser_menu.current([0])
#ser_menu.current(2) # delete this after testing
nEntry = Entry(menu, width=10)
nEntry.grid(row=1, column=2, padx=2, pady=2, sticky=W)
#nEntry.insert(END, 30) #delete this after testing

Label(menu, text="Number of data: ", bg='lightblue1').grid(row=2, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Entry(menu, width=15)
sizeEntry.grid(row=2, column=1, padx=2, pady=2, sticky=W)

pre_det = Combobox(menu, textvariable=dades_pre, values=['No', 'Pre', 'Pre1', 'Pre2', 'Pre3', 'Pre4', 'Pre5'])
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

Label(menu, text="Data mode:", bg='lightblue1').grid(row=3, column=2, padx=5, pady=5, sticky=W)
datamode_comb = Combobox(menu, textvariable=datamode_var, values=['Normal','Random', 'Repited', 'Inverted'])
datamode_comb.current(0)
datamode_comb.grid(row=3, column=3, padx=2, pady=2, sticky=W)

repited_times = Entry(menu, width=15)
repited_times.grid(row=3, column=4, padx=2, pady=2, sticky=W)

quit_but = Button(menu, text='Quit', font=("arial", 18), command=quit_func, bg='yellow')
quit_but.grid(row=0, column=4, padx=2, pady=2)

save_but = Button(menu, text='Save', font=("arial", 18), command=save_func, bg='green')
save_but.grid(row=0, column=5, padx=2, pady=2)

use_but = Button(menu, text='Use', font=("arial", 18), command=use_func, bg='green')
use_but.grid(row=1, column=5, padx=2, pady=2)

database_info_but = Button(menu, text='Database', font=('arial', 18), command=dbinfo, bg='royalblue1')
database_info_but.grid(row=2, column=5, padx=2, pady=2)

checkbox_wind = Checkbutton(menu, text='Minimize?', variable=checkvar, onvalue=1, offvalue=0, heigh=5, width=20, bg='lightblue1')
checkbox_wind.config(activebackground='lightblue2')

checkbox_wind.grid(row=2, column=4)

menu.mainloop()
root.mainloop()
