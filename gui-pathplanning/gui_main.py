from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("475x150")
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")

B1 = Button(top, text = "Generate WayPoints", command = helloCallBack)
B1.place(x = 50,y = 50)
B2 = Button(top, text = "Start Drone", command = print("Connecting to tello"))
B2.place(x = 200,y = 50)
B3 = Button(top, text = "Check waypoints", command = print("Checking for waypoints"))
B3.place(x = 300,y = 50)
top.mainloop()