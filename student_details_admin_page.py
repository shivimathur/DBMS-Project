import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import dlib

class student_details_admin_page:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1204x750+0+0")
        self.root.title("Parousia - Student Details")

        self.roll_no_variable=tk.StringVar()
 
        #add background image
        bg_image=Image.open('images\\admin_page_bg.jpg')
        bg_image=bg_image.resize((1204,750),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg_image)
        label_bg=tk.Label(self.root,image=self.bg)
        label_bg.place(x=0,y=0,relheight=1,relwidth=1)

        #add label for title
        page_title_label=tk.Label(self.root,text="Parousia - Student Details",font=("Candara",30,"bold"),fg="black",bg="#edf4fa")
        page_title_label.place(x=0,y=0,width=1204,height=50)

        #adding a frame
        frame=tk.Frame(label_bg,bg="#49bbc6")
        frame.place(x=300,y=100,height=600,width=600)

        #adding a label
        course_details_label=tk.Label(frame,text="Student Details",font=("Candara",23,"bold"),fg="black",bg="#49bbc6",bd=2,relief="solid")
        course_details_label.place(x=0,y=0,width=600,height=50)

        #label for roll number
        roll_label=tk.Label(frame,text="Enter Roll Number:",font=("Candara",17),bg="#49bbc6",fg="black")
        roll_label.place(x=75,y=70)

        #entry field for roll number
        self.roll=ttk.Entry(frame,font=("Candara",14),textvariable=self.roll_no_variable)
        self.roll.place(x=270,y=70,width=230)

        #button to search entry
        search_button=tk.Button(frame,text="Search",font=("Candara",14),fg="black",bg="#00a4b7",bd=3,command=self.display_specific_data)
        search_button.place(x=75,y=110,width=200,height=30)

        #button to show all entries
        show_all_button=tk.Button(frame,text="Show all",font=("Candara",14),fg="black",bg="#00a4b7",bd=3,command=self.display_data)
        show_all_button.place(x=300,y=110,width=200,height=30)

        #make a frame for the table
        table_frame=tk.Frame(frame,bd=2,bg="#49bbc6",relief=tk.RIDGE)
        table_frame.place(x=5,y=150,width=590,height=400)

        #adding scroll bars
        scroll_x=ttk.Scrollbar(table_frame,orient=tk.HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=tk.VERTICAL)

        self.details_table=ttk.Treeview(table_frame,column=("first name","last name","roll number","department","course","year","semester"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=tk.BOTTOM,fill=tk.X)
        scroll_y.pack(side=tk.RIGHT,fill=tk.Y)

        self.details_table.heading("first name",text="First Name")
        self.details_table.heading("last name",text="Last Name")
        self.details_table.heading("roll number",text="Roll Number")
        self.details_table.heading("department",text="Department")
        self.details_table.heading("course",text="Course")
        self.details_table.heading("year",text="Year")
        self.details_table.heading("semester",text="Semester")
        self.details_table["show"]="headings"

        self.details_table.pack(fill=tk.BOTH,expand=1)

        scroll_x.config(command=self.details_table.xview)
        scroll_y.config(command=self.details_table.yview)
        self.display_data()

    def display_data(self):
        connect=mysql.connector.connect(host="localhost",user="root",password="mysqlroot",database="mydata")
        cursor=connect.cursor()
        query=("select firstname,lastname,rollnumber,department,course,year,semester from userdetails")
        cursor.execute(query)
        data=cursor.fetchall()

        if len(data)!=0:
            self.details_table.delete(*self.details_table.get_children())
            for i in data:
                self.details_table.insert("",tk.END,values=i)
            connect.commit()
        connect.close()

    def display_specific_data(self):
        connect=mysql.connector.connect(host="localhost",user="root",password="mysqlroot",database="mydata")
        cursor=connect.cursor()
        query=("select firstname,lastname,rollnumber,department,course,year,semester from userdetails where rollnumber=%s")
        roll=(self.roll_no_variable.get(),)
        cursor.execute(query,roll)
        data=cursor.fetchall()

        if len(data)!=0:
            self.details_table.delete(*self.details_table.get_children())
            for i in data:
                self.details_table.insert("",tk.END,values=i)
            connect.commit()
        connect.close()












if __name__=="__main__":
    root=tk.Tk()
    root.resizable(width=False, height=False)
    object=student_details_admin_page(root)
    root.mainloop()

