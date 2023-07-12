import tkinter as tk
import sqlite3
import time
from datetime import date

#CREATE GUI WINDOW
lmsGui = tk.Tk()
lmsGui.title("Library System Dashboard")
#SET GUI DIMENSIONS
lmsGui.geometry("900x500+250+100")

#GUI LIBRARY HEADER
def Header(lmsGui):
    fm = tk.Frame(lmsGui,height=500,width=900,bg='#fff')
    fm.place(x=0,y=0)
    fm2=tk.Frame(lmsGui,bg='#991423',height=80,width=900)
    fm2.place(x=0,y=0)
    lbb = tk.Label(lmsGui, bg='#991423')
    lbb.place(x=15, y=5)
    ig = tk.PhotoImage(file='library.png')
    lbb.config(image=ig)
    lb3 = tk.Label(lmsGui, text='LIBRARY MATERIAL DASHBOARD', fg='#fff', bg='#991423', font=('Arial', 30, 'bold'))
    lb3.place(x=125, y=17)
    return ig

#GUI DISPLAY CURRENT DATE
def Header2():
    dev = tk.Label(lmsGui,text="Developed by: De Omania | Del Rosario ", fg='black', bg='#fff',font=('Arial',10,'bold'))
    dev.place(x=40,y=83)
    today = date.today()
    dat = tk.Label(lmsGui,text='Date : ',bg='#fff',fg='black',font=('Arial', 10, 'bold'))
    dat.place(x=740,y=83)
    dat2 = tk.Label(lmsGui, text= today, bg='#fff', fg='black', font=('Arial', 10, 'bold'))
    dat2.place(x=790, y=83)

#DISPLAY CLOCK
def clock(lb1_hr, lb3_hr, lb5_hr, lb7_hr):
    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))

    if int(h) >=12 and int(m) >=0:
        lb7_hr.config(text="PM")
        if int(h) > 12:
            h = int(h) - 12
            h = str(h)
    lb1_hr.config(text=h)
    lb3_hr.config(text=m)
    lb5_hr.config(text=s)
    lb1_hr.after(200, lambda: clock(lb1_hr, lb3_hr, lb5_hr, lb7_hr))

def dispClock():
    #DISPLAY HOURS
    lb1_hr = tk.Label(lmsGui, text='00', font=('times new roman', 20, 'bold'), bg='#cf0404', fg='white')
    lb1_hr.place(x=100, y=370, width=60, height=30)
    #DISPLAY MINUTES
    lb3_hr = tk.Label(lmsGui, text='00', font=('times new roman', 20, 'bold'), bg='#27db0f', fg='white')
    lb3_hr.place(x=170, y=370, width=60, height=30)
    #DISPLAY SECONDS
    lb5_hr = tk.Label(lmsGui, text='00', font=('times new roman', 20, 'bold'), bg='#06afd1', fg='white')
    lb5_hr.place(x=240, y=370, width=60, height=30)
    #DISPLAY AM/PM
    lb7_hr = tk.Label(lmsGui, text='AM', font=('times new roman', 17, 'bold'), bg='#2b1dff', fg='white')
    lb7_hr.place(x=310, y=370, width=60, height=30)
    clock(lb1_hr, lb3_hr, lb5_hr, lb7_hr)

#DISPLAY LIB IMAGE
def homescreenImage(lmsGui):
    canvas = tk.Canvas(lmsGui, bg='black', width=400, height=300)
    canvas.place(x=455, y=150)
    photo= tk.PhotoImage(file='bb.png')
    canvas.create_image(0,0,image=photo,anchor= tk.NW)
    return photo

#FUNCTION TO INITIALIZE BUTTONS
def addLibMat(command):
    button = tk.Button(text='Add Material', fg='#fff', bg='#decb00', font=('Arial', 15, 'bold'), width = 15, command=command)
    button.place(x=40, y=150)
def remLibMat(command):
    button = tk.Button(text='Remove Material', fg='#fff', bg='#decb00', font=('Arial', 15, 'bold'), width = 15, command=command)
    button.place(x=240, y=150)
def dspLibMat(command):
    button = tk.Button(text='Display Material', fg='#fff', bg='#decb00', font=('Arial', 15, 'bold'), width = 15, command=command)
    button.place(x=40, y=220)
def borLibMat(command):
    button = tk.Button(text='Borrow Material', fg='#fff', bg='#decb00', font=('Arial', 15, 'bold'), width = 15, command=command)
    button.place(x=240, y=220)
def retLibMat(command):
    button = tk.Button(text='Return Material', fg='#fff', bg='#decb00', font=('Arial', 15, 'bold'), width = 15, command=command)
    button.place(x=40, y=290)
def logOut(command):
    button = tk.Button(text='Log Out', fg='#fff', bg='#decb00', font=('Arial', 15, 'bold'), width = 15, command=command)
    button.place(x=240, y=290)

#RE-DIRECT FRAME
def newFrame():
    addfm = tk.Frame(lmsGui,bg='#991423',width=900,height=390)
    addfm.place(x=0, y= 110)
    return addfm

#GO BACK TO HOMEPAGE
def goBack(homePage):
    go_back_button = tk.Button(homePage, text="Go Back", fg= '#fff', bg='#decb00', command=lambda: homePage.destroy())
    go_back_button.place(x=40, y=10)

#FUNCTION TO SET BUTTON COMMANDS
def add_books():
    addgui = newFrame()
    ad = tk.Label(addgui, text='Serial Number:', fg= '#fff', bg='#991423', font=('times new roman', 12))
    ad.place(x=130, y=50)
    data = tk.Entry(addgui, width= 70)
    data.place(x=290, y=50)
    ad1 = tk.Label(addgui, text='Title of Material:', fg= '#fff', bg='#991423', font=('times new roman', 12))
    ad1.place(x=130, y=100)
    data1 = tk.Entry(addgui, width= 70)
    data1.place(x=290, y=100)
    ad2 = tk.Label(addgui, text='Author:', fg= '#fff', bg='#991423', font=('times new roman', 12))
    ad2.place(x=130, y=150)
    data2 = tk.Entry(addgui, width= 70)
    data2.place(x=290, y=150)
    ad3 = tk.Label(addgui, text='Publisher:', fg= '#fff', bg='#991423', font=('times new roman', 12))
    ad3.place(x=130, y=200)
    data3 = tk.Entry(addgui, width= 70)
    data3.place(x=290, y=200)
    ad4 = tk.Label(addgui, text='Date Published:', fg= '#fff', bg='#991423', font=('times new roman', 12))
    ad4.place(x=130, y=250)
    data3 = tk.Entry(addgui, width= 70)
    data3.place(x=290, y=250)
    addData = tk.Button(addgui, text= 'Add Material', fg= '#fff', bg='#decb00', font=('Arial', 10, 'bold'), width= 52)
    addData.place(x=290, y=300)
    goBack(addgui)

def remove_books():
    addgui = newFrame()
    goBack(addgui)
    print("Remove Books button clicked")
def disp_books():
    addgui = newFrame()
    goBack(addgui)
    print("Display Books button clicked")
def borrow_books():
    addgui = newFrame()
    goBack(addgui)
    print("Borrow Books button clicked")
def return_books():
    addgui = newFrame()
    goBack(addgui)
    print("Return Books button clicked")
def log_out():
    print("logout button clicked")

#MAIN 
Banner = Header(lmsGui)
DateDev = Header2()
hsi = homescreenImage(lmsGui)
bt1 = addLibMat(add_books)
bt2 = remLibMat(remove_books)
bt3 = dspLibMat(disp_books)
bt4 = borLibMat(borrow_books)
bt5 = retLibMat(return_books)
bt6 = logOut(log_out)
whatTime = dispClock()

#MAKE GUI VISIBLE
lmsGui.resizable(False, False)
lmsGui.mainloop()
