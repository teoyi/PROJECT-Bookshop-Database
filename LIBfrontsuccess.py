import tkinter as tk
import os
from LIBback import Database

database = Database('lib.db')

class Widgets(tk.Frame):

    def __init__(self, win):

        # Creating functions to be used in the application
        def get_row(event):
            try:
                index = self.lstbox.curselection()[0]
                self.tuple_select = self.lstbox.get(index)
                self.e1.delete(0, tk.END)
                self.e1.insert(tk.END, self.tuple_select[1])
                self.e2.delete(0, tk.END)
                self.e2.insert(tk.END, self.tuple_select[2])
                self.e3.delete(0, tk.END)
                self.e3.insert(tk.END, self.tuple_select[3])
                self.e4.delete(0, tk.END)
                self.e4.insert(tk.END, self.tuple_select[4])
            except IndexError:
                pass

        def view_cmd():
            self.lstbox.delete(0, tk.END)
            for row in database.view_all():
                self.lstbox.insert(tk.END, row)

        def search_cmd():
            self.lstbox.delete(0,tk.END)
            for row in database.search_entry(self.title_val.get(), self.author_val.get(), self.year_val.get(), self.isbn_val.get()):
                self.lstbox.insert(tk.END, row)

        def add_cmd():
            self.lstbox.delete(0, tk.END)
            database.add_entry(self.title_val.get(), self.author_val.get(), self.year_val.get(), self.isbn_val.get())
            self.lstbox.insert(tk.END, (self.title_val.get(), self.author_val.get(), self.year_val.get(), self.isbn_val.get()))

        def update_cmd():
            database.update_entry(self.tuple_select[0],self.title_val.get(), self.author_val.get(), self.year_val.get(), self.isbn_val.get())
            print(self.tuple_select[0],self.tuple_select[1],self.tuple_select[2],self.tuple_select[3],self.tuple_select[4])

        def delete_cmd():
            database.delete_entry(self.tuple_select[0])

        def exit_cmd():
            self.win.destroy()

        # Generating Frames
        self.win = win
        self.frame = tk.Frame(win, relief = 'groove')
        self.frame.pack(fill = 'x', expand = False)
        self.frame1 = tk.Frame(win)
        self.frame1.pack(fill = 'both', side = "left", expand = False)
        self.frame2 = tk.Frame(win)
        self.frame2.pack(fill = 'both', side = "left", expand = True)

        # Entry and Label widgets
        self.title_val = tk.StringVar()
        self.lbl1 = tk.Label(self.frame, text = 'Title:')
        self.e1 = tk.Entry(self.frame, width = 25, textvariable = self.title_val)
        self.lbl1.grid(row = 0, column = 0, ipadx = 10, ipady = 10)
        self.e1.grid(row = 0, column = 1, sticky = 'e')

        self.author_val = tk.StringVar()
        self.lbl2 = tk.Label(self.frame, text = 'Author:')
        self.e2 = tk.Entry(self.frame, width = 25, textvariable = self.author_val)
        self.lbl2.grid(row = 0, column = 2, ipadx = 10)
        self.e2.grid(row = 0, column = 3, sticky = 'e')

        self.year_val = tk.StringVar()
        self.lbl3 = tk.Label(self.frame, text = 'Year:')
        self.e3 = tk.Entry(self.frame, width = 25, textvariable = self.year_val)
        self.lbl3.grid(row = 1, column = 0, ipady = 5)
        self.e3.grid(row = 1, column = 1)

        self.isbn_val = tk.StringVar()
        self.lbl4 = tk.Label(self.frame, text = 'ISBN:')
        self.e4 = tk.Entry(self.frame, width = 25, textvariable = self.isbn_val)
        self.lbl4.grid(row = 1, column = 2)
        self.e4.grid(row = 1, column = 3)

        # Button widgets
        self.button1 = tk.Button(self.frame1, text = 'View All', height = 2 , width = 10, command = view_cmd)
        self.button1.pack(side = 'top', fill = 'y', pady = 5, padx = 10)

        self.button2 = tk.Button(self.frame1, text = 'Search Entry', height = 2 , width = 10, command = search_cmd)
        self.button2.pack(side = 'top', fill = 'y', pady = 5, padx = 5)

        self.button3 = tk.Button(self.frame1, text = 'Add Entry', height = 2 , width = 10, command = add_cmd)
        self.button3.pack(side = 'top', fill = 'y', pady = 5, padx = 5)

        self.button4 = tk.Button(self.frame1, text = 'Update Entry', height = 2 , width = 10, command = update_cmd)
        self.button4.pack(side = 'top', fill = 'y', pady = 5, padx = 5)

        self.button5 = tk.Button(self.frame1, text = 'Delete Entry', height = 2 , width = 10, command = delete_cmd)
        self.button5.pack(side = 'top', fill = 'y', pady = 5, padx = 5)

        self.button6 = tk.Button(self.frame1, text = 'Exit', height = 2 , width = 10, command = exit_cmd)
        self.button6.pack(side = 'top', fill = 'y', pady = 5, padx = 5)

        # Listbox widget to display data
        self.lstbox = tk.Listbox(self.frame2, width=40, height=10)
        self.lstbox.pack(fill = 'both', expand=True, padx = 7, pady = 7)
        self.lstbox.bind('<<ListboxSelect>>', get_row)

def main():

    win = tk.Tk()
    win.title('Library')
    win.geometry("630x370")
    widgets = Widgets(win)
    win.mainloop()

if __name__ == '__main__':
    main()
