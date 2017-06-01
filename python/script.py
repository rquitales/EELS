#!/usr/bin/env python
import pandas as pd
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
from tkinter import *

def eels(start = 0, end = 0):
    df = pd.read_csv(askopenfilename(),sep='\t',header=None,)
    df = df.transpose()
    df = df.dropna()
    step = (end - start)/(len(df) - 1)

    if (step != 0):
        df['x'] = range(0, len(df))
        df['x'] = start + step * df['x']
        df['y'] = df[0]
        del df[0]
    else:
        df['y'] = df[0]
        del df[0]

    filename = asksaveasfilename(filetypes=(("XY File", "*.xy"), ("TAB Separated File", "*.txt"), ("Comma Separated File", "*.csv"), ("All Files", "*.*")))
    if filename[-3:] == "csv":
        df.to_csv(filename, header=True, index=False)
    else:
        df.to_csv(filename, header=True, index=False, sep='\t')

    root.quit()

root = Tk()
root.title("EELS Transposer")
Label(root, text="Please enter the start and end eV for x-axis generation. Leave 0 if not required.").grid(row=0)
Label(root, text="Start eV").grid(row=1)
Label(root, text="End eV").grid(row=2)
Label(root, text="Created by Ramon Quitales").grid(row=3)

e1 = Entry(root)
e2 = Entry(root)
e1.insert(END, '0')
e2.insert(END, '0')

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)

Button(root, text='Load & Save', command=lambda: eels(start = int(e1.get()), end = int(e2.get()))).grid(row=3, column=1, sticky=W, pady=4)
mainloop()
