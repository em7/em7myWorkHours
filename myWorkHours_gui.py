import tkinter as tk

#tkdocs.com

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.hel_lbl = tk.Label(self)
        self.hel_lbl["text"] = u"HelloWorld"
        self.hel_lbl.grid(column=0,row=0,sticky='NEW')
        
        
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.grid(column=0,row=1)

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)
        self.QUIT.grid(column=0,row=2)

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
