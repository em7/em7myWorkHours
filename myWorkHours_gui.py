import tkinter as tk
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
import tkinter.font as font
#import tkinter.scrolledtext as tkst #not used

from myWorkHours import Counter,\
    Event,\
    InvalidEventTypeOrderException,\
    InvalidEventOverlapException,\
    InsufficientEventsException,\
    Parser

class MyWorkHoursAboutWin(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        if not (self.master == None):
            self.master.title("About My Work Hours")
            self.master.minsize(150, 150)
            self.master.resizable(width='FALSE', height='FALSE')
            
        self.pack(fill='both', expand='yes', padx=5, pady=5)
        
        boldFont = font.Font(size=16, weight='bold')
        italicFont = font.Font(size=10, slant='italic')
        
        self.app_name = ttk.Label(self, font=boldFont)
        self.app_name["text"] = "My Work Hours"
        self.app_name.grid(row=0, column=0, sticky='N')
        
        self.app_version = ttk.Label(self)
        self.app_version["text"] = "Version 1.0.2"
        self.app_version.grid(row=1, column=0, sticky='N')
        
        self.app_desc = ttk.Label(self, font=italicFont, anchor='center', justify='center')
        self.app_desc["text"] = "This is a program for counting the" \
                + "time spent in work.\nUses the format used by WebTerm software.\n" \
                + "Distributed under the terms and conditions of WTFPL - http://www.wtfpl.net"
        self.app_desc.grid(row=2, column=0, sticky='N',pady=10)
        
        self.close_btn = ttk.Button(self)
        self.close_btn["text"] = "Close"
        self.close_btn["command"] = root.destroy
        self.close_btn.grid(row=3, column=0, sticky='S')
        

class MyWorkHoursMainWin(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        if not (self.master == None):
            self.master.title("Hello")
            self.master.minsize(450, 300)
            
        self.pack(fill='both', expand='yes', padx=5, pady=5)
        self.createVariables()
        self.createWidgets()
        self.createMenu()
    
    # UI creating
    def createVariables(self):
        #self.hours_input = tk.StringVar() #Text does not support this? 
        self.hours_counted = tk.StringVar()

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
        self.hours_scrollbar.grid(row=1,column=3,sticky='NSE',pady=8)
        
        self.time_label = ttk.Label(self)
        self.time_label["text"] = u"Computed time:"
        self.time_label.grid(row=2,column=0,sticky='W')

        self.time_comp = ttk.Label(self, textvariable=self.hours_counted)
        self.time_comp.grid(row=2,column=1,sticky='WE', padx=5)
        
        self.compute_button = ttk.Button(self)
        self.compute_button["text"] = "Compute"
        self.compute_button["command"] = self.compute
        self.compute_button.grid(row=2,column=2,sticky='NW')

        self.grid_columnconfigure(1,weight=2)
        self.grid_columnconfigure(2,weight=0)
        self.grid_rowconfigure(1,weight=1)
        
    def createMenu(self):
        self.menubar = tk.Menu(self)
        
        self.myWorkHours_menu = tk.Menu(self.menubar, tearoff=0)
        self.myWorkHours_menu.add_command(label="About", command=self.about)
        self.myWorkHours_menu.add_separator()
        self.myWorkHours_menu.add_command(label="Exit", command=root.destroy)
        
        self.menubar.add_cascade(label="Program", menu=self.myWorkHours_menu)
        
        root.config(menu=self.menubar)

    #UI event handlers
    def compute(self):
        events = self.parseEvents()
        if (events == -1): return
        
        assert isinstance(events, list)
        
        try:
            delta = Counter.count_event_list(events)
            self.hours_counted.set(delta)
        except Exception as exc:
            if len(exc.args) > 0: excMsg = exc.args[0]
            msgbox.showwarning("Count error", "An error occurred when counting the events:\n" + excMsg)
        
    def about(self):
        tl = tk.Toplevel()
        about = MyWorkHoursAboutWin(tl)
        
        if not (self.master == None):
            #make it modal
            about.focus_set()
            tl.transient(self.master)
            tl.grab_set()
            self.master.wait_window(tl)
        
        
    #Computing
    def parseEvents(self):
        """
         Tries to parse the input (self.hours_edit), convert it to events
    
         @returns list of Event, -1 on error
        """
        events = []
        lines = self.hours_edit.get(1.0,tk.END).splitlines()
        for line in lines:
            assert isinstance(line, str)
            if not line.strip(): continue #skip empty lines
            try:
                event = Parser.parse_from_str(line)
                events.append(event)
            except Exception as exc:
                if len(exc.args) > 0: excMsg = exc.args[0]
                response = msgbox.askquestion("Parse error",
                                   "The event '" + line.strip("\n") + "' could not be parsed:\n" + excMsg \
                                   + "\nContinuing in counting could lead to incorrect results. Do you wish to continue counting?",
                                   icon='warning')
                if (response == msgbox.NO):
                    return -1
        return events

if __name__ == '__main__':
    root = tk.Tk()
    app = MyWorkHoursMainWin(master=root)
    #app = MyWorkHoursAboutWin(master=root)
    app.mainloop()
