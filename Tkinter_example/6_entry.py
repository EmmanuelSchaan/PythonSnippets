from Tkinter import *



# main window
master = Tk()

# entry field, child of master
e = Entry(master)
e.pack()
# get the cursor in the entry field
e.focus_set()

# function executed when button is clicked
def callback():
   print e.get()

# button
b = Button(master, text="get", width=10, command=callback)
b.pack()


mainloop()
e = Entry(master, width=50)
e.pack()

text = e.get()
def makeentry(parent, caption, width=None, **options):
   Label(parent, text=caption).pack(side=LEFT)
   entry = Entry(parent, **options)
   if width:
      entry.config(width=width)
   entry.pack(side=LEFT)
   return entry

user = makeentry(parent, "User name:", 10)
password = makeentry(parent, "Password:", 10, show="*")
content = StringVar()
entry = Entry(parent, text=caption, textvariable=content)

text = content.get()
content.set(text)