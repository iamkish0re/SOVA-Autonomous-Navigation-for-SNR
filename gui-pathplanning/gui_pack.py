import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
import shutil
from path_plan import map_points
from functools import partial
from dji_tello_sdk.start_planner import start_drone

LARGE_FONT= ("Verdana", 12)

class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self, width=300, height=300)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, minsize=250, weight=1)
        container.grid_columnconfigure(0, minsize=300, weight=1)

        self.frames = {}
        for F in (user_page,  path_planning):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(user_page)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class user_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="SOVA Navigator", font=LARGE_FONT)
        label.pack(pady=20,padx=20)

        tk.Button(self, text="Path Planning", width=25, height=1, command=lambda: controller.show_frame(path_planning)).pack(pady=3,padx=10)#ADD COMMAND LATER
        tk.Button(self, text="Face Tracking", width=25, height=1, command=lambda: print("Starting face Tracking")).pack(pady=3,padx=10)
        tk.Button(self, text="Hand Gesture Recognition", width=25, height=1, command=lambda: print("Starting Hand Gesture")).pack(pady=3,padx=10)
        tk.Button(self, text="Help", width=25, height=1, command=self.main_help).pack(pady=3,padx=10)
        tk.Button(self, text="Quit", width=25, height=1, command= self.quit).pack(pady=3,padx=10)

    def main_help(self):
        self.msg = messagebox.showinfo( "SOVA Help", "Instructions:\n1. To Start Path planning Click on 'Path Planning'\n2. To Start Face track and navigate the face Click on 'Face Tracking'\n3. To take full Hand gesture control Click on 'Hand Gesture'\n4. To close the GUI Navigator click on 'Quit' or 'X'")


class path_planning(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        T = tk.Label(self, height=2, width=30 ,text="Path Planning")
        T.pack(pady=10,padx=10)

        button2 = tk.Button(self, text="Map Path", width = 10 , command = lambda:map_points())
        button2.pack(pady=3,padx=10)
        button3 = tk.Button(self, text="Start UAV", width = 10 ,command =lambda: start_drone())
        button3.pack(pady=3,padx=10)
        button4 = tk.Button(self, text="Help", width = 10, command = self.help)
        button4.pack(pady=3,padx=10)
        button5 = tk.Button(self, text="Back", width = 10, command = lambda: controller.show_frame(user_page) )
        button5.pack(pady=3,padx=10)

    def help(self):
        self.msg = messagebox.showinfo( "Path Planning Help", "Instructions:\n1. To Map the path in the image Click on 'Map Path'\n2. To Start the drone to fly Click on 'Start UAV'\n3. To close the GUI Navigator click on 'Quit' or 'X'")
app = SeaofBTCapp()
app.title("Sova: Control Panel")
app.mainloop()

