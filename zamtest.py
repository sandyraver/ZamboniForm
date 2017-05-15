#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Apr 29, 2017 06:26:41 AM
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import time
import xlsxwriter
import zamtest_support

from PIL import Image, ImageTk

global banner
global bannerPhoto 

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
   
    root = Tk()
    zamtest_support.set_Tk_var()
    top = ZamTest_Form (root)
    zamtest_support.init(root, top)
    root.mainloop()

w = None
def create_ZamTest_Form(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    zamtest_support.set_Tk_var()
    top = ZamTest_Form (w)
    zamtest_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_ZamTest_Form():
    global w
    w.destroy()
    w = None

       
    

class ZamTest_Form:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("819x659+573+178")
        top.title("ZamTest Form")
        top.configure(background="#d9d9d9")
       
        
        #This configures widgets
        #Ice Complex Banner
        banner = Image.open("banner.png")
        bannerPhoto = ImageTk.PhotoImage(banner)
        self.Label1 = Label(top, image=bannerPhoto)
        self.Label1.image = bannerPhoto
        self.Label1.place(relx=0.01, rely=0.02, height=60, width=300)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor=CENTER)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        #self.Label.configure(image = bannerPhoto)
        #self.Label.configure(text='''test''')
        self.Label1.configure(width=154)
        #-----------------------------

        
        self.Checkbutton1 = Checkbutton(top)
        self.Checkbutton1.place(relx=0.78, rely=0.3, relheight=0.04
                , relwidth=0.21)
        self.Checkbutton1.configure(activebackground="#d9d9d9")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(anchor=W)
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify=LEFT)
        self.Checkbutton1.configure(text='''Flood''')
        self.Checkbutton1.configure(variable=zamtest_support.flood)
        self.Checkbutton1.configure(width=171)
        self.Checkbutton1.deselect()

        self.Checkbutton2 = Checkbutton(top)
        self.Checkbutton2.place(relx=0.78, rely=0.26, relheight=0.04
                , relwidth=0.22)
        self.Checkbutton2.configure(activebackground="#d9d9d9")
        self.Checkbutton2.configure(activeforeground="#000000")
        self.Checkbutton2.configure(anchor=W)
        self.Checkbutton2.configure(background="#d9d9d9")
        self.Checkbutton2.configure(disabledforeground="#a3a3a3")
        self.Checkbutton2.configure(foreground="#000000")
        self.Checkbutton2.configure(highlightbackground="#d9d9d9")
        self.Checkbutton2.configure(highlightcolor="black")
        self.Checkbutton2.configure(justify=LEFT)
        self.Checkbutton2.configure(text='''Dry''')
        self.Checkbutton2.configure(variable=zamtest_support.dry)
        self.Checkbutton2.configure(width=181)
        self.Checkbutton2.deselect()

        self.Checkbutton3 = Checkbutton(top)
        self.Checkbutton3.place(relx=0.78, rely=0.42, relheight=0.04
                , relwidth=0.21)
        self.Checkbutton3.configure(activebackground="#d9d9d9")
        self.Checkbutton3.configure(activeforeground="#000000")
        self.Checkbutton3.configure(anchor=W)
        self.Checkbutton3.configure(background="#d9d9d9")
        self.Checkbutton3.configure(disabledforeground="#a3a3a3")
        self.Checkbutton3.configure(foreground="#000000")
        self.Checkbutton3.configure(highlightbackground="#d9d9d9")
        self.Checkbutton3.configure(highlightcolor="black")
        self.Checkbutton3.configure(justify=LEFT)
        self.Checkbutton3.configure(text='''Edge''')
        self.Checkbutton3.configure(variable=zamtest_support.edge)
        self.Checkbutton3.configure(width=176)
        #self.photo = PhotoImage(file="designer.png")
        #self.Checkbutton3.configure(image=self.photo)
        self.Checkbutton3.deselect()
    

        self.Checkbutton4 = Checkbutton(top)
        self.Checkbutton4.place(relx=0.78, rely=0.38, relheight=0.04
                , relwidth=0.21)
        self.Checkbutton4.configure(activebackground="#d9d9d9")
        self.Checkbutton4.configure(activeforeground="#000000")
        self.Checkbutton4.configure(anchor=W)
        self.Checkbutton4.configure(background="#d9d9d9")
        self.Checkbutton4.configure(disabledforeground="#a3a3a3")
        self.Checkbutton4.configure(foreground="#000000")
        self.Checkbutton4.configure(highlightbackground="#d9d9d9")
        self.Checkbutton4.configure(highlightcolor="black")
        self.Checkbutton4.configure(justify=LEFT)
        self.Checkbutton4.configure(text='''3-lap''')
        self.Checkbutton4.configure(variable=zamtest_support.threeLap)
        self.Checkbutton4.configure(width=171)
        self.Checkbutton4.deselect()

        self.Scrolledlistbox1 = ScrolledListBox(top)
        self.Scrolledlistbox1.place(relx=0.12, rely=0.68, relheight=0.3
                , relwidth=0.76)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(foreground="black")
        self.Scrolledlistbox1.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(selectforeground="black")
        self.Scrolledlistbox1.configure(width=10)
        self.Scrolledlistbox1.configure(listvariable=zamtest_support.Recent_Resurfaces)

        #---------------------------------
        #Board Brush
        self.Checkbutton9 = Checkbutton(top)
        self.Checkbutton9.place(relx=0.78, rely=0.18, relheight=0.04
                , relwidth=0.21)
        self.Checkbutton9.configure(activebackground="#d9d9d9")
        self.Checkbutton9.configure(activeforeground="#000000")
        self.Checkbutton9.configure(anchor=W)
        self.Checkbutton9.configure(background="#d9d9d9")
        self.Checkbutton9.configure(disabledforeground="#a3a3a3")
        self.Checkbutton9.configure(foreground="#000000")
        self.Checkbutton9.configure(highlightbackground="#d9d9d9")
        self.Checkbutton9.configure(highlightcolor="black")
        self.Checkbutton9.configure(justify=LEFT)
        self.Checkbutton9.configure(text='''Board Brush''')
        self.Checkbutton9.configure(variable=zamtest_support.boardBrush)
        self.Checkbutton9.configure(width=171)
        self.Checkbutton9.deselect()
        #---------------------------------

        
        self.Checkbutton5 = Checkbutton(top)
        self.Checkbutton5.place(relx=0.78, rely=0.22, relheight=0.04
                , relwidth=0.21)
        self.Checkbutton5.configure(activebackground="#d9d9d9")
        self.Checkbutton5.configure(activeforeground="#000000")
        self.Checkbutton5.configure(anchor=W)
        self.Checkbutton5.configure(background="#d9d9d9")
        self.Checkbutton5.configure(disabledforeground="#a3a3a3")
        self.Checkbutton5.configure(foreground="#000000")
        self.Checkbutton5.configure(highlightbackground="#d9d9d9")
        self.Checkbutton5.configure(highlightcolor="black")
        self.Checkbutton5.configure(justify=LEFT)
        self.Checkbutton5.configure(text='''Wet''')
        self.Checkbutton5.configure(variable=zamtest_support.wet)
        self.Checkbutton5.configure(width=171)
        self.Checkbutton5.deselect()

        self.Checkbutton6 = Checkbutton(top)
        self.Checkbutton6.place(relx=0.78, rely=0.34, relheight=0.04
                , relwidth=0.21)
        self.Checkbutton6.configure(activebackground="#d9d9d9")
        self.Checkbutton6.configure(activeforeground="#000000")
        self.Checkbutton6.configure(anchor=W)
        self.Checkbutton6.configure(background="#d9d9d9")
        self.Checkbutton6.configure(disabledforeground="#a3a3a3")
        self.Checkbutton6.configure(foreground="#000000")
        self.Checkbutton6.configure(highlightbackground="#d9d9d9")
        self.Checkbutton6.configure(highlightcolor="black")
        self.Checkbutton6.configure(justify=LEFT)
        self.Checkbutton6.configure(text='''Center Flood''')
        self.Checkbutton6.configure(variable=zamtest_support.centerFlood)
        self.Checkbutton6.configure(width=171)
        self.Checkbutton6.deselect()
        #test disable

        self.Label3 = Label(top)
        self.Label3.place(relx=0.0, rely=0.2, height=21, width=154)
        self.Label3.configure(anchor=E)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Dump Tank Level''')
        self.Label3.configure(width=154)

        self.Label4 = Label(top)
        self.Label4.place(relx=0.0, rely=0.26, height=21, width=154)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(anchor=E)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Temperature''')
        self.Label4.configure(width=154)

        self.Label5 = Label(top)
        self.Label5.place(relx=0.0, rely=0.32, height=21, width=154)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(anchor=E)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Temp / Humidity''')
        self.Label5.configure(width=154)

        self.Label6 = Label(top)
        self.Label6.place(relx=0.0, rely=0.38, height=21, width=154)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(anchor=E)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Comment''')
        self.Label6.configure(width=154)

        self.Label7 = Label(top)
        self.Label7.place(relx=0.0, rely=0.44, height=21, width=154)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(anchor=E)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Zam Driver Initials''')
        self.Label7.configure(width=154)

        self.Entry3 = Entry(top)
        self.Entry3.place(relx=0.21, rely=0.2, relheight=0.03, relwidth=0.2)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")
        self.Entry3.configure(width=164)

        self.Entry4 = Entry(top)
        self.Entry4.place(relx=0.21, rely=0.26, relheight=0.03, relwidth=0.2)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="#c4c4c4")
        self.Entry4.configure(selectforeground="black")
        self.Entry4.configure(width=164)

        self.Entry5 = Entry(top)
        self.Entry5.place(relx=0.21, rely=0.32, relheight=0.03, relwidth=0.2)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(highlightbackground="#d9d9d9")
        self.Entry5.configure(highlightcolor="black")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(selectbackground="#c4c4c4")
        self.Entry5.configure(selectforeground="black")
        self.Entry5.configure(width=164)

        self.Entry6 = Entry(top)
        self.Entry6.place(relx=0.21, rely=0.38, relheight=0.03, relwidth=0.2)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(highlightbackground="#d9d9d9")
        self.Entry6.configure(highlightcolor="black")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(selectbackground="#c4c4c4")
        self.Entry6.configure(selectforeground="black")
        self.Entry6.configure(width=164)

        self.Entry7 = Entry(top)
        self.Entry7.place(relx=0.21, rely=0.44, relheight=0.03, relwidth=0.2)
        self.Entry7.configure(background="white")
        self.Entry7.configure(disabledforeground="#a3a3a3")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(highlightbackground="#d9d9d9")
        self.Entry7.configure(highlightcolor="black")
        self.Entry7.configure(insertbackground="black")
        self.Entry7.configure(selectbackground="#c4c4c4")
        self.Entry7.configure(selectforeground="black")
        self.Entry7.configure(width=164)
        ##self.Entry7.configure(justify="right")

        self.Button1 = Button(top)
        self.Button1.place(relx=0.67, rely=0.56, height=34, width=157)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Submit''')
        self.Button1.configure(width=157)
        ##test global button command from support
##        self.Button1.configure(command=print(zamtest_support.che56.get()))
        self.Button1.configure(command=self.writeResurface)

#############################################

        self.Button2 = Button(top)
        self.Button2.place(relx=0.40, rely=0.56, height=34, width=157)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text="Export")
        self.Button2.configure(width=157)
## Call Export Function
        self.Button2.configure(command =lambda : self.getExportData(self.Scrolledlistbox1.get(0,END)))

#############################################
        
        self.Label8 = Label(top)
        self.Label8.place(relx=0.12, rely=0.64, height=21, width=174)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Recent Resurfaces''')
        self.Label8.configure(width=174)

        self.Checkbutton7 = Checkbutton(top)
        self.Checkbutton7.place(relx=0.1, rely=0.13, relheight=0.04
                , relwidth=0.07)
        self.Checkbutton7.configure(activebackground="#d9d9d9")
        self.Checkbutton7.configure(activeforeground="#000000")
        self.Checkbutton7.configure(background="#d9d9d9")
        self.Checkbutton7.configure(disabledforeground="#a3a3a3")
        self.Checkbutton7.configure(foreground="#000000")
        self.Checkbutton7.configure(highlightbackground="#d9d9d9")
        self.Checkbutton7.configure(highlightcolor="black")
        self.Checkbutton7.configure(justify=LEFT)
        self.Checkbutton7.configure(text='''Rink 1''')
        self.Checkbutton7.configure(variable=zamtest_support.rink1)
        self.Checkbutton7.deselect()

        self.Checkbutton8 = Checkbutton(top)
        self.Checkbutton8.place(relx=0.26, rely=0.13, relheight=0.04
                , relwidth=0.07)
        self.Checkbutton8.configure(activebackground="#d9d9d9")
        self.Checkbutton8.configure(activeforeground="#000000")
        self.Checkbutton8.configure(background="#d9d9d9")
        self.Checkbutton8.configure(disabledforeground="#a3a3a3")
        self.Checkbutton8.configure(foreground="#000000")
        self.Checkbutton8.configure(highlightbackground="#d9d9d9")
        #self.Checkbutton8.configure(highlightcolor="black")
        self.Checkbutton8.configure(justify=LEFT)
        #self.Checkbutton8.configure(state="n)
        self.Checkbutton8.configure(text='''Rink 2''')
        self.Checkbutton8.configure(variable=zamtest_support.rink2)
        self.Checkbutton8.deselect()


        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

    def parseResurface(self,txt):
        #----------------
        ## Description: Accepts string of resurface text and returns
        ## list of indvidual elements
        #----------------

        line =  txt.split(" | ")
       
        return (line)
    
    def exportXls(self, exp):
        workbook = xlsxwriter.Workbook("test.xlsx")
        worksheet = workbook.add_worksheet()

        row = 0
        col = 0

        for i in exp:
            for l in i:
                worksheet.write(row,col, l)
                col += 1
            col = 0
            row += 1
        workbook.close()

        
    def getExportData(self,arr):
        resurfaceText =  arr #self.Scrolledlistbox1.get(0,END)
        #shortResurface = resurfaceText.replace("|", "")
        #print(resurfaceText)
        #Add "Wash Water"
        heading = ["Date", "Time", "Rink", "Board Brush", "Wet Cut", "Dry Cut","Edged",
                   "Three Lap", "Flood","Center Flood" , "Dump Tank", "HoneyWells", "Room Temp/Humidity", "Initials", "Comment"]
        #blah = self.parseResurface(resurfaceText[0])
        #print(blah[0])

        #2d array for exporting
        #print(len(self.Scrolledlistbox1.get(0,END)))
        print(len(arr))
        exp = [[] for i in range(len(arr) + 1)]
               
        #iterator
        count = 1

##        #set heading for xls
##        for l in heading:
##            exp[0].append(l) 
##        print(exp[0])
        exp[0] = heading
        #loop through arr
            #set line = parse(i)
            #exp[count] = line
            #count += 1
        for c in arr:
            line = self.parseResurface(c)
            #print(exp[count])
            exp[count] = line
            print("exp of [" + str(count) +"] :" +  str(exp[count]))
            count += 1
        #export
        self.exportXls(exp)
       
    
    def writeTime(self):
        timm = time.localtime()
        date = str(timm[1]) + "/" + str(timm[2]) + "/" + str(timm[0])

        if timm[3] > 12:
            pmam = "PM"
            hour = timm[3] - 12
        else:
            pmam = "AM"
            hour = timm[3]

        timofday =  str(hour) + ":" +  str(timm[4])
        dateandtime = date + " | " + timofday 

        return(dateandtime + pmam + " | ")
   
    
    def writeResurface(self):
        #print(zamtest_support.centerFlood.get())
        #creat resurface text = date and time
        #writeTim()
        resurfaceText=self.writeTime()
        #get checks and entries ----------------------------------------
        
        #checks
        if int(zamtest_support.rink1.get()) == 1:
            resurfaceText = resurfaceText + "Rink1 | "
        elif int(zamtest_support.rink2.get()) == 1:
            resurfaceText = resurfaceText + "Rink2 | "
        if int(zamtest_support.boardBrush.get()) == 1:
            resurfaceText = resurfaceText + "Brush | "
        if int(zamtest_support.wet.get()) == 1:
            resurfaceText = resurfaceText + "Wet | 0 | 0 | 0 | "
            self.Checkbutton2.deselect()
        elif int(zamtest_support.dry.get()) == 1:
            resurfaceText = resurfaceText + "0 | Dry | "
            if int(zamtest_support.edge.get()) == 1:
                resurfaceText = resurfaceText + "Edged | "
            else:
                resurfaceText = resurfaceText + "0 | "
            if int(zamtest_support.threeLap.get()) == 1:
                resurfaceText = resurfaceText + "Three Lap | "
            else:
                resurfaceText = resurfaceText + "0 | "
        if int(zamtest_support.flood.get()) == 1:
            resurfaceText = resurfaceText + "Flood | "
        else:
            resurfaceText = resurfaceText + "0 | "
        if int(zamtest_support.centerFlood.get()) == 1:
            resurfaceText = resurfaceText + "Center Flood | "
        else:
            resurfaceText = resurfaceText + "0 | "
        
        
            
        #entries
        resurfaceText = resurfaceText + self.Entry3.get() + " | "
        resurfaceText = resurfaceText + self.Entry4.get() + " | "
        resurfaceText = resurfaceText + self.Entry5.get() + " | "
        resurfaceText = resurfaceText + self.Entry6.get() + " | "
        resurfaceText = resurfaceText + self.Entry7.get() + ""

        #set resurface text += " %checks and %entries"
        self.Scrolledlistbox1.insert(END, resurfaceText)
        
        self.Entry3.delete(0,END)
        self.Entry4.delete(0,END)
        self.Entry5.delete(0,END)
        self.Entry6.delete(0,END)
        self.Entry7.delete(0,END)
   
        self.Checkbutton1.deselect()
        self.Checkbutton2.deselect()
        self.Checkbutton3.deselect()
        self.Checkbutton4.deselect()
        self.Checkbutton5.deselect()
        self.Checkbutton6.deselect()
        self.Checkbutton7.deselect()
        self.Checkbutton8.deselect()
        self.Checkbutton9.deselect()



# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

if __name__ == '__main__':
    vp_start_gui()
    if zamtest_support.dry.get() == 1:
        print("1 Test")



