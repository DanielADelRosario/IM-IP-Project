import tkinter as tk
from tkinter import ttk
import sqlite3
import time
from datetime import date

conn = sqlite3.connect('library.db')

# CREATE GUI WINDOW
lmsGui = tk.Tk()
lmsGui.title("Library System Dashboard")
# SET GUI DIMENSIONS
lmsGui.geometry("900x550+250+100")


# GUI LIBRARY HEADER
def Header(lmsGui):
    fm = tk.Frame(lmsGui, height=500, width=900, bg='#fff')
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

# # Create the ITEM table if it doesn't exist
# conn.execute('''
#     CREATE TABLE IF NOT EXISTS ITEM (
#         Standard_No NVARCHAR(100) PRIMARY KEY NOT NULL,
#         Publisher NVARCHAR(100) NOT NULL,
#         Publish_Date DATE NOT NULL,
#         Author NVARCHAR(100) NOT NULL,
#         Title NVARCHAR(100) NOT NULL,
#         Item_Type NVARCHAR(10) NOT NULL,
#         Status TEXT DEFAULT 'Available'
#     )
# ''')

conn.commit()


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
    data2 = tk.Entry(addgui, width=70, bg='white')
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
    data5 = tk.Entry(addgui, width=70, bg='white')
    data5.place(x=290, y=300)

    def add_data_to_db():
        standard_no = data.get()
        publisher = data1.get()
        publish_date = data2.get()
        author = data3.get()
        title = data4.get()
        item_type = data5.get()
        status = 'Available'

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
        data5.delete(0, tk.END)

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

    # Retrieve data from the MEMBER table
    cursor = conn.execute("SELECT * FROM LOAN")

    # Display data in the table
    for row in cursor:
        tree.insert("", tk.END, values=row)

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


# FUNCTION TO SET BUTTON COMMANDS
def disp_books():
    addgui = newFrame()
    goBack(addgui)
    treeView(addgui)

def borrow_input_window(tree):
    input_win = tk.Toplevel(lmsGui)
    input_win.title("Borrow Material")
    input_win.geometry("400x400")

    # Member ID
    lbl_member_id = tk.Label(input_win, text="Member ID:")
    lbl_member_id.pack()
    entry_member_id = tk.Entry(input_win)
    entry_member_id.pack()

    # Address
    lbl_address = tk.Label(input_win, text="Address:")
    lbl_address.pack()
    entry_address = tk.Entry(input_win)
    entry_address.pack()

    # Contact No
    lbl_contact_no = tk.Label(input_win, text="Contact No:")
    lbl_contact_no.pack()
    entry_contact_no = tk.Entry(input_win)
    entry_contact_no.pack()

    # Name
    lbl_name = tk.Label(input_win, text="Name:")
    lbl_name.pack()
    entry_name = tk.Entry(input_win)
    entry_name.pack()

    selected_items = tree.selection()
    for item in selected_items:
        values = tree.item(item)['values']
        standard_no = values[0]  # Standard_No of the selected material
        conn.execute("UPDATE ITEM SET Status = ? WHERE Standard_No = ?", ('Borrowed', standard_no))
        conn.commit()

    def select_member_type(event):
        member_type = member_type_combobox.get()
        if member_type == "Student":
            show_student_info(input_win)
        elif member_type == "Faculty":
            show_faculty_info(input_win)


    member_type_label = tk.Label(input_win, text="Member Type:")
    member_type_label.pack()
    member_type_combobox = ttk.Combobox(input_win, values=["Student", "Faculty"], width= 17, state="readonly")
    member_type_combobox.pack()
    member_type_combobox.bind("<<ComboboxSelected>>", select_member_type)

    def show_student_info(frame):
        year_level_label = tk.Label(frame, text='    Year Level:', fg='#000000', font=('calibri', 10))
        year_level_label.place(x=150, y=205)
        year_level_entry = tk.Entry(frame, width=20, bg='white')
        year_level_entry.place(x=140, y=225)

        course_label = tk.Label(frame, text='    Course:     ', fg='#000000', font=('calibri', 10))
        course_label.place(x=150, y=250)
        course_entry = tk.Entry(frame, width=20, bg='white')
        course_entry.place(x=140, y=275)

    def show_faculty_info(frame):
        department_label = tk.Label(frame, text='Department:', fg='#000000', font=('calibri', 10))
        department_label.place(x=150, y=205)
        department_entry = tk.Entry(frame, width=20, bg='white')
        department_entry.place(x=140, y=225)

        profession_label = tk.Label(frame, text='Profession:', fg='#000000', font=('calibri', 10))
        profession_label.place(x=150, y=250)
        profession_entry = tk.Entry(frame, width=20, bg='white')
        profession_entry.place(x=140, y=275)

    # Function to perform the borrowing process
    def confirm_borrow():
        member_id = entry_member_id.get()
        address = entry_address.get()
        contact_no = entry_contact_no.get()
        name = entry_name.get()

        # Update the "Status" of the material to "Borrowed" in the ITEM table
        selected_items = tree.selection()
        for item in selected_items:
            values = tree.item(item)['values']
            standard_no = values[0]  # Standard_No of the selected material
            conn.execute("UPDATE ITEM SET Status = ? WHERE Standard_No = ?", ('Borrowed', standard_no))
            conn.commit()
            
            # Update the "Status" value in the Treeview for the borrowed item
            tree.set(item, "Status", "Borrowed")

        input_win.destroy()

    # Confirm Borrow button
    btn_confirm_borrow = tk.Button(input_win, text="Confirm Borrow", command=confirm_borrow)
    btn_confirm_borrow.place(x= 150, y=300)


def borrow_book():
    addgui = newFrame()
    goBack(addgui)

    def borrow_material(tree):
        borrow_input_window(tree)

    treeview = treeView(addgui)
    borrowmaterial = lambda: borrow_material(treeview)

    # Borrow button
    borrow_button = tk.Button(addgui, text="Borrow", fg='#fff', bg='#8B0000', font=('Arial', 10, 'bold'), width=10,
                              command=borrowmaterial)
    borrow_button.place(x=430, y=391)


def return_books():
    addgui = newFrame()
    goBack(addgui)

    def return_material(tree):
        selected_items = tree.selection()
        for item in selected_items:
            values = tree.item(item)['values']
            standard_no = values[0]  # Standard_No of the selected material

            # Update the "Status" of the material to "Borrowed" in the ITEM table
            conn.execute("UPDATE ITEM SET Status = ? WHERE Standard_No = ?", ('Available', standard_no))
            conn.commit()

            # Usable for message dialog
            print("Material with Standard No", standard_no, "has been successfully Returned")

            # Update the "Status" value in the Treeview for the borrowed item
            tree.set(item, "Status", "Available")

    treeview = treeView(addgui)
    returnmaterial = lambda: return_material(treeview)
    # Return button
    borrow_button = tk.Button(addgui, text="Return", fg='#fff', bg='#8B0000', font=('Arial', 10, 'bold'), width=10,
                              command=returnmaterial)
    borrow_button.place(x=430, y=391)

def addmember_window(tree_view):
    input_win = tk.Toplevel(lmsGui)
    input_win.title("Add a Member")
    input_win.configure(bg="#00008B")
    input_win.geometry("400x400+480+200")

    # Member ID
    lbl_member_id = tk.Label(input_win, text="Member ID:")
    lbl_member_id.pack()
    entry_member_id = tk.Entry(input_win)
    entry_member_id.pack()

    # Address
    lbl_address = tk.Label(input_win, text="Address:")
    lbl_address.pack()
    entry_address = tk.Entry(input_win)
    entry_address.pack()

    # Contact No
    lbl_contact_no = tk.Label(input_win, text="Contact No:")
    lbl_contact_no.pack()
    entry_contact_no = tk.Entry(input_win)
    entry_contact_no.pack()

    # Name
    lbl_name = tk.Label(input_win, text="Name:")
    lbl_name.pack()
    entry_name = tk.Entry(input_win)
    entry_name.pack()

    def select_member_type(event):
        member_type = member_type_combobox.get()
        if member_type == "Student":
            show_student_info(input_win)
        elif member_type == "Faculty":
            show_faculty_info(input_win)


    member_type_label = tk.Label(input_win, text="Member Type:")
    member_type_label.pack()
    member_type_combobox = ttk.Combobox(input_win, values=["Student", "Faculty"], width= 17, state="readonly")
    member_type_combobox.pack()
    member_type_combobox.bind("<<ComboboxSelected>>", select_member_type)

    def show_student_info(frame):
        year_level_label = tk.Label(frame, text='    Year Level:', fg='#000000', font=('calibri', 10))
        year_level_label.place(x=150, y=205)
        year_level_entry = tk.Entry(frame, width=20, bg='white')
        year_level_entry.place(x=140, y=225)

        course_label = tk.Label(frame, text='    Course:     ', fg='#000000', font=('calibri', 10))
        course_label.place(x=150, y=250)
        course_entry = tk.Entry(frame, width=20, bg='white')
        course_entry.place(x=140, y=275)

    def show_faculty_info(frame):
        department_label = tk.Label(frame, text='Department:', fg='#000000', font=('calibri', 10))
        department_label.place(x=150, y=205)
        department_entry = tk.Entry(frame, width=20, bg='white')
        department_entry.place(x=140, y=225)

        profession_label = tk.Label(frame, text='Profession:', fg='#000000', font=('calibri', 10))
        profession_label.place(x=150, y=250)
        profession_entry = tk.Entry(frame, width=20, bg='white')
        profession_entry.place(x=140, y=275)

    # Function to perform the borrowing process
    def confirm_member():
        member_id = entry_member_id.get()
        address = entry_address.get()
        contact_no = entry_contact_no.get()
        name = entry_name.get()
        member_type = member_type_combobox.get()

        # Execute the INSERT statement to add member information to the MEMBER table
        conn.execute("INSERT INTO MEMBER (Member_ID, Address, Contact_No, Name, Member_Type) VALUES (?, ?, ?, ?, ?)",
                    (member_id, address, contact_no, name, member_type))
        
        # Commit the changes and close the connection
        conn.commit()
        # Insert the new member's information directly into the treeview
        tree_view.insert("", tk.END, values=(member_id, address, contact_no, name, member_type))

        input_win.destroy()

    # Confirm Borrow button
    btn_confirm_borrow = tk.Button(input_win, text="Add Member", command=confirm_member)
    btn_confirm_borrow.place(x= 150, y=300)

def members():
    addgui = newFrame()
    goBack(addgui)

    def addmember():
        addmember_window(tree_view)
    def removemember():
        print()

    tree_view = viewmembers(addgui)

    add_member = lambda: addmember()

    remove_member = lambda: removemember(tree_view)

    # Add button
    add_button = tk.Button(addgui, text="Add", fg='#fff', bg='#006400', font=('Arial', 10, 'bold'), width=10,
                              command=add_member)
    add_button.place(x=350, y=391)

    # Remove button
    remove_button = tk.Button(addgui, text="Remove", fg='#fff', bg='#8B0000', font=('Arial', 10, 'bold'), width=10,
                              command=remove_member)
    remove_button.place(x=450, y=391)    

def loan():
    addgui = newFrame()
    goBack(addgui)
    viewlogs(addgui)

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

    # Retrieve data from the FINE table
    cursor = conn.execute("SELECT * FROM FINE")

    # Display data in the table
    for row in cursor:
        print("Retrieved row from the cursor:", row)
        tree.insert("", tk.END, values=row)

    # Scrollbar
    scrollbar = ttk.Scrollbar(addgui, orient="vertical", command=tree.yview)
    scrollbar.place(x=860, y=45, height=340)
    tree.configure(yscrollcommand=scrollbar.set)
    return tree


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
