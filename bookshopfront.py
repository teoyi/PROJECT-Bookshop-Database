import tkinter as tk
import tkinter.scrolledtext as tkst

class Frame1():
    def __init__(self,win):
        frame = tk.Frame(win, relief = 'groove', bd = 1)
        frame.pack(fill = 'x', expand = False)

        self.lbl1 = tk.Label(frame, text = 'Title:')
        self.t1 = tk.Entry(frame, width = 25)
        self.lbl1.grid(row = 0, column = 0, ipadx = 10, ipady = 10)
        self.t1.grid(row = 0, column = 1, sticky = 'e')

        self.lbl2 = tk.Label(frame, text = 'Author:')
        self.t2 = tk.Entry(frame, width = 25)
        self.lbl2.grid(row = 0, column = 2, ipadx = 10)
        self.t2.grid(row = 0, column = 3, sticky = 'e')

        self.lbl3 = tk.Label(frame, text = 'Year:')
        self.t3 = tk.Entry(frame, width = 25)
        self.lbl3.grid(row = 1, column = 0, ipady = 5)
        self.t3.grid(row = 1, column = 1)

        self.lbl4 = tk.Label(frame, text = 'ISBN:')
        self.t4 = tk.Entry(frame, width = 25)
        self.lbl4.grid(row = 1, column = 2)
        self.t4.grid(row = 1, column = 3)

class Frame2():
    def __init__(self,win):

        frame = tk.Frame(win)
        frame.pack(fill = 'both', side = "left", expand = False)

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

class Frame3(tk.Frame):
    def __init__(self,win):

        frame = tk.Frame(win)
        frame.pack(fill = 'both', side = "left", expand = True)

        txtbox = tkst.ScrolledText(frame, width=40, height=10)
        txtbox.pack(fill = 'both', expand=True, padx = 7, pady = 7)

class main():

    win = tk.Tk()

    win.title('Book Shop')
    win.geometry("630x370")
    top1 = Frame1(win)
    bottomleft = Frame2(win)
    bottomright = Frame3(win)
    win.mainloop()

if __name__ == '__main__':
    main()
