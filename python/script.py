#!/usr/bin/env python
import pandas as pd
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
from tkinter import *
#Message to continue



#Read datafile

root = Tk()
root.withdraw()


df=pd.read_csv(askopenfilename(),sep='\t',header=None,)

df2=df.transpose()
#Make sure resolution is 2048 datapoints not 2049
if len(df2)!=2048:
    df2=df2.drop(df2.index[len(df2)-1])
#X-axis generation dialog
user=messagebox.askyesno("Column Generation","Do you want to generate an x-axis column?")
#X-axis user diaglog response
if user == False:
    df2['y'] = df2[0]
    del df2[0]
    filename = asksaveasfilename(filetypes=(("XY File", "*.xy"), ("TAB Separated File", "*.txt"), ("Comma Separated File", "*.csv"), ("All Files", "*.*")))
    if filename[-3:] == "csv":
        df2.to_csv(filename, header=True, index=False)
    else:
        df2.to_csv(filename, header=True, index=False, sep='\t')
else:
    #Start dialog for eV input and calculations

    def submit_button_save():
        start = int(e1.get())
        end = int(e2.get())
        step = (end - start) / (len(df2) - 1)
        df2['x'] = range(0, len(df2))
        df2['x'] = start + step * df2['x']
        df2['y'] = df2[0]
        del df2[0]
        filename=asksaveasfilename(filetypes=(("XY File", "*.xy"),("TAB Separated File", "*.txt"),("Comma Separated File", "*.csv"),("All Files", "*.*") ))
        if filename[-3:]=="csv":
            df2.to_csv(filename, header=True, index=False)
        else:
            df2.to_csv(filename, header=True, index=False,sep='\t')
        master.quit()

    master = Tk()
    Label(master, text="Please enter the start and end eV for x-axis generation.").grid(row=0)
    Label(master, text="Start eV").grid(row=1)
    Label(master, text="End eV").grid(row=2)

    e1 = Entry(master)
    e2 = Entry(master)

    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)

    Button(master, text='Save & Exit', command=submit_button_save).grid(row=3, column=1, sticky=W, pady=4)
    mainloop()
