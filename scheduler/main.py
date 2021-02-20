# Authors:
# RichieSjt https://github.com/RichieSjt
# EduardoHerreraJ https://github.com/EduardoHerreraJ

import tkinter as tk
from tkinter import filedialog
import scheduler
import operator

file_path = ''

def open_txt():
    #Get the file path
    global file_path
    file_path = filedialog.askopenfilename(initialdir= "/", title = "Open Text File", filetypes = (("Text Files", "*.txt"),))

def sort_table(table, col):
    return sorted(table, key=operator.itemgetter(col))

def get_inputs():
    root.geometry("1000x700")

    micro = tk.Label(root, text = "MICRO ID", font=('bold'))
    micro.grid(row = 1, column = 6)

    micro = tk.Label(root, text = "PNAME", font=('bold'))
    micro.grid(row = 1, column = 7)

    micro = tk.Label(root, text = "CCT", font=('bold'))
    micro.grid(row = 1, column = 8)

    micro = tk.Label(root, text = "ET", font=('bold'))
    micro.grid(row = 1, column = 9)

    micro = tk.Label(root, text = "QET", font=('bold'))
    micro.grid(row = 1, column = 10)

    micro = tk.Label(root, text = "CST", font=('bold'))
    micro.grid(row = 1, column = 11)

    micro = tk.Label(root, text = "TT", font=('bold'))
    micro.grid(row = 1, column = 12)

    micro = tk.Label(root, text = "IT", font=('bold'))
    micro.grid(row = 1, column = 13)

    micro = tk.Label(root, text = "FT", font=('bold'))
    micro.grid(row = 1, column = 14)
    
    mp_n = int(number_of_microprocessors.get())
    quantum_t = int(quantum_time.get())
    context_switch_t = int(context_switch_time.get())
    stop_t = int(stop_between_switches.get())
    tables = scheduler.generate_tables(mp_n, quantum_t, context_switch_t, stop_t, file_path)

    col=0
    sorted_table=sort_table(tables,col)

    total_rows = len(tables) 
    total_columns = len(tables[0])

    for i in range(total_rows): 
        for j in range(total_columns):
             
            e = tk.Entry(root, width=5,font=('Arial',16,'bold')) 
            e.grid(row=i+2, column=j+6) 
            e.insert(tk.END, sorted_table[i][j]) 


root = tk.Tk()
root.geometry("400x300")

'''
scrollbar = tk.Scrollbar(root)
scrollbar.grid(row = 1, column = 3)

listbox = tk.Listbox(root, yscrollcommand=scrollbar.set)
for i in range(10000):
    listbox.insert(tk.END, str(i))
listbox.grid(row = 1, column = 3)

scrollbar.config(command=listbox.yview)
'''

#Labels and text inputs

title = tk.Label(root, text = "Project - Scheduler", padx = 20, pady = 20)
title.grid(row = 0, column = 1)

label_number_of_micro = tk.Label(root, text = "Number of microprocessors", anchor="w", width = 23, padx = 5, pady = 5)
number_of_microprocessors = tk.Entry(root)

label_quantum_time = tk.Label(root, text = "Quantum time", anchor="w", width = 23, padx = 5, pady = 5)
quantum_time = tk.Entry(root)

label_switch_time = tk.Label(root, text = "Context switch time", anchor="w", width = 23, padx = 5, pady = 5)
context_switch_time = tk.Entry(root)

label_stop_between_switches = tk.Label(root, text = "Stop time between switches", anchor="w", width = 23, padx = 5, pady = 5)
stop_between_switches = tk.Entry(root)


#Grid positioning

label_number_of_micro.grid(row=1,column=0)
number_of_microprocessors.grid(row=1,column=1)

label_quantum_time.grid(row=2,column=0)
quantum_time.grid(row=2,column=1)

label_switch_time.grid(row=3,column=0)
context_switch_time.grid(row=3,column=1)

label_stop_between_switches.grid(row=4,column=0)
stop_between_switches.grid(row=4,column=1)

#Buttons
#Button to select the text file from the file browser

open_button = tk.Button(root, text="Open text file", command=open_txt )
open_button.grid(row=5,column=1)

generate_table_button = tk.Button(root, text = "Generate Table", command = get_inputs, padx = 5, pady = 5)
generate_table_button.grid(row=6,column=1)

#scheduler.generate_tables(number_of_microprocessors)
root.mainloop()