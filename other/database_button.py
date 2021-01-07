from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox
import pandas as pd
import csv
    
def grid(filee):
    data_grid = []

    with open(filee) as f:
        reader = csv.reader(f)
        for row in reader:
            data_grid.append(row)
 
    row = len(data_grid)
    col = len(data_grid[0])
    return row, col, data_grid

def database_func():

    file1 = '/home/jordina/Desktop/programes python/sorting_alg/db/sortdata.csv'
    file2 = '/home/jordina/Desktop/programes python/sorting_alg/db/searchdata.csv'
    dfso = pd.read_csv(file1)
    dfse = pd.read_csv(file2)

    root = Tk()
    root.minsize(600, 400)
    root.config(bg="white")
    root.title("Database information")

    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame, bg='white')
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    row, col, data_grid = grid(file1)
    scroll = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview, width=15)
    scroll.pack(side=RIGHT, fill=Y)

    my_canvas.config(yscrollcommand=scroll.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox('all')))
    
    second_frame = Frame(my_canvas, bg='white')
    my_canvas.create_window((0,0), window=second_frame, anchor='nw')

    tabControl = ttk.Notebook(second_frame) 

    tab1 = Frame(tabControl, bg='white') 
    tab2 = Frame(tabControl, bg='white') 

    tabControl.add(tab1, text ='Sorting') 
    tabControl.add(tab2, text ='Searching') 
    tabControl.pack(expand = 1, fill ="both") 

    with open(file1) as f:

        sort_row, sort_columns, data_grid = grid(file1)

        for i in range(sort_row):
            for j in range(sort_columns):
                e = Entry(tab1, width=10, font=('arial', 15), state='normal')
                if i == 0:
                    e.configure(font=('arial', 15, 'bold'))
                if i % 2 == 0:
                    e.config(bg='grey92')

                e.grid(row=i, column=j)
                e.insert(tk.END, data_grid[i][j])

    with open(file2) as f:

        row, col, data_grid = grid(file2)

        for i in range(row):
            for j in range(col):
                e = Entry(tab2, width=10, font=('arial', 15), state='normal')
                if i == 0:
                    e.configure(font=('arial', 15, 'bold'))
                if i % 2 == 0:
                    e.config(bg='grey92')

                e.grid(row=i, column=j)
                e.insert(tk.END, data_grid[i][j])


    root.mainloop()

database_func()
