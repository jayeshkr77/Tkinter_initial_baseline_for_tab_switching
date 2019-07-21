import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        #for adding icon to the window
        # tk.Tk.iconbitmap(self,default="name of the .ico file")
        
        #title
        tk.Tk.wm_title(self,"Title")
        
        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        
        #adding all pages to frames
        self.frames={}
        for F in (StartPage,Pageone):
            frame=F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self,cont):
        '''
        raises the frame on top to make it visible
        cont: is the page
        '''
        frame=self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    '''
    The page first page 
    '''
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        #layout normal tkinter
        label=tk.Label(self,text="Start Page")
        label.pack(pady=10,padx=10)

        button1=ttk.Button(self,text="page1",command=lambda:controller.show_frame(Pageone))
        button1.pack()

class Pageone(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="page2")
        label.pack(pady=10,padx=10)

        button1=ttk.Button(self,text="start",command=lambda:controller.show_frame(StartPage))
        button1.pack()


app = App()
app.mainloop()