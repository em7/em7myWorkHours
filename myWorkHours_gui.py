import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as tkst


class MyWorkHoursMainWin(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        if not (self.master == None):
            self.master.title("Hello")
            
        self.pack(fill='both', expand='yes', padx=5, pady=5)
        self.createWidgets()
        self.createMenu()

    def createWidgets(self):
        
        self.hours_label = ttk.Label(self)
        self.hours_label["text"] = u"Please paste the work hour report copied from\n" \
                + "the WebTerm website, one per line\n" \
                + "(= copied from Chrome or IE, Firefox puts them on different lines)."
        self.hours_label.grid(row=0,column=0,sticky='W',columnspan=4)
        
        self.hours_scrollbar = ttk.Scrollbar(self)
        self.hours_edit = tk.Text(self, width=10, height=10, wrap='word',
                                  yscrollcommand=self.hours_scrollbar.set)
        self.hours_scrollbar.config(command=self.hours_edit.yview)
        self.hours_edit.grid(row=1,column=0,columnspan=3,sticky='NEWS',
                             pady=5)
        self.hours_scrollbar.grid(row=1,column=3,sticky='NSE',pady=5)
        
        self.time_label = ttk.Label(self)
        self.time_label["text"] = u"Computed time:"
        self.time_label.grid(row=2,column=0,sticky='W')

        self.time_comp = ttk.Label(self)
        self.time_comp["text"] = u"comptime:0"
        self.time_comp.grid(row=2,column=1,sticky='W', padx=5)
        
        self.compute_button = ttk.Button(self)
        self.compute_button["text"] = "Compute"
        self.compute_button["command"] = self.compute
        self.compute_button.grid(row=2,column=2,columnspan=2,sticky='W')

        self.grid_columnconfigure(1,weight=2)
        self.grid_columnconfigure(2,weight=1)
        self.grid_rowconfigure(1,weight=1)
        
    def createMenu(self):
        self.menubar = tk.Menu(self)
        
        self.myWorkHours_menu = tk.Menu(self.menubar, tearoff=0)
        self.myWorkHours_menu.add_command(label="About", command=self.about)
        self.myWorkHours_menu.add_separator()
        self.myWorkHours_menu.add_command(label="Exit", command=root.destroy)
        
        self.menubar.add_cascade(label="Program", menu=self.myWorkHours_menu)
        
        root.config(menu=self.menubar)

    def compute(self):
        tl = tk.Toplevel(self)
        
    def about(self):
        tl = tk.Toplevel(self)

if __name__ == '__main__':
    root = tk.Tk()
    app = MyWorkHoursMainWin(master=root)
    app.mainloop()
