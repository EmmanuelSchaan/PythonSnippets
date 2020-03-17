import Tkinter as tk

class App:
   
   def __init__(self, master):
      
      # the frame widget is a child of the parent widget (master)
      frame = tk.Frame(master)
      # make the frame visible
      frame.pack()
      
      # create button, child of the frame
      self.button = tk.Button(frame, text="QUIT", fg="red", command=frame.quit)
      # place the button as far left as possible
      self.button.pack(side=tk.LEFT)
      
      # another button
      self.hi_there = tk.Button(frame, text="Hello", command=self.say_hi)
      self.hi_there.pack(side=tk.LEFT)
   
   def say_hi(self):
      print "hi there, everyone!"



root = tk.Tk()
app = App(root)
root.mainloop()
# optional; makes sure the python process ends when the main loop ends
root.destroy()