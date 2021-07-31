from tkinter import *
import tkinter as tk
from tkinter import ttk
import csv

def mouse_wheel(event):     # bind the mouse wheel to the scroll bar
    global count

    def delta(event):
        if event.num == 5 or event.delta < 0:
            return -1 
        return 1 

    count += delta(event)

def grid(filee):        # create the grid where the data is going to be showed
    data_grid = []

    with open(filee) as f:
        reader = csv.reader(f)
        for row in reader:
            data_grid.append(row)
 
    row = len(data_grid)
    col = len(data_grid[0])
    return row, col, data_grid

def database_func(count):    # main function

    # open the .csv files
    file1 = 'sorting-algs-visualization/db/sortdata.csv'
    file2 = 'sorting-algs-visualization/db/searchdata.csv'

    # start a window
    root = Tk()
    root.minsize(600, 400)
    root.config(bg="white")
    root.title("Database information")
    
    # create frames, the scrollbar and two tabs
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame, bg='white')
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    row, col, data_grid = grid(file1)
    scroll = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview, width=15)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(bg="grey30", troughcolor="light steel blue", highlightcolor="grey30", activebackground="grey30", highlightbackground="grey30")

    my_canvas.config(yscrollcommand=scroll.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox('all')))
    
    second_frame = Frame(my_canvas)
    my_canvas.create_window((0,0), window=second_frame, anchor='nw')

    tabControl = ttk.Notebook(second_frame) 

    tab1 = Frame(tabControl) 
    tab2 = Frame(tabControl) 

    tabControl.add(tab1, text ='Sorting') 
    tabControl.add(tab2, text ='Searching') 
    tabControl.pack(expand = 1, fill ="both") 

    my_canvas.bind("<Button-4>", mouse_wheel)
    my_canvas.bind("<Button-5>", mouse_wheel)

    # open file and put the information in the grid
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

database_func(0)
