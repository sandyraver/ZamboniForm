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
        ##Ice Complex Banner
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

        #Flood Checkbutton
        self.Flood = Checkbutton(top)
        self.Flood.place(relx=0.78, rely=0.3, relheight=0.04
                , relwidth=0.21)
        self.Flood.configure(activebackground="#d9d9d9")
        self.Flood.configure(activeforeground="#000000")
        self.Flood.configure(anchor=W)
        self.Flood.configure(background="#d9d9d9")
        self.Flood.configure(disabledforeground="#a3a3a3")
        self.Flood.configure(foreground="#000000")
        self.Flood.configure(highlightbackground="#d9d9d9")
        self.Flood.configure(highlightcolor="black")
        self.Flood.configure(justify=LEFT)
        self.Flood.configure(text='''Flood''')
        self.Flood.configure(variable=zamtest_support.flood)
        self.Flood.configure(width=171)
        self.Flood.deselect()
        #---------------------------

        #Dry Checkbutton
        self.Dry = Checkbutton(top)
        self.Dry.place(relx=0.78, rely=0.38, relheight=0.04
                , relwidth=0.22)
        self.Dry.configure(activebackground="#d9d9d9")
        self.Dry.configure(activeforeground="#000000")
        self.Dry.configure(anchor=W)
        self.Dry.configure(background="#d9d9d9")
        self.Dry.configure(disabledforeground="#a3a3a3")
        self.Dry.configure(foreground="#000000")
        self.Dry.configure(highlightbackground="#d9d9d9")
        self.Dry.configure(highlightcolor="black")
        self.Dry.configure(justify=LEFT)
        self.Dry.configure(text='''Dry''')
        self.Dry.configure(variable=zamtest_support.dry)
        self.Dry.configure(width=181)
        self.Dry.deselect()
        #---------------------------

        #Edge Checkbutton
        self.Edge = Checkbutton(top)
        self.Edge.place(relx=0.78, rely=0.46, relheight=0.04
                , relwidth=0.21)
        self.Edge.configure(activebackground="#d9d9d9")
        self.Edge.configure(activeforeground="#000000")
        self.Edge.configure(anchor=W)
        self.Edge.configure(background="#d9d9d9")
        self.Edge.configure(disabledforeground="#a3a3a3")
        self.Edge.configure(foreground="#000000")
        self.Edge.configure(highlightbackground="#d9d9d9")
        self.Edge.configure(highlightcolor="black")
        self.Edge.configure(justify=LEFT)
        self.Edge.configure(text='''Edge''')
        self.Edge.configure(variable=zamtest_support.edge)
        self.Edge.configure(width=176)
        #self.photo = PhotoImage(file="designer.png")
        #self.Edge.configure(image=self.photo)
        self.Edge.deselect()
        #---------------------------

        #3 Lap Checkbutton
        self.ThreeLap = Checkbutton(top)
        self.ThreeLap.place(relx=0.78, rely=0.34, relheight=0.04
                , relwidth=0.21)
        self.ThreeLap.configure(activebackground="#d9d9d9")
        self.ThreeLap.configure(activeforeground="#000000")
        self.ThreeLap.configure(anchor=W)
        self.ThreeLap.configure(background="#d9d9d9")
        self.ThreeLap.configure(disabledforeground="#a3a3a3")
        self.ThreeLap.configure(foreground="#000000")
        self.ThreeLap.configure(highlightbackground="#d9d9d9")
        self.ThreeLap.configure(highlightcolor="black")
        self.ThreeLap.configure(justify=LEFT)
        self.ThreeLap.configure(text='''3-lap''')
        self.ThreeLap.configure(variable=zamtest_support.threeLap)
        self.ThreeLap.configure(width=171)
        self.ThreeLap.deselect()
        #---------------------------

        #Recent Resurfaces Checkbutton
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
        #---------------------------

        #Board Brush Checkbutton
        self.Brush = Checkbutton(top)
        self.Brush.place(relx=0.78, rely=0.18, relheight=0.04
                , relwidth=0.21)
        self.Brush.configure(activebackground="#d9d9d9")
        self.Brush.configure(activeforeground="#000000")
        self.Brush.configure(anchor=W)
        self.Brush.configure(background="#d9d9d9")
        self.Brush.configure(disabledforeground="#a3a3a3")
        self.Brush.configure(foreground="#000000")
        self.Brush.configure(highlightbackground="#d9d9d9")
        self.Brush.configure(highlightcolor="black")
        self.Brush.configure(justify=LEFT)
        self.Brush.configure(text='''Board Brush''')
        self.Brush.configure(variable=zamtest_support.boardBrush)
        self.Brush.configure(width=171)
        self.Brush.deselect()
        #---------------------------------

        #Wash water Checkbutton
        self.Flood0 = Checkbutton(top)
        self.Flood0.place(relx=0.78, rely=0.22, relheight=0.04
                , relwidth=0.21)
        self.Flood0.configure(activebackground="#d9d9d9")
        self.Flood0.configure(activeforeground="#000000")
        self.Flood0.configure(anchor=W)
        self.Flood0.configure(background="#d9d9d9")
        self.Flood0.configure(disabledforeground="#a3a3a3")
        self.Flood0.configure(foreground="#000000")
        self.Flood0.configure(highlightbackground="#d9d9d9")
        self.Flood0.configure(highlightcolor="black")
        self.Flood0.configure(justify=LEFT)
        self.Flood0.configure(text='''Wash Water''')
        self.Flood0.configure(variable=zamtest_support.wash)
        self.Flood0.configure(width=171)
        self.Flood0.deselect()
        #---------------------------------

        #Wet Checkbutton
        self.Wet = Checkbutton(top)
        self.Wet.place(relx=0.78, rely=0.26, relheight=0.04
                , relwidth=0.21)
        self.Wet.configure(activebackground="#d9d9d9")
        self.Wet.configure(activeforeground="#000000")
        self.Wet.configure(anchor=W)
        self.Wet.configure(background="#d9d9d9")
        self.Wet.configure(disabledforeground="#a3a3a3")
        self.Wet.configure(foreground="#000000")
        self.Wet.configure(highlightbackground="#d9d9d9")
        self.Wet.configure(highlightcolor="black")
        self.Wet.configure(justify=LEFT)
        self.Wet.configure(text='''Wet''')
        self.Wet.configure(variable=zamtest_support.wet)
        self.Wet.configure(width=171)
        self.Wet.deselect()
        #---------------------------

        #Center Flood Checkbutton
        self.CenterFlood = Checkbutton(top)
        self.CenterFlood.place(relx=0.78, rely=0.42, relheight=0.04
                , relwidth=0.21)
        self.CenterFlood.configure(activebackground="#d9d9d9")
        self.CenterFlood.configure(activeforeground="#000000")
        self.CenterFlood.configure(anchor=W)
        self.CenterFlood.configure(background="#d9d9d9")
        self.CenterFlood.configure(disabledforeground="#a3a3a3")
        self.CenterFlood.configure(foreground="#000000")
        self.CenterFlood.configure(highlightbackground="#d9d9d9")
        self.CenterFlood.configure(highlightcolor="black")
        self.CenterFlood.configure(justify=LEFT)
        self.CenterFlood.configure(text='''Center Flood''')
        self.CenterFlood.configure(variable=zamtest_support.centerFlood)
        self.CenterFlood.configure(width=171)
        self.CenterFlood.deselect()
        #---------------------------

        #Dump tank Label
        self.Label3 = Label(top)
        self.Label3.place(relx=0.0, rely=0.2, height=21, width=154)
        self.Label3.configure(anchor=E)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Dump Tank Level''')
        self.Label3.configure(width=154)
        #---------------------------

        #Temp Label
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
        #---------------------------

        #Temp/Humid Label
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
        #---------------------------

        #Comment Label
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
        #---------------------------

        #Initials Label
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
        #---------------------------

        #Dump Tank Entry
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
        #---------------------------

        #Temp Entry
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
        #---------------------------

        #Temp/Humid Entry
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
        #---------------------------

        #Comment Entry
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
        #---------------------------

        #Initials Entry
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
        #---------------------------

        #Submit Button
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
        self.Button1.configure(command=self.writeResurface)
        #---------------------------


        #Export Button
        self.ExportButton = Button(top)
        self.ExportButton.place(relx=0.40, rely=0.56, height=34, width=157)
        self.ExportButton.configure(activebackground="#d9d9d9")
        self.ExportButton.configure(activeforeground="#000000")
        self.ExportButton.configure(background="#d9d9d9")
        self.ExportButton.configure(disabledforeground="#a3a3a3")
        self.ExportButton.configure(foreground="#000000")
        self.ExportButton.configure(highlightbackground="#d9d9d9")
        self.ExportButton.configure(highlightcolor="black")
        self.ExportButton.configure(pady="0")
        self.ExportButton.configure(text="Export")
        self.ExportButton.configure(width=157)
        ## Call Export Function
        self.ExportButton.configure(command =lambda : self.getExportData(self.Scrolledlistbox1.get(0,END)))
        #---------------------------

        self.Label8 = Label(top)
        self.Label8.place(relx=0.12, rely=0.64, height=21, width=174)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Recent Resurfaces''')
        self.Label8.configure(width=174)

        self.Rink1 = Checkbutton(top)
        self.Rink1.place(relx=0.1, rely=0.13, relheight=0.04
                , relwidth=0.07)
        self.Rink1.configure(activebackground="#d9d9d9")
        self.Rink1.configure(activeforeground="#000000")
        self.Rink1.configure(background="#d9d9d9")
        self.Rink1.configure(disabledforeground="#a3a3a3")
        self.Rink1.configure(foreground="#000000")
        self.Rink1.configure(highlightbackground="#d9d9d9")
        self.Rink1.configure(highlightcolor="black")
        self.Rink1.configure(justify=LEFT)
        self.Rink1.configure(text='''Rink 1''')
        self.Rink1.configure(variable=zamtest_support.rink1)
        self.Rink1.deselect()


        ##
        self.Rink2 = Checkbutton(top)
        self.Rink2.place(relx=0.26, rely=0.13, relheight=0.04
                , relwidth=0.07)
        self.Rink2.configure(activebackground="#d9d9d9")
        self.Rink2.configure(activeforeground="#000000")
        self.Rink2.configure(background="#d9d9d9")
        self.Rink2.configure(disabledforeground="#a3a3a3")
        self.Rink2.configure(foreground="#000000")
        self.Rink2.configure(highlightbackground="#d9d9d9")
        #self.Rink2.configure(highlightcolor="black")
        self.Rink2.configure(justify=LEFT)
        #self.Rink2.configure(state="n)
        self.Rink2.configure(text='''Rink 2''')
        self.Rink2.configure(variable=zamtest_support.rink2)
        self.Rink2.deselect()


        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)


        # Get selected entry
    # if board/wet/wash/dry/center/3-lap/edge  are in string recheck respective boxes
    # parse it into individual elements for the text entries
    # reinsert text entries back into the input boxes in order


    # Get selected entry (entr)
    # if entr.find("Wash", 0)
    # then check washwater checkbox
    # if entr.find("Wet", 0)
    # then check wet checkbox
    # ...

    # Parse entry backwards ( If applicable)
    # Massive systemic problem ( how the fuck do you tell which is which lol)
    # Algorithm for determining what is what based on element lay out/order
    # element content can't help in determining no entry checking
    #

    # Half the number of slots can be cut down
    # 4 zeros even when every entry is checked
    # Write resurface could be adjusted to fix this
    # by making the if statements more complex
    # So What conflicts with what?
    # Board brush, wash water stand alone?
    # wet and dry, Center flood and dry?
    # Graphically outline what does what

    def parseResurface(self,txt):
        #----------------
        ## Description: Accepts string of resurface text and returns
        ## list of indvidual elements
        #----------------

        line =  txt.split(" | ")

        return (line)

    def exportXls(self, exp):
        #---------------------------
        ##Description: Accepts 2d list of all Recent Resurfaces
        ## and writes them to xls document based on position in list
        #---------------------------
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
        #---------------------------
        ##Description: Accepts list of strings from Recent resurfaces(scrolled listbox)
        ## adds formats adds heading and
        #---------------------------
        resurfaceText =  arr #self.Scrolledlistbox1.get(0,END)
        #shortResurface = resurfaceText.replace("|", "")
        #print(resurfaceText)
        #Add "Wash Water"
        heading = ["Date", "Time", "Rink", "Board Brush", "Wash Water", "Wet Cut", "Dry Cut","Edged",
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

 #this commen
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
        else:
            resurfaceText = resurfaceText + "0 | "
        if int(zamtest_support.boardBrush.get()) == 1:
            resurfaceText = resurfaceText + "Brush | "
        else:
            resurfaceText = resurfaceText + "0 | "
        if int(zamtest_support.wash.get()) == 1:
            resurfaceText = resurfaceText + "Wash | "
        else:
            resurfaceText = resurfaceText + "0 | "
        if int(zamtest_support.wet.get()) == 1:
            resurfaceText = resurfaceText + "Wet | 0 | 0 | 0 | "
            self.Dry.deselect()
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
        else:
            resurfaceText = resurfaceText + "0 | 0 | 0 | 0 | "
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
        resurfaceText = resurfaceText + self.Entry7.get() + " | "
        resurfaceText = resurfaceText + self.Entry6.get() + " | "


        #set resurface text += " %checks and %entries"
        self.Scrolledlistbox1.insert(END, resurfaceText)

        #clearing all the entries
        self.Entry3.delete(0,END)
        self.Entry4.delete(0,END)
        self.Entry5.delete(0,END)
        self.Entry6.delete(0,END)
        self.Entry7.delete(0,END)

       #deselecting all the buttons
        self.Flood.deselect()
        self.Dry.deselect()
        self.Edge.deselect()
        self.ThreeLap.deselect()
        self.Wet.deselect()
        self.CenterFlood.deselect()
        self.Rink1.deselect()
        self.Rink2.deselect()
        self.Brush.deselect()



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
