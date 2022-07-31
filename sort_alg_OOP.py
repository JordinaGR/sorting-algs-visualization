import imp
from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.config(background="white")

sc_height = int(root.winfo_screenheight())
sc_width = int(root.winfo_screenwidth())
# 810, 1536
#h = sc_height - int(sc_height/4)
#w = sc_width - int(sc_width/5)
he = 810
we = 1536

selected_alg = StringVar()
dades_pre = StringVar()
datamode_var = StringVar()

class Main:
    def __init__(self, master, w, h):
        for widgets in master.winfo_children():
            widgets.destroy()

        self.w = w
        self.h = h

        master.geometry(f"{w}x{h}")

        self.canvas = Canvas(master, width=w, height=h*0.8233, bg="white")
        self.canvas.place(x=0, y=h*0.1767)

        self.alg_menu = Combobox(master, width=int(w*0.008823), textvariable=selected_alg, values=['Algs' , 'Bubble Sort'])
        self.alg_menu.place(x=w*0.170588, y=h*0.023529)
        self.alg_menu.current([0])

        self.ser_menu = Combobox(master, width=int(w*0.0088235), textvariable=self.selected_search, values=['Search Alg' ,'Linear Search'])
        self.ser_menu.place(x=w*0.170588, y=h/17)
        self.ser_menu.current([0])

        Label(master, text="Search this: ", bg='white').place(x=w*0.170588, y=h*9/85)
        #ser_menu.current(2) # delete this after testing
        self.nEntry = Entry(master, width=int(w*3/330))
        self.nEntry.place(x=w*39/170, y=h*9/85)
        #nEntry.insert(END, 30) #delete this after testing
        
        self.order = Button(master, text='Order', font=("arial", 11), command=self.Start_alg, bg='red')
        self.order.place(x=w*22/85, y=h*3/170)
        self.order = Button(master, text=' Find ', font=("arial", 11),command=self.selected_search, bg='red')
        self.order.place(x=w*22/85, y=h/17)

        Label(master, text="# data: ", bg='white').place(x=w/34, y=h*2/85)
        self.sizeEntry = Entry(master, width=int(w*3/340))
        self.sizeEntry.place(x=w*11/170, y=h*2/85)

        Button(master, text='Create', font=("arial", 11), command=self.generate, bg='white').place(x=w*8/85, y=h*8/85)

        self.pre_det = Combobox(master, width=int(w/170), textvariable=dades_pre, values=['No Default'])
        self.pre_det.place(x=w/34, y=h*9/85)
        self.pre_det.current([0])
        #pre_det.current(1) # delete this after testing

        #Text widget
        crono = Text(master, width=int(w*7/340), height=int(h*3/425), state='normal')
        crono.place(x=w*12/17, y=h*2/85)

        Label(master, text="Speed:", bg='white').place(x=w/34, y=h/17)
        self.speed_entry = Entry(master, width=int(w*3/340))
        self.speed_entry.place(x=w*11/170, y=h/17)

        Label(master, text="Data mode:", bg='white').place(x=w*6/17, y=h*2/85)
        self.datamode_comb = Combobox(master, width=int(w/170), textvariable=datamode_var, values=['Normal'])
        self.datamode_comb.current(0)
        self.datamode_comb.place(x=w*7/17, y=h*2/85)

        Label(master, text="if repided, times?", bg="white").place(x=w*6/17, y=h/17)
        self.repited_times = Entry(master, width=int(w*3/340))
        self.repited_times.place(x=w*36/85, y=h/17)

        self.quit_but = Button(master, text='Quit', font=("arial", 11), command=self.quit_func, bg='red')
        self.quit_but.place(x=w*11/17, y=h*3/170)

        self.save_but = Button(master, text='Save', font=("arial", 11), command=self.save_func, bg='red')
        self.save_but.place(x=w*9/17 ,y=h*3/170)

        self.use_but = Button(master, text=' Use ', font=("arial", 11), command=self.use_func, bg='red')
        self.use_but.place(x=w*9/17, y=h/17)

        self.database_info_but = Button(master, text='Database', font=('arial', 11), command=self.dbinfo, bg='red')
        self.database_info_but.place(x=w*49/85, y=h*3/170)

        self.change_scs_W = Button(master, text='x+', font=('arial', 10), bg='white', command=lambda: self.change_size_screen(1, "more"))
        self.change_scs_W.place(x=w*149/170, y=h*2/85)

        self.change_scs_H = Button(master, text='y+', font=('arial', 10), bg='white', command=lambda: self.change_size_screen(2, "more"))
        self.change_scs_H.place(x=w*77/85, y=h*2/85)

        self.change_scs_W = Button(master, text='x-', font=('arial', 10), bg='white', command=lambda: self.change_size_screen(1, "less"))
        self.change_scs_W.place(x=w*149/170, y=h*5/85)

        self.change_scs_H = Button(master, text='y-', font=('arial', 10), bg='white', command=lambda: self.change_size_screen(2, "less"))
        self.change_scs_H.place(x=w*77/85, y=h*5/85)


    def Start_alg(self):
        pass

    def selected_search(self):
        pass

    def generate(self):
        pass

    def quit_func(self):
        pass

    def save_func(self):
        pass

    def use_func(self):
        pass

    def dbinfo(self):
        pass

    def change_size_screen(self, dir, siz):
        if dir == 1 and siz == "more":
            self.w += 35
        elif dir == 2 and siz == "more":
            self.h += 35
        elif dir == 1 and siz == "less":
            self.w -= 35
        elif dir == 2 and siz == "less":
            self.h -= 35

        Main.__init__(self, root, self.w, self.h)


m = Main(root, we, he)
root.mainloop()