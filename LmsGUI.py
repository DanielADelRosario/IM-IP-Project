# di pa narestrict yung accepting symbols, numbers or characters tsaka yung disabled button

import tkinter as tk
from tkinter import ttk
import sqlite3
import datetime
import time
from datetime import date, timedelta
import tkinter.messagebox as messagebox
import tkinter as tk
from tkcalendar import DateEntry

conn = sqlite3.connect('system.db')

# CREATE GUI WINDOW
lmsGui = tk.Tk()
lmsGui.title("Library System Dashboard")
# SET GUI DIMENSIONS
lmsGui.geometry("900x550+250+100")


# GUI LIBRARY HEADER
def Header(lmsGui):
    fm = tk.Frame(lmsGui, height=550, width=900, bg='#fff')
    fm.place(x=0, y=0)
    fm2 = tk.Frame(lmsGui, bg='#00008B', height=80, width=900)
    fm2.place(x=0, y=0)
    lbb = tk.Label(lmsGui, bg='#00008B')
    lbb.place(x=15, y=5)
    ig = tk.PhotoImage(file='library.png')
    lbb.config(image=ig)
    lb3 = tk.Label(lmsGui, text='LIBRARY MATERIAL DASHBOARD', fg='#fff', bg='#00008B', font=('Arial', 30, 'bold'))
    lb3.place(x=125, y=17)
    return ig


# GUI DISPLAY CURRENT DATE
def Header2():
    dev = tk.Label(lmsGui, text="Developed by: De Omania | Del Rosario ", fg='black', bg='#fff',
                   font=('Arial', 10, 'bold'))
    dev.place(x=40, y=83)
    today = date.today()
    dat = tk.Label(lmsGui, text='Date : ', bg='#fff', fg='black', font=('Arial', 10, 'bold'))
    dat.place(x=740, y=83)
    dat2 = tk.Label(lmsGui, text=today, bg='#fff', fg='black', font=('Arial', 10, 'bold'))
    dat2.place(x=790, y=83)


# DISPLAY CLOCK
def clock(lb1_hr, lb3_hr, lb5_hr, lb7_hr):
    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))

    if int(h) >= 12 and int(m) >= 0:
        lb7_hr.config(text="PM")
        if int(h) > 12:
            h = int(h) - 12
            h = str(h)
    lb1_hr.config(text=h)
    lb3_hr.config(text=m)
    lb5_hr.config(text=s)
    lb1_hr.after(200, lambda: clock(lb1_hr, lb3_hr, lb5_hr, lb7_hr))


def dispClock():
    # DISPLAY HOURS
    lb1_hr = tk.Label(lmsGui, text='00', font=('times new roman', 20, 'bold'), bg='#cf0404', fg='white')
    lb1_hr.place(x=100, y=400, width=60, height=30)
    # DISPLAY MINUTES
    lb3_hr = tk.Label(lmsGui, text='00', font=('times new roman', 20, 'bold'), bg='#27db0f', fg='white')
    lb3_hr.place(x=170, y=400, width=60, height=30)
    # DISPLAY SECONDS
    lb5_hr = tk.Label(lmsGui, text='00', font=('times new roman', 20, 'bold'), bg='#06afd1', fg='white')
    lb5_hr.place(x=240, y=400, width=60, height=30)
    # DISPLAY AM/PM
    lb7_hr = tk.Label(lmsGui, text='AM', font=('times new roman', 17, 'bold'), bg='#2b1dff', fg='white')
    lb7_hr.place(x=310, y=400, width=60, height=30)
    clock(lb1_hr, lb3_hr, lb5_hr, lb7_hr)


# DISPLAY LIB IMAGE
def homescreenImage(lmsGui):
    canvas = tk.Canvas(lmsGui, bg='black', width=400, height=300)
    canvas.place(x=455, y=150)
    photo = tk.PhotoImage(file='bb.png')
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)
    return photo


# FUNCTION TO INITIALIZE BUTTONS
def addLibMat(command):
    button = tk.Button(text='Add Material', fg='#fff', bg='#006400', font=('Arial', 15, 'bold'), width=15,
                       command=command)
    button.place(x=40, y=180)


def remLibMat(command):
    button = tk.Button(text='Remove Material', fg='#fff', bg='#006400', font=('Arial', 15, 'bold'), width=15,
                       command=command)
    button.place(x=240, y=180)


def dspLibMat(command):
    button = tk.Button(text='Display Material', fg='#fff', bg='#006400', font=('Arial', 15, 'bold'), width=15,
                       command=command)
    button.place(x=40, y=235)


def borLibMat(command):
    button = tk.Button(text='Borrow Material', fg='#fff', bg='#006400', font=('Arial', 15, 'bold'), width=15,
                       command=command)
    button.place(x=240, y=235)


def retLibMat(command):
    button = tk.Button(text='Return Material', fg='#fff', bg='#006400', font=('Arial', 15, 'bold'), width=15,
                       command=command)
    button.place(x=40, y=290)


def dspMember(command):
    button = tk.Button(text='List of Members', fg='#fff', bg='#006400', font=('Arial', 15, 'bold'), width=15,
                       command=command)
    button.place(x=240, y=290)


def dspLoan(command):
    button = tk.Button(text='Circulation Log', fg='#fff', bg='#006400', font=('Arial', 15, 'bold'), width=15,
                       command=command)
    button.place(x=40, y=345)


def fineDetail(command):
    button = tk.Button(text='Late Fees', fg='#fff', bg='#006400', font=('Arial', 15, 'bold'), width=15,
                       command=command)
    button.place(x=240, y=345)


# def logOut(command):
#     button = tk.Button(text='Log Out', fg='#fff', bg='#006400', font=('Arial', 15, 'bold'), width=15, command=command)
#     button.place(x=40, y=320)

# RE-DIRECT FRAME
def newFrame():
    addfm = tk.Frame(lmsGui, bg='#00008B', width=900, height=590)
    addfm.place(x=0, y=110)
    return addfm


# GO BACK TO HOMEPAGE
def goBack(homePage):
    go_back_button = tk.Button(homePage, text="Go Back", fg='#fff', bg='#FF0000', command=lambda: homePage.destroy())
    go_back_button.place(x=40, y=10)


# Create the ITEM table if it doesn't exist
# conn.execute('''
#    CREATE TABLE IF NOT EXISTS ITEM (
#       Standard_No NVARCHAR(100) PRIMARY KEY NOT NULL,
#       Publisher NVARCHAR(100) NOT NULL,
#       Publish_Date DATE NOT NULL,
#       Author NVARCHAR(100) NOT NULL,
#       Title NVARCHAR(100) NOT NULL,
#       Item_Type NVARCHAR(10) NOT NULL,
#       Status TEXT DEFAULT 'Available'
#   )
# ''')

# FUNCTION TO SET BUTTON COMMANDS
def add_books():
    addgui = newFrame()
    goBack(addgui)
    ad = tk.Label(addgui, text='Standard Number:', fg='#fff', bg='#00008B', font=('times new roman', 12))
    ad.place(x=130, y=50)
    data = tk.Entry(addgui, width=70, bg='white')
    data.place(x=290, y=50)
    ad1 = tk.Label(addgui, text='Publisher:', fg='#fff', bg='#00008B', font=('times new roman', 12))
    ad1.place(x=130, y=100)
    data1 = tk.Entry(addgui, width=70, bg='white')
    data1.place(x=290, y=100)
    ad2 = tk.Label(addgui, text='Publish Date:', fg='#fff', bg='#00008B', font=('times new roman', 12))
    ad2.place(x=130, y=150)
    data2 = DateEntry(addgui, width=12, background='green', foreground='white', borderwidth=2)
    data2.place(x=290, y=150)
    ad3 = tk.Label(addgui, text='Author:', fg='#fff', bg='#00008B', font=('times new roman', 12))
    ad3.place(x=130, y=200)
    data3 = tk.Entry(addgui, width=70, bg='white')
    data3.place(x=290, y=200)
    ad4 = tk.Label(addgui, text='Title:', fg='#fff', bg='#00008B', font=('times new roman', 12))
    ad4.place(x=130, y=250)
    data4 = tk.Entry(addgui, width=70, bg='white')
    data4.place(x=290, y=250)
    ad5 = tk.Label(addgui, text='Item Type:', fg='#fff', bg='#00008B', font=('times new roman', 12))
    ad5.place(x=130, y=300)
    data5 = ttk.Combobox(addgui, values=["Book", "Journal"], width=67, state="readonly")
    data5.place(x=290, y=300)

    def add_data_to_db():
        standard_no = data.get()
        publisher = data1.get()
        publish_date = data2.get()
        author = data3.get()
        title = data4.get()
        item_type = data5.get()
        status = 'Available'

        # Check if any of the required fields are empty
        if not (standard_no and publisher and publish_date and author and title and item_type):
            messagebox.showerror("Error", "Please fill in all the required fields.")
            return

        # Execute SQL query to insert the data into the ITEM table
        conn.execute(
            "INSERT INTO ITEM (Standard_No, Publisher, Publish_Date, Author, Title, Item_Type, Status) VALUES (?, ?, ?, ?, ?, "
            "?, ?)",
            (standard_no, publisher, publish_date, author, title, item_type, status))
        conn.commit()

        # Clear the entry fields after adding the data
        data.delete(0, tk.END)
        data1.delete(0, tk.END)
        data2.delete(0, tk.END)
        data3.delete(0, tk.END)
        data4.delete(0, tk.END)
        data5.set("")

    addData = tk.Button(addgui, text='Add Material', fg='#fff', bg='#008000', font=('Arial', 10, 'bold'), width=52,
                        command=add_data_to_db)
    addData.place(x=290, y=350)


# FUNCTION FOR EVERY TREEVIEW INTERFACE (LIST OF MATERIALS)
def treeView(addgui):
    # Create a Treeview widget
    tree = ttk.Treeview(addgui)
    tree.place(x=20, y=45, width=840, height=340)

    # Define columns
    tree["columns"] = ("Standard_No", "Publisher", "Publish_Date", "Author", "Title", "Item_Type", "Status")

    # Format columns
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("Standard_No", width=120, anchor=tk.CENTER)
    tree.column("Publisher", width=120, anchor=tk.CENTER)
    tree.column("Publish_Date", width=120, anchor=tk.CENTER)
    tree.column("Author", width=120, anchor=tk.CENTER)
    tree.column("Title", width=120, anchor=tk.W)
    tree.column("Item_Type", width=120, anchor=tk.CENTER)
    tree.column("Status", width=118, anchor=tk.CENTER)

    # Create headings
    tree.heading("#0", text="", anchor=tk.CENTER)
    tree.heading("Standard_No", text="Standard No", anchor=tk.CENTER)
    tree.heading("Publisher", text="Publisher", anchor=tk.CENTER)
    tree.heading("Publish_Date", text="Publish Date", anchor=tk.CENTER)
    tree.heading("Author", text="Author", anchor=tk.CENTER)
    tree.heading("Title", text="Title", anchor=tk.CENTER)
    tree.heading("Item_Type", text="Item Type", anchor=tk.CENTER)
    tree.heading("Status", text="Status", anchor=tk.CENTER)

    # Retrieve data from the ITEM table
    cursor = conn.execute("SELECT * FROM ITEM")

    # Display data in the table
    for row in cursor:
        tree.insert("", tk.END, values=row)

    # Scrollbar
    scrollbar = ttk.Scrollbar(addgui, orient="vertical", command=tree.yview)
    scrollbar.place(x=860, y=45, height=340)
    tree.configure(yscrollcommand=scrollbar.set)
    return tree


def viewmembers(addgui):
    # Create a Treeview widget
    tree = ttk.Treeview(addgui)
    tree.place(x=20, y=45, width=840, height=340)

    # Define columns
    tree["columns"] = ("Member_ID", "Address", "Contact_No", "Name", "Member_Type")
    # Format columns
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("Member_ID", width=120, anchor=tk.CENTER)
    tree.column("Address", width=120, anchor=tk.CENTER)
    tree.column("Contact_No", width=120, anchor=tk.CENTER)
    tree.column("Name", width=120, anchor=tk.W)
    tree.column("Member_Type", width=120, anchor=tk.CENTER)

    # Create headings
    tree.heading("#0", text="", anchor=tk.CENTER)
    tree.heading("Member_ID", text="Member ID", anchor=tk.CENTER)
    tree.heading("Address", text="Address", anchor=tk.CENTER)
    tree.heading("Contact_No", text="Contact No.", anchor=tk.CENTER)
    tree.heading("Name", text="Name", anchor=tk.CENTER)
    tree.heading("Member_Type", text="Member Type", anchor=tk.CENTER)

    # Retrieve data from the MEMBER table
    cursor = conn.execute("SELECT * FROM MEMBER")

    # Display data in the table
    for row in cursor:
        tree.insert("", tk.END, values=row)

    # Scrollbar
    scrollbar = ttk.Scrollbar(addgui, orient="vertical", command=tree.yview)
    scrollbar.place(x=860, y=45, height=340)
    tree.configure(yscrollcommand=scrollbar.set)

    return tree


def viewlogs(addgui):
    # Create a Treeview widget
    tree = ttk.Treeview(addgui)
    tree.place(x=20, y=45, width=840, height=340)

    # Define columns
    tree["columns"] = ("Loan_ID", "Standard_No", "Member_ID", "Loan_Date", "Due_Date", "Return_Date")
    # Format columns
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("Loan_ID", width=120, anchor=tk.CENTER)
    tree.column("Standard_No", width=120, anchor=tk.CENTER)
    tree.column("Member_ID", width=120, anchor=tk.CENTER)
    tree.column("Loan_Date", width=120, anchor=tk.W)
    tree.column("Due_Date", width=120, anchor=tk.CENTER)
    tree.column("Return_Date", width=120, anchor=tk.CENTER)

    # Create headings
    tree.heading("#0", text="", anchor=tk.CENTER)
    tree.heading("Loan_ID", text="Loan ID", anchor=tk.CENTER)
    tree.heading("Standard_No", text="Standard No.", anchor=tk.CENTER)
    tree.heading("Member_ID", text="Member ID.", anchor=tk.CENTER)
    tree.heading("Loan_Date", text="Date Loaned", anchor=tk.CENTER)
    tree.heading("Due_Date", text="Due Date", anchor=tk.CENTER)
    tree.heading("Return_Date", text="Date Returned", anchor=tk.CENTER)

    # Scrollbar
    scrollbar = ttk.Scrollbar(addgui, orient="vertical", command=tree.yview)
    scrollbar.place(x=860, y=45, height=340)
    tree.configure(yscrollcommand=scrollbar.set)
    return tree


def remove_books():
    addgui = newFrame()
    goBack(addgui)

    def remove_selected_materials(tree):
        selected_items = tree.selection()
        for item in selected_items:
            values = tree.item(item)['values']
            standard_no = values[0]  # Standard_No of the selected material
            check_stat = values[-1]
            
            if check_stat == 'Borrowed':
                messagebox.showerror("Error", "Cannot Remove Borrowed Item.")
                return
            
            # Remove the material from the ITEM table
            conn.execute("DELETE FROM ITEM WHERE Standard_No = ?", (standard_no,))
            conn.commit()

            # USABLE FOR Message Dialog
            print("Material with Standard No", standard_no, "has been successfully removed")

            # Delete the material from the Treeview
            tree.delete(item)

    tree_view = treeView(addgui)

    remove_material = lambda: remove_selected_materials(tree_view)

    # Remove button
    remove_button = tk.Button(addgui, text="Remove", fg='#fff', bg='#8B0000', font=('Arial', 10, 'bold'), width=10,
                              command=remove_material)
    remove_button.place(x=430, y=391)


def disp_books():
    addgui = newFrame()
    goBack(addgui)

    itemtree = treeView(addgui)

    def edit_item():
        selected_item = itemtree.selection()
        if selected_item:
            # DISABLE EDIT BUTTON
            edit_button.config(state=tk.DISABLED)

            values = itemtree.item(selected_item)['values']
            Item_ID = values[0]

            input_win = tk.Toplevel(lmsGui)
            input_win.title("Edit an Item")
            input_win.configure(bg="#00008B")
            input_win.geometry("400x400+480+200")
            input_win.resizable(False, False)

            # Publisher
            lbl_pub = tk.Label(input_win, text="Publisher:", bg='#00008B', fg='#fff')
            entry_pub = tk.Entry(input_win, width=50)
            entry_pub.insert(0, values[1])  # Populate with existing value
            lbl_pub.grid(row=1, column=0, padx=50, pady=3)
            entry_pub.grid(row=2, column=0, padx=50, pady=3)

            # date
            lbl_pdat = tk.Label(input_win, text="Publish Date:", bg='#00008B', fg='#fff')
            entry_pdat = DateEntry(input_win, width=12, background='green', foreground='white', borderwidth=2)
            entry_pdat.insert(0, values[2])  # Populate with existing value
            lbl_pdat.grid(row=3, column=0, pady=3)
            entry_pdat.grid(row=4, column=0, pady=3)

            # Author
            lbl_au = tk.Label(input_win, text="Author:", bg='#00008B', fg='#fff')
            entry_au = tk.Entry(input_win, width=50)
            entry_au.insert(0, values[3])  # Populate with existing value
            lbl_au.grid(row=5, column=0, pady=3)
            entry_au.grid(row=6, column=0, pady=3)

            # Title
            lbl_t = tk.Label(input_win, text="Title:", bg='#00008B', fg='#fff')
            entry_t = tk.Entry(input_win, width=50)
            entry_t.insert(0, values[4])  # Populate with existing value
            lbl_t.grid(row=7, column=0, pady=3)
            entry_t.grid(row=8, column=0, pady=3)

            # Type
            lbl_typ = tk.Label(input_win, text="Type", bg='#00008B', fg='#fff')
            entry_typ = ttk.Combobox(input_win, values=["Book", "Journal"], width=47, state="readonly")
            entry_typ.set(values[5])  # Set the combobox to the existing value
            lbl_typ.grid(row=9, column=0, pady=3)
            entry_typ.grid(row=10, column=0, pady=3)

            # FUNCTION TO UPDATE AND REFRESH TREEVIEW
            def clear_treeview(tree):
                for item in tree.get_children():
                    tree.delete(item)

            # FUNCTION TO COMMMIT CHANGES
            def new_info():
                publisher = entry_pub.get()
                publish_date = entry_pdat.get()
                author = entry_au.get()
                title = entry_t.get()
                item_type = entry_typ.get()

                if not (publisher and publish_date and author and title and item_type):
                    messagebox.showerror("Error", "Please fill in all the required fields.")
                    input_win.focus()
                    return

                conn.execute("UPDATE ITEM SET Publisher=?, Publish_Date=?, "
                             "Author=?, Title=?, Item_Type=? WHERE Standard_No=?", (publisher,
                                                                                    publish_date, author, title,
                                                                                    item_type, Item_ID))
                conn.commit()

                input_win.destroy()

                # REFRESH TREEVIEW
                clear_treeview(itemtree)
                cursor = conn.execute("SELECT * FROM ITEM")
                for row in cursor:
                    itemtree.insert("", tk.END, values=row)

                # REENABLE EDIT UPON EXIT
                edit_button.config(state=tk.NORMAL)

            # REENABLE EDIT UPON CANCEL
            def on_window_close():
                edit_button.config(state=tk.NORMAL)  # Enable the "Edit" button when the window is closed
                input_win.destroy()

            input_win.protocol("WM_DELETE_WINDOW", on_window_close)

            # SAVE BUTTON
            save_button = tk.Button(input_win, text="Save", fg='#fff', bg='#8B0000', font=('Arial', 10, 'bold'),
                                    width=10,
                                    command=lambda: new_info())
            save_button.grid(row=11, columnspan=2, padx=10, pady=10)

    # EDIT BUTTON
    edit_button = tk.Button(addgui, text="Edit", fg='#fff', bg='#28a7c7', font=('Arial', 10, 'bold'), width=10,
                            command=edit_item)
    edit_button.place(x=390, y=391)


def borrow_input_window(treeview, borrow_button):
    borrow_button['state'] = tk.DISABLED
    input_win = tk.Toplevel(lmsGui)
    input_win.title("Select Member")
    input_win.configure(bg="#fff")
    input_win.resizable(False, False)
    bnnr = tk.Frame(input_win, bg='#00008B', height=50, width=900)
    bnnr.place(x=0, y=0)
    input_win.geometry("700x350+350+200")
    heading = tk.Label(input_win, text='Member Selection', fg='#fff', bg='#00008B', font=('Arial', 10, 'bold'))
    heading.place(x=25, y=17)
    membertree = ttk.Treeview(input_win)
    membertree.place(x=20, y=65, width=640, height=140)

    # Define columns
    membertree["columns"] = ("Member_ID", "Name", "Member_Type")
    # Format columns
    membertree.column("#0", width=0, stretch=tk.NO)
    membertree.column("Member_ID", width=80, anchor=tk.CENTER)
    membertree.column("Name", width=80, anchor=tk.CENTER)
    membertree.column("Member_Type", width=80, anchor=tk.CENTER)

    # Create headings
    membertree.heading("#0", text="", anchor=tk.CENTER)
    membertree.heading("Member_ID", text="Member ID", anchor=tk.CENTER)
    membertree.heading("Name", text="Name", anchor=tk.CENTER)
    membertree.heading("Member_Type", text="Member Type", anchor=tk.CENTER)

    # Retrieve data from the MEMBER table
    cursor = conn.execute("SELECT Member_ID, Name, Member_Type FROM MEMBER")

    # Display data in the table
    for row in cursor:
        membertree.insert("", tk.END, values=row)

    # Scrollbar
    scrollbar = ttk.Scrollbar(input_win, orient="vertical", command=membertree.yview)
    scrollbar.place(x=650, y=65, height=140)
    membertree.configure(yscrollcommand=scrollbar.set)

    # Function to perform the borrowing process
    def confirm_borrow():

        # Update the "Status" of the material to "Borrowed" in the ITEM table
        select_ID = treeview.selection()
        selected_items = membertree.selection()

        if selected_items:
            # Get the selected item values
            selected_item = treeview.item(select_ID[0])['values']
            selected_standard_no = selected_item[0]  # Assuming Standard_no is the first column
            status = selected_item[-1]  # Get Status of Item

            if status == 'Borrowed':
                messagebox.showerror("Error", "Item currently unavailable.")
                input_win.destroy()
                return

            else:
                # Get the Member_ID from the selected row and insert it into the LOAN table
                getmemID = membertree.item(selected_items[0])["values"]
                member_id = getmemID[0]  # Assuming Member_ID is in the first

                member_id_to_check = member_id
                check_member_query = conn.execute(
                    "SELECT Member_ID FROM LOAN WHERE Member_ID = ? AND Return_Date IS NULL", (member_id_to_check,))
                existing_loan = check_member_query.fetchone()
                if existing_loan:
                    messagebox.showerror("Error", "Member can only borrow one book.")
                    input_win.destroy()
                    return

                else:
                    # Update the "Status" of the material to "Borrowed" in the ITEM table
                    conn.execute("UPDATE ITEM SET Status = ? WHERE Standard_No = ?", ('Borrowed', selected_standard_no))
                    conn.commit()

                    # Set Date today and Due date
                    current_date = date.today()
                    due_date = current_date + timedelta(days=1)

                    conn.execute("INSERT INTO LOAN (Standard_no, Member_ID, Loan_Date, Due_Date) VALUES (?, ?, ?, ?)",
                                 (selected_standard_no, member_id, current_date, due_date))
                    conn.commit()
                    borrow_button['state'] = tk.NORMAL
        
        input_win.destroy()
        treeview.set(select_ID, "Status", "Borrowed")

    # REENABLE EDIT UPON CANCEL
    def on_window_close():
        borrow_button.config(state=tk.NORMAL)  # Enable the "Edit" button when the window is closed
        input_win.destroy()

    input_win.protocol("WM_DELETE_WINDOW", on_window_close)

    # Confirm Borrow button
    btn_confirm_borrow = tk.Button(input_win, text="Confirm borrow", fg='#fff', bg='#8B0000',
                                   font=('Arial', 10, 'bold'), width=15, command=confirm_borrow)

    btn_confirm_borrow['state'] = tk.DISABLED
    btn_confirm_borrow.place(x=270, y=300)

    def selectmember(event):
        selected_member = membertree.selection()
        if selected_member:
            # If a row is selected, enable the "Borrow" button
            btn_confirm_borrow['state'] = tk.NORMAL

    # Bind the select event of the Treeview to the on_treeview_select function
    membertree.bind("<<TreeviewSelect>>", selectmember)


def borrow_book():
    addgui = newFrame()
    goBack(addgui)

    treeview = treeView(addgui)
    borrowmaterial = lambda: borrow_input_window(treeview, borrow_button)

    # Borrow button
    borrow_button = tk.Button(addgui, text="Borrow", fg='#fff', bg='#8B0000', font=('Arial', 10, 'bold'), width=10,
                              command=borrowmaterial)
    # Disable button
    borrow_button['state'] = tk.DISABLED
    borrow_button.place(x=410, y=391)

    def selectrow(event):
        selected_items = treeview.selection()
        if selected_items:
            # If a row is selected, enable the "Borrow" button
            borrow_button['state'] = tk.NORMAL

    # Bind the select event of the Treeview to the on_treeview_select function
    treeview.bind("<<TreeviewSelect>>", selectrow)


def return_books():
    addgui = newFrame()
    goBack(addgui)

    tree = viewlogs(addgui)

    # Retrieve data from the LOAN table where Return_Date is null
    cursor = conn.execute("SELECT * FROM LOAN WHERE Return_Date IS NULL")

    # Display data in the table
    for row in cursor:
        tree.insert("", tk.END, values=row)

    def return_material():
        selected_items = tree.selection()
        for item in selected_items:
            values = tree.item(item)['values']
            Loan_ID = values[0]  # Assuming Loan_ID is the first column

            # Get the current date as the return date
            return_date = date.today()

            # Update the "Return_Date" in the LOAN table with the current date
            conn.execute("UPDATE LOAN SET Return_Date = ? WHERE Loan_ID = ?", (return_date, Loan_ID))
            conn.commit()

            print("Book with Loan ID", Loan_ID, "has been successfully returned")

            # Update the "Status" of the material to "Available" in the ITEM table
            standard_no = values[1]  # Assuming Standard_No is the second column
            conn.execute("UPDATE ITEM SET Status = ? WHERE Standard_No = ?", ('Available', standard_no))
            conn.commit()

            # Refresh the view to show the updated data (optional)
            tree.delete(item)

    # Return button
    return_button = tk.Button(addgui, text="Return", fg='#fff', bg='#8B0000', font=('Arial', 10, 'bold'), width=10,
                              command=return_material)
    return_button.place(x=390, y=391)

def editmember(tree_view, edit_button, add_button, remove_button, student_button, faculty_button):
    selected_item = tree_view.selection()
    if selected_item:

        edit_button.config(state=tk.DISABLED)
        add_button.config(state=tk.DISABLED)
        remove_button.config(state=tk.DISABLED)
        student_button.config(state=tk.DISABLED)
        faculty_button.config(state=tk.DISABLED)

        values = tree_view.item(selected_item)['values']
        Item_ID = values[0]
        input_win = tk.Toplevel(lmsGui)
        input_win.title("Add a Member")
        input_win.configure(bg="#00008B")
        input_win.geometry("400x400+480+200")
        input_win.resizable(False, False)

        # Address
        lbl_address = tk.Label(input_win, text="Address:", bg='#00008B', fg='#fff')
        entry_address = tk.Entry(input_win, width=50)
        entry_address.insert(0, values[1])  # Populate with existing value
        lbl_address.grid(row=1, column=0, padx=50, pady=3)
        entry_address.grid(row=2, column=0, padx=50, pady=3)

        # Contact No
        lbl_contact_no = tk.Label(input_win, text="Contact No:", bg='#00008B', fg='#fff')
        entry_contact_no = tk.Entry(input_win, width=50)
        entry_contact_no.insert(0, values[2])  # Populate with existing value
        lbl_contact_no.grid(row=3, column=0, padx=50, pady=3)
        entry_contact_no.grid(row=4, column=0, padx=50, pady=3)

        # Name
        lbl_name = tk.Label(input_win, text="Name:", bg='#00008B', fg='#fff')
        entry_name = tk.Entry(input_win, width=50)
        entry_name.insert(0, values[3])  # Populate with existing value
        lbl_name.grid(row=5, column=0, padx=50, pady=3)
        entry_name.grid(row=6, column=0, padx=50, pady=3)

        def select_member_type(event):
            member_type = member_type_combobox.get()
            if member_type == "Student":
                show_student_info(input_win)
            elif member_type == "Faculty":
                show_faculty_info(input_win)

        # Member Type
        member_type_label = tk.Label(input_win, text="Member Type:", bg='#00008B', fg='#fff')
        member_type_combobox = ttk.Combobox(input_win, values=["Student", "Faculty"], width=47, state="readonly")
        member_type_combobox.bind("<<ComboboxSelected>>", select_member_type)
        member_type_combobox.set(values[4])  # Populate with existing value
        member_type_label.grid(row=7, column=0, padx=50, pady=3)
        member_type_combobox.grid(row=8, column=0, padx=50, pady=3)

        def show_student_info(frame):
            year_level_label = tk.Label(frame, text='    Year Level:', fg='#fff', bg='#00008B', font=('calibri', 10))
            year_level_label.place(x=150, y=205)
            year_level_entry = tk.Entry(frame, width=50, bg='white')
            year_level_entry.place(x=140, y=225)

            course_label = tk.Label(frame, text='    Course:     ', fg='#fff', bg='#00008B', font=('calibri', 10))
            course_label.place(x=150, y=250)
            course_entry = tk.Entry(frame, width=50, bg='white')
            course_entry.place(x=140, y=275)

        def show_faculty_info(frame):
            department_label = tk.Label(frame, text='Department:', fg='#fff', bg='#00008B', font=('calibri', 10))
            department_label.place(x=150, y=205)
            department_entry = tk.Entry(frame, width=50, bg='white')
            department_entry.place(x=140, y=225)

            profession_label = tk.Label(frame, text='Profession:', fg='#fff', bg='#00008B', font=('calibri', 10))
            profession_label.place(x=150, y=250)
            profession_entry = tk.Entry(frame, width=50, bg='white')
            profession_entry.place(x=140, y=275)


        # FUNCTION TO UPDATE AND REFRESH TREEVIEW
        def clear_treeview(tree):
            for item in tree.get_children():
                tree.delete(item)

        def new_info():
            addr = entry_address.get()
            contacts = entry_contact_no.get()
            name = entry_name.get()
            member_type = member_type_combobox.get()

            if not (addr and contacts  and name and member_type):
                messagebox.showerror("Error", "Please fill in all the required fields.")
                input_win.focus_force()
                return

            conn.execute("UPDATE MEMBER SET Address=?, "
                         "Contact_No=?, Name=?, Member_Type=? WHERE Member_ID=?", (addr,
                                                                                   contacts, name, member_type,
                                                                                   Item_ID))
            conn.commit()

            input_win.destroy()

            # REFRESH TREEVIEW
            clear_treeview(tree_view)
            cursor = conn.execute("SELECT * FROM MEMBER")
            for row in cursor:
                tree_view.insert("", tk.END, values=row)

            # REENABLE EDIT UPON EXIT
            edit_button.config(state=tk.NORMAL)
            add_button.config(state=tk.NORMAL)
            remove_button.config(state=tk.NORMAL)
            faculty_button.config(state=tk.NORMAL)
            student_button.config(state=tk.NORMAL)

        def on_window_close():
            edit_button.config(state=tk.NORMAL)  # Enable the "Edit" button when the window is closed
            add_button.config(state=tk.NORMAL)
            remove_button.config(state=tk.NORMAL)
            student_button.config(state=tk.NORMAL)
            faculty_button.config(state=tk.NORMAL)
            input_win.destroy()

        input_win.protocol("WM_DELETE_WINDOW", on_window_close)

        # SAVE BUTTON
        save_button = tk.Button(input_win, text="Save", fg='#fff', bg='#8B0000', font=('Arial', 10, 'bold'), width=10,
                                command=lambda: new_info())
        save_button.grid(row=12, columnspan=2, pady=150)

def addmember_window(tree_view, edit_button, add_button, remove_button, student_button, faculty_button):
    edit_button.config(state=tk.DISABLED)
    add_button.config(state=tk.DISABLED)
    remove_button.config(state=tk.DISABLED)
    student_button.config(state=tk.DISABLED)
    faculty_button.config(state=tk.DISABLED)

    input_win = tk.Toplevel(lmsGui)
    input_win.title("Add a Member")
    input_win.configure(bg="#00008B")
    input_win.geometry("400x400+480+200")
    input_win.resizable(False, False)

    # Address
    lbl_address = tk.Label(input_win, text="Address:", bg='#00008B', fg='#fff')
    entry_address = tk.Entry(input_win, width=50)
    lbl_address.grid(row=1, column=0, padx=50, pady=3)
    entry_address.grid(row=2, column=0, padx=50, pady=3)

    # Contact No
    lbl_contact_no = tk.Label(input_win, text="Contact No:", bg='#00008B', fg='#fff')
    entry_contact_no = tk.Entry(input_win, width=50)
    lbl_contact_no.grid(row=3, column=0, padx=50, pady=3)
    entry_contact_no.grid(row=4, column=0, padx=50, pady=3)

    # Name
    lbl_name = tk.Label(input_win, text="Name:", bg='#00008B', fg='#fff')
    entry_name = tk.Entry(input_win, width=50)
    lbl_name.grid(row=5, column=0, padx=50, pady=3)
    entry_name.grid(row=6, column=0, padx=50, pady=3)

    def select_member_type(event):
        member_type = member_type_combobox.get()
        if member_type == "Student":
            show_student_info()
        elif member_type == "Faculty":
            show_faculty_info()

    # Member Type
    member_type_label = tk.Label(input_win, text="Member Type:", bg='#00008B', fg='#fff')
    member_type_combobox = ttk.Combobox(input_win, values=["Student", "Faculty"], width=47, state="readonly")
    member_type_combobox.bind("<<ComboboxSelected>>", select_member_type)
    member_type_label.grid(row=7, column=0, padx=50, pady=3)
    member_type_combobox.grid(row=8, column=0, padx=50, pady=3)

    def show_student_info():
        year_level_label = tk.Label(input_win, text='Year Level:', fg='#fff', bg='#00008B', font=('calibri', 10))
        year_level_label.grid(row=9, column=0, padx=50, pady=3)
        year_level_entry = tk.Entry(input_win, width=50, bg='white')
        year_level_entry.grid(row=10, column=0, padx=50, pady=3)

        course_label = tk.Label(input_win, text='Course:', fg='#fff', bg='#00008B', font=('calibri', 10))
        course_label.grid(row=11, column=0, padx=50, pady=3)
        course_entry = tk.Entry(input_win, width=50, bg='white')
        course_entry.grid(row=12, column=0, padx=50, pady=3)

        def confirm_student_member():
            address = entry_address.get()
            contact_no = entry_contact_no.get()
            name = entry_name.get()
            member_type = member_type_combobox.get()
            year_level = year_level_entry.get()
            course = course_entry.get()

            # Check if any of the required fields are empty
            if not (address and contact_no and name and member_type and year_level and course):
                messagebox.showerror("Error", "Please fill in all the required fields.")
                input_win.focus_force()
                return

            try:
                # Insert data into the MEMBER table
                conn.execute("INSERT INTO MEMBER (Address, Contact_No, Name, Member_Type) VALUES (?, ?, ?, ?)",
                             (address, contact_no, name, 'Student'))

                # Get the last inserted Member_ID (AUTOINCREMENT value)
                member_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

                # Insert data into the STUDENT table with references to the MEMBER table
                conn.execute("INSERT INTO STUDENT (Member_ID, Year_Level, Course) VALUES (?, ?, ?)",
                             (member_id, year_level, course))

                conn.commit()

                # Insert the new member's data into the Treeview
                tree_view.insert("", tk.END, values=(member_id, address, contact_no, name, member_type))

                input_win.destroy()

                # REENABLE EDIT UPON EXIT
                edit_button.config(state=tk.NORMAL)
                add_button.config(state=tk.NORMAL)
                remove_button.config(state=tk.NORMAL)
                student_button.config(state=tk.NORMAL)
                faculty_button.config(state=tk.NORMAL)

            except sqlite3.Error as e:
                conn.rollback()
                messagebox.showerror("Error", f"An error occurred: {e}")

        # Confirm Borrow button
        btn_confirm_borrow = tk.Button(input_win, text="Add Member", fg='#fff', bg='#8B0000',
                                       font=('Arial', 10, 'bold'), command=confirm_student_member)
        btn_confirm_borrow.grid(row=13, column=0, pady=10)

    def show_faculty_info():
        department_label = tk.Label(input_win, text='Department:', fg='#fff', bg='#00008B', font=('calibri', 10))
        department_label.grid(row=9, column=0, padx=50, pady=3)
        department_entry = tk.Entry(input_win, width=50, bg='white')
        department_entry.grid(row=10, column=0, padx=50, pady=3)

        profession_label = tk.Label(input_win, text='Profession:', fg='#fff', bg='#00008B', font=('calibri', 10))
        profession_label.grid(row=11, column=0, padx=50, pady=3)
        profession_entry = tk.Entry(input_win, bg='white', width=50)
        profession_entry.grid(row=12, column=0, padx=50, pady=3)

        def confirm_faculty_member():
            address = entry_address.get()
            contact_no = entry_contact_no.get()
            name = entry_name.get()
            member_type = member_type_combobox.get()
            department = department_entry.get()
            profession = profession_entry.get()

            # Check if any of the required fields are empty
            if not (address and contact_no and name and member_type and department and profession):
                messagebox.showerror("Error", "Please fill in all the required fields.")
                input_win.focus_force()
                return

            try:
                # Insert data into the MEMBER table
                conn.execute("INSERT INTO MEMBER (Address, Contact_No, Name, Member_Type) VALUES (?, ?, ?, ?)",
                             (address, contact_no, name, 'Faculty'))

                # Get the last inserted Member_ID (AUTOINCREMENT value)
                member_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

                # Insert data into the FACULTY and PROFESSIONAL tables with references to the MEMBER table
                conn.execute("INSERT INTO FACULTY (Member_ID, Department) VALUES (?, ?)",
                             (member_id, department))
                conn.execute("INSERT INTO PROFESSIONAL (Member_ID, Profession) VALUES (?, ?)",
                             (member_id, profession))

                conn.commit()

                # Insert the new member's data into the Treeview
                tree_view.insert("", tk.END, values=(member_id, address, contact_no, name, member_type))

                input_win.destroy()

                # REENABLE EDIT UPON EXIT
                edit_button.config(state=tk.NORMAL)
                add_button.config(state=tk.NORMAL)
                remove_button.config(state=tk.NORMAL)
                student_button.config(state=tk.NORMAL)
                faculty_button.config(state=tk.NORMAL)

            except sqlite3.Error as e:
                conn.rollback()
                messagebox.showerror("Error", f"An error occurred: {e}")

        # Confirm Borrow button
        btn_confirm_borrow = tk.Button(input_win, text="Add Member", fg='#fff', bg='#8B0000',
                                       font=('Arial', 10, 'bold'), command=confirm_faculty_member)
        btn_confirm_borrow.grid(row=13, column=0, pady=10)

    def on_window_close():
        edit_button.config(state=tk.NORMAL)  # Enable the "Edit" button when the window is closed
        add_button.config(state=tk.NORMAL)
        remove_button.config(state=tk.NORMAL)
        student_button.config(state=tk.NORMAL)
        faculty_button.config(state=tk.NORMAL)
        input_win.destroy()

    input_win.protocol("WM_DELETE_WINDOW", on_window_close)


def members():
    addgui = newFrame()
    goBack(addgui)

    def addmember():
        addmember_window(tree_view, edit_button, add_button, remove_button, student_button, faculty_button)

    def removemember(tree_view):
        selected_items = tree_view.selection()

        for item in selected_items:
            # Get the member ID of the selected row
            member_id = tree_view.item(item, "values")[0]

            # Delete the corresponding record from the 'members' table
            conn.execute("DELETE FROM MEMBER WHERE Member_ID = ?", (member_id,))

        # Commit the changes and update the Treeview
        conn.commit()
        tree_view.delete(*selected_items)

    tree_view = viewmembers(addgui)

    add_member = lambda: addmember()
    remove_member = lambda: removemember(tree_view)
    edit_member = lambda: editmember(tree_view, edit_button, add_button, remove_button, student_button, faculty_button)


    # Add button
    add_button = tk.Button(addgui, text="Add", fg='#fff', bg='#006400', font=('Arial', 10, 'bold'), width=10,
                           command=add_member)
    add_button.place(x=400, y=391)

    # Remove button
    remove_button = tk.Button(addgui, text="Remove", fg='#fff', bg='#8B0000', font=('Arial', 10, 'bold'), width=10,
                              command=remove_member)
    remove_button.place(x=300, y=391)

    # Edit button
    edit_button = tk.Button(addgui, text="Edit", fg='#fff', bg='#28a7c7', font=('Arial', 10, 'bold'), width=10,
                            command=edit_member)
    edit_button.place(x=500, y=391)

    def view_student_data():
        # Create a new window
        student_window = tk.Toplevel()
        student_window.title("Student Data")
        student_window.configure(bg="#00008B")
        student_window.geometry("600x280+400+250")
        edit_button.config(state=tk.DISABLED)
        add_button.config(state=tk.DISABLED)
        remove_button.config(state=tk.DISABLED)
        student_button.config(state=tk.DISABLED)
        faculty_button.config(state=tk.DISABLED)

        def edit_student_data():
            # Get the selected item in the Treeview
            selected_item = tree_view_student.selection()

            # Ensure that only one item is selected for editing
            if len(selected_item) != 1:
                messagebox.showerror("Error", "Please select one student to edit.")
                student_window.focus_force()
                return

            # Get the student data from the selected row
            member_id, year_level, course = tree_view_student.item(selected_item, "values")

            # Create a new window for editing student data
            edit_win = tk.Toplevel()
            edit_win.title("Edit Student Data")
            edit_win.configure(bg="#00008B")
            edit_win.geometry("300x200+550+300")
            edit_win.resizable(False, False)

            # Year Level
            lbl_year_level = tk.Label(edit_win, text="Year Level:", bg='#00008B', fg='#fff')
            lbl_year_level.grid(row=0, column=0, padx=30, pady=3)
            entry_year_level = tk.Entry(edit_win, width=20, bg='white')
            entry_year_level.grid(row=0, column=1, padx=30, pady=3)
            entry_year_level.insert(0, year_level)

            # Course
            lbl_course = tk.Label(edit_win, text="Course:", bg='#00008B', fg='#fff')
            lbl_course.grid(row=1, column=0, padx=30, pady=3)
            entry_course = tk.Entry(edit_win, width=20, bg='white')
            entry_course.grid(row=1, column=1, padx=30, pady=3)
            entry_course.insert(0, course)

            def save_changes():
                new_year_level = entry_year_level.get()
                new_course = entry_course.get()

                if not (new_year_level and new_course):
                    messagebox.showerror("Error", "Please fill in all the required fields.")
                    student_window.focus_force()
                    return

                # Update the student data in the database
                conn.execute("UPDATE STUDENT SET Year_Level = ?, Course = ? WHERE Member_ID = ?",
                             (new_year_level, new_course, member_id))
                conn.commit()

                # Update the Treeview with the new data
                tree_view_student.item(selected_item, values=(member_id, new_year_level, new_course))

                edit_win.destroy()

            # Save Changes button
            btn_save_changes = tk.Button(edit_win, text="Save Changes", fg='#fff', bg='#8B0000',
                                         font=('Arial', 10, 'bold'), command=save_changes)
            btn_save_changes.grid(row=2, column=0, columnspan=2, pady=10)

        # Create a Treeview in the new window
        tree_view_student = ttk.Treeview(student_window, columns=("Member ID", "Year Level", "Course"), show="headings")
        tree_view_student.heading("Member ID", text="Member ID")
        tree_view_student.heading("Year Level", text="Year Level")
        tree_view_student.heading("Course", text="Course")
        tree_view_student.pack()

        # Fetch data from the 'STUDENT' table with references to the 'MEMBER' table using JOIN
        cursor = conn.execute("""
            SELECT M.Member_ID, S.Year_Level, S.Course
            FROM MEMBER M
            LEFT JOIN STUDENT S ON M.Member_ID = S.Member_ID
            WHERE M.Member_Type = 'Student'  -- Show only student data
        """)

        # Insert data into the Treeview
        for row in cursor:
            tree_view_student.insert("", "end", values=row)

        def on_window_close():
            edit_button.config(state=tk.NORMAL)  # Enable the "Edit" button when the window is closed
            add_button.config(state=tk.NORMAL)
            remove_button.config(state=tk.NORMAL)
            student_button.config(state=tk.NORMAL)
            faculty_button.config(state=tk.NORMAL)
            student_window.destroy()
        student_window.protocol("WM_DELETE_WINDOW", on_window_close)

        # Edit button
        btn_edit_student = tk.Button(student_window, text="Edit", fg='#fff', bg='#28a7c7', font=('Arial', 10, 'bold'),
                                     width=10, command=edit_student_data)
        btn_edit_student.place(x=10, y=240)

        scrollbar = ttk.Scrollbar(student_window, orient="vertical", command=tree_view_student.yview)
        scrollbar.place(x=583, y=1, height=224)
        tree_view_student.configure(yscrollcommand=scrollbar.set)

    def view_faculty_data():
        # Create a new window
        data_window = tk.Toplevel()
        data_window.title("Faculty Data")
        data_window.configure(bg="#00008B")
        data_window.geometry("600x280+400+250")
        edit_button.config(state=tk.DISABLED)
        add_button.config(state=tk.DISABLED)
        remove_button.config(state=tk.DISABLED)
        student_button.config(state=tk.DISABLED)
        faculty_button.config(state=tk.DISABLED)

        def edit_faculty_data():
            # Get the selected item in the Treeview
            selected_item = tree_view_data.selection()

            # Ensure that only one item is selected for editing
            if len(selected_item) != 1:
                messagebox.showerror("Error", "Please select one faculty member to edit.")
                data_window.focus_force()
                return

            # Get the faculty data from the selected row
            member_id, department, profession = tree_view_data.item(selected_item, "values")

            # Create a new window for editing faculty data
            edit_win = tk.Toplevel()
            edit_win.title("Edit Faculty Data")
            edit_win.configure(bg="#00008B")
            edit_win.geometry("300x200+550+300")
            edit_win.resizable(False, False)

            # Department
            lbl_department = tk.Label(edit_win, text="Department:", bg='#00008B', fg='#fff')
            lbl_department.grid(row=0, column=0, padx=30, pady=3)
            entry_department = tk.Entry(edit_win, width=20, bg='white')
            entry_department.grid(row=0, column=1, padx=30, pady=3)
            entry_department.insert(0, department)

            # Profession
            lbl_profession = tk.Label(edit_win, text="Profession:", bg='#00008B', fg='#fff')
            lbl_profession.grid(row=1, column=0, padx=30, pady=3)
            entry_profession = tk.Entry(edit_win, width=20, bg='white')
            entry_profession.grid(row=1, column=1, padx=30, pady=3)
            entry_profession.insert(0, profession)

            def save_changes():
                new_department = entry_department.get()
                new_profession = entry_profession.get()

                if not (new_profession and new_department):
                    messagebox.showerror("Error", "Please fill in all the required fields.")
                    edit_win.focus_force()
                    return

                # Update the faculty data in the database
                conn.execute("UPDATE FACULTY SET Department = ? WHERE Member_ID = ?", (new_department, member_id))
                conn.execute("UPDATE PROFESSIONAL SET Profession = ? WHERE Member_ID = ?", (new_profession, member_id))
                conn.commit()

                # Update the Treeview with the new data
                tree_view_data.item(selected_item, values=(member_id, new_department, new_profession))

                edit_win.destroy()

            # Save Changes button
            btn_save_changes = tk.Button(edit_win, text="Save Changes", fg='#fff', bg='#8B0000',
                                         font=('Arial', 10, 'bold'), command=save_changes)
            btn_save_changes.grid(row=2, column=0, columnspan=2, pady=10)

        # Create a Treeview in the new window
        tree_view_data = ttk.Treeview(data_window, columns=("Member ID", "Department", "Profession"), show="headings")
        tree_view_data.heading("Member ID", text="Member ID")
        tree_view_data.heading("Department", text="Department")
        tree_view_data.heading("Profession", text="Profession")
        tree_view_data.pack()

        # Fetch data from the 'FACULTY' and 'PROFESSIONAL' tables using JOIN
        cursor = conn.execute("""
            SELECT M.Member_ID, F.Department, P.Profession
            FROM MEMBER M
            LEFT JOIN FACULTY F ON M.Member_ID = F.Member_ID
            LEFT JOIN PROFESSIONAL P ON M.Member_ID = P.Member_ID
            WHERE M.Member_Type = 'Faculty'
        """)

        # Insert data into the Treeview
        for row in cursor:
            tree_view_data.insert("", "end", values=row)

        def on_window_close():
            edit_button.config(state=tk.NORMAL)  # Enable the "Edit" button when the window is closed
            add_button.config(state=tk.NORMAL)
            remove_button.config(state=tk.NORMAL)
            student_button.config(state=tk.NORMAL)
            faculty_button.config(state=tk.NORMAL)
            data_window.destroy()
        
        data_window.protocol("WM_DELETE_WINDOW", on_window_close)

        # Edit button
        btn_edit_faculty = tk.Button(data_window, text="Edit", fg='#fff', bg='#28a7c7', font=('Arial', 10, 'bold'),
                                     width=10, command=edit_faculty_data)
        btn_edit_faculty.place(x=10, y=240)

        scrollbar = ttk.Scrollbar(data_window, orient="vertical", command=tree_view_data.yview)
        scrollbar.place(x=583, y=1, height=224)
        tree_view_data.configure(yscrollcommand=scrollbar.set)

    # Student button
    student_button = tk.Button(addgui, text="Student Data", fg='#fff', bg='#800080', font=('Arial', 10, 'bold'), width=15,
                               command=view_student_data)
    student_button.place(x=160, y=391)

    # Faculty button
    faculty_button = tk.Button(addgui, text="Faculty Data", fg='#fff', bg='#800080', font=('Arial', 10, 'bold'), width=15,
                               command=view_faculty_data)
    faculty_button.place(x=600, y=391)


def loan():
    addgui = newFrame()
    goBack(addgui)
    tree = viewlogs(addgui)
    # Retrieve data from the MEMBER table
    cursor = conn.execute("SELECT * FROM LOAN")

    # Display data in the table
    for row in cursor:
        tree.insert("", tk.END, values=row)

# Global variable to store the selected row data
selected_row_data = None
def update_treeview(tree_view):
    # Clear existing data from the Treeview
    tree_view.delete(*tree_view.get_children())

    # Fetch data from the FINE table
    cursor = conn.execute("SELECT * FROM FINE")
    fine_data = cursor.fetchall()

    # Display data in the Treeview
    for data in fine_data:
        tree_view.insert("", tk.END, values=data)

def submit_payment(payment_method_var, tree_view):
    global selected_row_data

    if selected_row_data:
        # Get the selected payment method
        selected_method = payment_method_var.get()
        if not (selected_method):
            messagebox.showerror("Error", "Please fill in all the required fields.")
            return
        # Get the necessary data from the selected row
        fine_date = datetime.date.today()
        amount = 0
        reason_fine = "Late"
        payment_method = selected_method
        standard_no = selected_row_data[1]
        member_id = selected_row_data[2]

        # Check if a record with the same standard_no and member_id already exists in FINE table
        cursor = conn.cursor()
        cursor.execute("""
            SELECT COUNT(*)
            FROM FINE
            WHERE standard_no = ? AND member_id = ?
        """, (standard_no, member_id))
        count = cursor.fetchone()[0]

        if count > 0:
            # If a record exists, update the payment method in the existing row
            cursor.execute("""
                UPDATE FINE
                SET fine_date = ?, amount = ?, reason_fine = ?, payment_method = ?
                WHERE standard_no = ? AND member_id = ?
            """, (fine_date, amount, reason_fine, payment_method, standard_no, member_id))
            print("Data updated in FINE table successfully.")
        else:
            # If no record exists, insert the data into the FINE table
            cursor.execute("""
                INSERT INTO FINE (fine_date, amount, reason_fine, payment_method, standard_no, member_id)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (fine_date, amount, reason_fine, payment_method, standard_no, member_id))
            print("Data inserted into FINE table successfully.")

        # Commit the changes to the database
        conn.commit()

        # Update the Treeview with the latest data
        update_treeview(tree_view)
    else:
        print("Please select a row from the table first.")

def payment_callback(tree):
    global selected_row_data
    selected_row = tree.focus()  # Get the selected row ID
    if selected_row:
        selected_row_data = tree.item(selected_row, 'values')
        payment_window = tk.Toplevel()
        payment_window.geometry("300x300")
        payment_window.title("Select Payment Method")

        # Set the background color of the payment window to dark blue
        payment_window.configure(bg="#00008B")

        # Create and add content to the payment window
        label = ttk.Label(payment_window, text="Select Payment Method:", background='#00008B', foreground='#fff')
        label.pack(pady=10)

        # Create a custom style for the radio buttons with dark blue background and white text
        style = ttk.Style()
        style.configure("DarkBlue.TRadiobutton", background="#00008B", foreground="#fff")

        # Create radio buttons for payment method options
        payment_method_var = tk.StringVar()

        cash_radio = ttk.Radiobutton(payment_window, text="Cash", variable=payment_method_var, value="Cash",
                                     style="DarkBlue.TRadiobutton")
        cash_radio.pack(anchor=tk.W, pady=5, padx=80)

        credit_card_radio = ttk.Radiobutton(payment_window, text="Credit Card", variable=payment_method_var,
                                            value="Credit Card", style="DarkBlue.TRadiobutton")
        credit_card_radio.pack(anchor=tk.W, pady=5, padx=80)

        paypal_radio = ttk.Radiobutton(payment_window, text="PayPal", variable=payment_method_var, value="PayPal",
                                       style="DarkBlue.TRadiobutton")
        paypal_radio.pack(anchor=tk.W, pady=5, padx=80)

        mobile_payment_radio = ttk.Radiobutton(payment_window, text="Gcash", variable=payment_method_var,
                                               value="Gcash", style="DarkBlue.TRadiobutton")
        mobile_payment_radio.pack(anchor=tk.W, pady=5, padx=80)

        mobile_payment_radio = ttk.Radiobutton(payment_window, text="Paymaya", variable=payment_method_var,
                                               value="Paymaya", style="DarkBlue.TRadiobutton")
        mobile_payment_radio.pack(anchor=tk.W, pady=5, padx=80)

        bank_transfer_radio = ttk.Radiobutton(payment_window, text="Bank Transfer", variable=payment_method_var,
                                              value="Bank Transfer", style="DarkBlue.TRadiobutton")
        bank_transfer_radio.pack(anchor=tk.W, pady=5, padx=80)

        confirm_button = tk.Button(payment_window, text="Confirm", fg='#fff', bg='#006400', font=('Arial', 9, 'bold'),
                                   width=8,
                                   command=lambda: submit_payment(payment_method_var, tree))
        confirm_button.place(x=100, y=230)

    else:
        print("Please select a row from the table first.")

def fine_add():
    cursor = conn.cursor()

    # Retrieve data from the LOAN table
    cursor.execute("""
            SELECT Due_Date, standard_no, member_id
            FROM LOAN
            WHERE Due_Date < Return_Date 
        """)
    loan_data = cursor.fetchall()

    # Insert the loan_data into the FINE table
    for data in loan_data:
        fine_date = datetime.date.today()
        amount = 0
        reason_fine = "Late"
        payment_method = ""
        standard_no = data[1]
        member_id = data[2]

        # Check if a record with the same standard_no and member_id already exists in FINE table
        cursor.execute("""
            SELECT COUNT(*)
            FROM FINE
            WHERE standard_no = ? AND member_id = ?
        """, (standard_no, member_id))
        count = cursor.fetchone()[0]

        if count == 0:
            # If no record exists, insert the data into the FINE table
            cursor.execute("""
                INSERT INTO FINE (fine_date, amount, reason_fine, payment_method, standard_no, member_id)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (fine_date, amount, reason_fine, payment_method, standard_no, member_id))

    # Commit the changes to the database
    conn.commit()
    print("Data inserted into FINE table successfully.")


def fine():
    addgui = newFrame()
    goBack(addgui)

    # Create a Treeview widget
    tree = ttk.Treeview(addgui)
    tree.place(x=20, y=45, width=840, height=340)

    # Define columns
    tree["columns"] = ("Fine_ID", "Standard_No", "Member_ID", "Fine_Date", "Amount", "Reason_Fine", "Payment_Method")

    # Format columns
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("Fine_ID", width=120, anchor=tk.CENTER)
    tree.column("Standard_No", width=120, anchor=tk.CENTER)
    tree.column("Member_ID", width=120, anchor=tk.CENTER)
    tree.column("Fine_Date", width=120, anchor=tk.CENTER)
    tree.column("Amount", width=120, anchor=tk.W)
    tree.column("Reason_Fine", width=120, anchor=tk.CENTER)
    tree.column("Payment_Method", width=118, anchor=tk.CENTER)

    # Create headings
    tree.heading("#0", text="", anchor=tk.CENTER)
    tree.heading("Fine_ID", text="Fine ID", anchor=tk.CENTER)
    tree.heading("Standard_No", text="Standard No", anchor=tk.CENTER)
    tree.heading("Member_ID", text="Member ID", anchor=tk.CENTER)
    tree.heading("Fine_Date", text="Fine Date", anchor=tk.CENTER)
    tree.heading("Amount", text="Amount", anchor=tk.CENTER)
    tree.heading("Reason_Fine", text="Reason of Fine", anchor=tk.CENTER)
    tree.heading("Payment_Method", text="Payment Method", anchor=tk.CENTER)

    fine_add()
    # Fetch data from the FINE table only once
    cursor = conn.execute("SELECT * FROM FINE")
    fine_data = cursor.fetchall()

    # Display data in the table
    for data in fine_data:
        tree.insert("", tk.END, values=data)


    payment_button = tk.Button(addgui, text=" Mode of Payment", fg='#fff', bg='#006400', font=('Arial', 10, 'bold'), width=18,
                           command=lambda: payment_callback(tree))
    payment_button.place(x=350, y=391)

    # Scrollbar
    scrollbar = ttk.Scrollbar(addgui, orient="vertical", command=tree.yview)
    scrollbar.place(x=860, y=45, height=340)
    tree.configure(yscrollcommand=scrollbar.set)

# def log_out():
#     print("logout button clicked")


# MAIN
Banner = Header(lmsGui)
DateDev = Header2()
hsi = homescreenImage(lmsGui)
bt1 = addLibMat(add_books)
bt2 = remLibMat(remove_books)
bt3 = dspLibMat(disp_books)
bt4 = borLibMat(borrow_book)
bt5 = retLibMat(return_books)
bt6 = dspMember(members)
bt7 = dspLoan(loan)
bt8 = fineDetail(fine)
# bt9 = logOut(log_out)
whatTime = dispClock()

# MAKE GUI VISIBLE
lmsGui.resizable(False, False)
lmsGui.mainloop()