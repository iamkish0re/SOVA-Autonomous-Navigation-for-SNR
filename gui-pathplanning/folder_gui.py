from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import shutil


def fg():
    class Root(Tk):
        def __init__(self):
            super(Root, self).__init__()
            self.title("Select your Photo!")
            self.minsize(400, 200)
            #self.wm_iconbitmap('icon.ico')

            self.labelFrame = ttk.LabelFrame(self, text = "Open File")
            self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)

            #self.button()
            self.src = self.fileDialog()
            self.fileCopy(self.src)
            self.checkbox()
            #self.Button(self, text='Quit', command=self.quit).grid(row=4, sticky=W, pady=4)


        #def button(self):
        #   self.button = ttk.Button(self, text = "OK")
        #  self.button.grid(column = 1, row = 1)


        def fileDialog(self):

            self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
            (("jpeg files","*.jpg"),("all files","*.*")) )
            self.label = ttk.Label(self.labelFrame, text = "")
            self.label.grid(column = 1, row = 2)
            self.label.configure(text = "Chosen file : " + self.filename)

            return self.filename

        def fileCopy(self, srcpath):
            self.currentDirec = os.getcwd()
            despath = "C:\\Users\\kisho\\Desktop\\HAWK_V2.0\\User_faces"
            folder_exist = os.path.exists(despath)

            if(folder_exist):
                shutil.copy(srcpath, despath)
            else:
                os.mkdir(despath)
                shutil.copy(srcpath, despath)

        def checkbox(self):
        #Label(frame, )
        #print("Brightness Flag: %d,\nPrivacy Flag: %d,\nAuto Lock Flag: %d" % (BRIGHTFLAG.get(), PRIVACYFLAG.get(), LOCKFLAG.get()))
            self.BRIGHTFLAG = IntVar()
            self.PRIVACYFLAG = IntVar()
            self.LOCKFLAG = IntVar()

            Label(self, text="Select ...").grid(row=0, sticky=W)

            Checkbutton(self, text="Brightness", variable= self.BRIGHTFLAG).grid(row=3, sticky=W)
            Checkbutton(self, text="Privacy Protection", variable= self.PRIVACYFLAG).grid(row=4, sticky=W)
            Checkbutton(self, text="Auto Lock", variable=self.LOCKFLAG).grid(row=5, sticky=W)

            Button(self, text='Quit', command=self.quit).grid(row=4, column = 4, sticky=W, pady=4)
            #Button(frame, text='Show', command=).grid(row=5, sticky=W, pady=4)

        #mainloop()


    root = Root()
    root.mainloop()
