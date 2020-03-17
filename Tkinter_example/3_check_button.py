import Tkinter as tk



# to do when check button is clicked
def onclick():
   print var.get()



# main window
root = tk.Tk()

# check button
var = tk.IntVar()
c = tk.Checkbutton(root, text="Choose 1 over 0", variable=var, command=onclick)
c.pack()

# enter main loop
tk.mainloop()