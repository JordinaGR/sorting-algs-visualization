import mysql.connector
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
from pre import pre1
from pre import pre15
from pre import pre20
from pre import pre30
from pre import pre40
from pre import pre50

#algs
    #shell sort
    #radix sort

    #comb sort
    #heap sort

file1 = open("passw.txt", "r")
passw = file1.readline()

# connect to database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = passw,
    database = "sort_algdb")
mycursor = mydb.cursor()

# start a tkinter window
root = Tk()
root.maxsize(2000, 2000)
root.config(bg="black")
root.title("Sorting algorithms visualization")

# vars
selected_alg = StringVar()
dades_pre = StringVar()
data = []
pre1 = pre1.pre1
pre15 = pre15.pre15
pre20 = pre20.pre20
pre30 = pre30.pre30
pre40 = pre40.pre40
pre50 = pre50.pre50

# draw the rectangles
def drawdata(data, colorarray):

    canvas.delete("all")
    c_height = 750
    c_width = 1900
    x_width = c_width / (len(data) + 1)
    offset = 0
    spacing = 0
    normalizeddata = [i / max(data) for i in data]

    for i, height in enumerate(normalizeddata):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 700
        x1 = (i+1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorarray[i])

    root.update_idletasks() # update the triangles

# generate an array
def generate():
    global data
    global pre1
    global pre15
    global pre20
    global pre30
    global pre40
    global pre50
    global size

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
    global data
    global size
    global crono

    if alg_menu.get() == "Bubble Sort": # if buble sort selected:
        start = time.perf_counter() # start a timer
        bubble_sort(data, drawdata, 0)  # call the sort function
        end = time.perf_counter()   # stop the timer when the function ends
        timetext = str(f'Bubble {size} en {round(end - start, 2)} \n')  # write the timing in the program
        crono.insert(0.0, str(timetext))    
        dbb_alg = "bubble"  # create variables to insert them in the SQL table
        dbb_size = size
        dbb_sec = round(end - start, 2)
        sqlformula = "INSERT INTO sortdata (alg, size, sec) VALUES (%s, %s, %s)"
        dades = (dbb_alg, dbb_size, dbb_sec)
        mycursor.execute(sqlformula, dades)
        mydb.commit()   # insert the data

    elif alg_menu.get() == "Quick Sort":
        start = time.perf_counter()
        quick_sort(data, 0, len(data)-1, drawdata, 0)
        drawdata(data, ['green' for x in range(len(data))])
        end = time.perf_counter()
        timetext = str(f'Quick {size} en {round(end - start, 2)} \n')
        crono.insert(0.0, str(timetext))
        dbq_alg = "quick"
        dbq_size = size
        dbq_sec = round(end - start, 2)
        sqlformula = "INSERT INTO sortdata (alg, size, sec) VALUES (%s, %s, %s)"
        dades = (dbq_alg, dbq_size, dbq_sec)
        mycursor.execute(sqlformula, dades)
        mydb.commit()

    elif alg_menu.get() == "Insertion Sort":
        start = time.perf_counter()
        insertion(data, drawdata, 0)
        end = time.perf_counter()
        timetext = str(f'Insertion {size} en {round(end - start, 2)} \n')
        crono.insert(0.0, str(timetext))
        dbi_alg = "insertion"
        dbi_size = size
        dbi_sec = round(end - start, 2)
        sqlformula = "INSERT INTO sortdata (alg, size, sec) VALUES (%s, %s, %s)"
        dades = (dbi_alg, dbi_size, dbi_sec)
        mycursor.execute(sqlformula, dades)
        mydb.commit()

    elif alg_menu.get() == "Merge Sort":
        start = time.perf_counter()
        merge_sort(data, drawdata, 0)
        end = time.perf_counter()
        timetext = str(f'Merge {size} en {round(end - start, 2)} \n')
        crono.insert(0.0, str(timetext))
        dbm_alg = "merge"
        dbm_size = size
        dbm_sec = round(end - start, 2)
        sqlformula = "INSERT INTO sortdata (alg, size, sec) VALUES (%s, %s, %s)"
        dades = (dbm_alg, dbm_size, dbm_sec)
        mycursor.execute(sqlformula, dades)
        mydb.commit()

    elif alg_menu.get() == "Selection Sort":
        start = time.perf_counter()
        selection(data, drawdata, 0)
        end = time.perf_counter()
        timetext = str(f'selection {size} en {round(end - start, 2)} \n')
        crono.insert(0.0, str(timetext))
        dbm_alg = "selection"
        dbm_size = size
        dbm_sec = round(end - start, 2)
        sqlformula = "INSERT INTO sortdata (alg, size, sec) VALUES (%s, %s, %s)"
        dades = (dbm_alg, dbm_size, dbm_sec)
        mycursor.execute(sqlformula, dades)
        mydb.commit()

    else:
        pass

def selected_search():
    global nEntry
    global ser_menu
    global data
    global size
    # check if the value is correct, if it's not, set a defaul of 2
    try:
        n = int(nEntry.get())
    except:
        n = 2

    if ser_menu.get() == "Linear Search":
        start = time.perf_counter() # start timer
        linear(data, n, drawdata, 0)    # call the function
        end = time.perf_counter()   # stop timer
        timetext = str(f'Linear {n}, {size} en {round(end - start, 5)} \n')
        crono.insert(0.0, str(timetext))    # write the times in the screen

# frames
ui_frame = Frame(root, width=1900, height=150, bg="lightblue1")
ui_frame.grid(row=0, column=0, padx=0, pady=0)

canvas = Canvas(root, width=1880, height=750, bg="white")
canvas.grid(row=2, column=0, padx=10, pady=2)

# ui
Label(ui_frame, text="Algs:", bg="lightblue1").grid(row=0, column=0, padx=0, pady=0)
alg_menu = Combobox(ui_frame, textvariable=selected_alg, values=['No' , 'Bubble Sort','Selection Sort' ,'Insertion Sort', 'Quick Sort', 'Merge Sort'])
alg_menu.grid(row=0, column=1, padx=2, pady=2)
alg_menu.current([0])
Button(ui_frame, text='Create', font=("arial", 13), command=generate, bg='white').grid(row=0, column=2, padx=5, pady=5)

Label(ui_frame, text="Search:", bg="lightblue1").grid(row=1, column=0, padx=5, pady=5)
ser_menu = Combobox(ui_frame, textvariable=selected_search, values=['No' ,'Linear Search'])
ser_menu.grid(row=1, column=1, padx=2, pady=2)
ser_menu.current([0])
nEntry = Entry(ui_frame, width=10)
nEntry.grid(row=1, column=2, padx=2, pady=2, sticky=W)

Label(ui_frame, text="Nombre de barres ", bg='lightblue1').grid(row=2, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Entry(ui_frame, width=15)
sizeEntry.grid(row=2, column=1, padx=2, pady=2, sticky=W)

pre_det = Combobox(ui_frame, textvariable=dades_pre, values=['No', 'Pre1', 'Pre15', 'Pre20', 'Pre30', 'Pre40', 'Pre50'])
pre_det.grid(row=1, column=3, padx=2, pady=2)
pre_det.current([0])

crono = Text(ui_frame, width=35, height=6, state='normal')
crono.grid(row=0, column=3)

order = Button(ui_frame, text='Order!', font=("arial", 18), command=Start_alg, bg='red')
order.grid(row=2, column=2, padx=2, pady=2)
order = Button(ui_frame, text='Find', font=("arial", 18), command=selected_search, bg='red')
order.grid(row=2, column=3, padx=2, pady=2)
root.mainloop()
