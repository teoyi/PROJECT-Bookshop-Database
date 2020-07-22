import tkinter as tk

class Frame1():
    def __init__(self,win):
        frame = tk.Frame(win, bg = 'pink')
        frame.pack(fill = 'both', expand = True)

        self.lbl1 = tk.Label(frame, text = 'Title:')
        self.t1 = tk.Entry(frame, width = 25)
        self.lbl1.grid(row = 0, column = 0, ipadx = 10, ipady = 10)
        self.t1.grid(row = 0, column = 1, sticky = 'e')

        self.lbl2 = tk.Label(frame, text = 'Author:')
        self.t2 = tk.Entry(frame)
        self.lbl2.grid(row = 0, column = 2, ipadx = 10)
        self.t2.grid(row = 0, column = 3, sticky = 'e')

        self.lbl3 = tk.Label(frame, text = 'Year:')
        self.t3 = tk.Entry(frame)
        self.lbl3.grid(row = 1, column = 0, ipady = 5)
        self.t3.grid(row = 1, column = 1)

        self.lbl4 = tk.Label(frame, text = 'ISBN:')
        self.t4 = tk.Entry(frame)
        self.lbl4.grid(row = 1, column = 2)
        self.t4.grid(row = 1, column = 3)

        print(self.t1.grid.size)

class Frame2():
    def __init__(self,win):

        frame = tk.Frame(win)
        frame.pack(fill = 'x', expand = True)

        self.lbl3 = tk.Label(frame, text = 'Year:')
        self.t3 = tk.Entry(frame)
        self.lbl3.pack(side = 'left', fill = 'x', padx = 7, pady = 7)
        self.t3.pack(side = 'left', fill = 'x', expand = 1, pady = 7)

        self.lbl4 = tk.Label(frame, text = 'ISBN:')
        self.t4 = tk.Entry(frame)
        self.lbl4.pack(side = 'left', fill = 'x', padx = 7, pady = 5)
        self.t4.pack(side = 'left', fill = 'x', expand = 1, padx = 7, pady = 5)



class Frame3():
    def __init__(self,win):

        frame = tk.Frame(win)
        frame.pack(fill = 'none', side = "left", expand = False)

        self.button1 = tk.Button(frame, text = 'View All', height = 2 , width = 10)
        self.button1.pack(side = 'top', fill = 'y', pady = 5, padx = 10)

        self.button2 = tk.Button(frame, text = 'Search Entry', height = 2 , width = 10)
        self.button2.pack(side = 'top', fill = 'y', pady = 5, padx = 5)

        self.button3 = tk.Button(frame, text = 'Add Entry', height = 2 , width = 10)
        self.button3.pack(side = 'top', fill = 'y', pady = 5, padx = 5)

        self.button4 = tk.Button(frame, text = 'Update Entry', height = 2 , width = 10)
        self.button4.pack(side = 'top', fill = 'y', pady = 5, padx = 5)

        self.button5 = tk.Button(frame, text = 'Delete Entry', height = 2 , width = 10)
        self.button5.pack(side = 'top', fill = 'y', pady = 5, padx = 5)

        self.button6 = tk.Button(frame, text = 'Close Entry', height = 2 , width = 10)
        self.button6.pack(side = 'top', fill = 'y', pady = 5, padx = 5)

class Frame4():
    def __init__(self,win):

        frame = tk.Frame(win)
        frame.pack(fill = 'both', side = "left", expand = True)

        text = tk.Text(frame)

        text.pack(side = 'left', padx = 7,pady = 7)

class main():

    win = tk.Tk()

    win.title('Book Shop')
    win.geometry("600x370")
    win.columnconfigure(0, weight = 0)
    win.columnconfigure(1, weight = 1)
    win.columnconfigure(2, weight = 0)
    win.columnconfigure(3, weight = 1)


    top1 = Frame1(win)
    # top2 = Frame2(win)
    bottomleft = Frame3(win)
    bottomright = Frame4(win)
    win.mainloop()

if __name__ == '__main__':
    main()
