import Tkinter as tk


# root widget (window)
root = tk.Tk()

# label widget, child to the root window
w = tk.Label(root, text="Hello, world!")
# fit the window to the label widget
w.pack()

# root event loop
# shows the window, and stays active until the window is closed
root.mainloop()
