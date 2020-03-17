import Tkinter as tk


# to do when one of the radio buttons is clicked
def onclick():
   print v.get()


# main window
master = tk.Tk()

# variable for radio button
v = tk.IntVar()
# first option
tk.Radiobutton(master, text="One", variable=v, value=1, command=onclick).pack(anchor=tk.W)
# second option
tk.Radiobutton(master, text="Two", variable=v, value=2, command=onclick).pack(anchor=tk.W)

# enter main loop
tk.mainloop()