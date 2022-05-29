import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import csv
from tkinter import filedialog

class attendance_record_student_page:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1204x750+0+0")
        self.root.title("Parousia - Attendance Record")
 
        #add background image
        bg_image=Image.open('images\\admin_page_bg.jpg')
        bg_image=bg_image.resize((1204,750),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg_image)
        label_bg=tk.Label(self.root,image=self.bg)
        label_bg.place(x=0,y=0,relheight=1,relwidth=1)

        #add label for title
        page_title_label=tk.Label(self.root,text="Parousia - Student Attendance Record",font=("Candara",30,"bold"),fg="black",bg="#edf4fa")
        page_title_label.place(x=0,y=0,width=1204,height=50)

        #adding a frame
        frame=tk.Frame(label_bg,bg="#49bbc6")
        frame.place(x=300,y=100,height=600,width=600)

        #adding a label
        course_details_label=tk.Label(frame,text="Attendance Record",font=("Candara",23,"bold"),fg="black",bg="#49bbc6",bd=2,relief="solid")
        course_details_label.place(x=0,y=0,width=600,height=50)

        
        #button to show entries
        search_button=tk.Button(frame,text="Show",font=("Candara",14),fg="black",bg="#00a4b7",bd=3,command=self.display_specific_data)
        search_button.place(x=200,y=80,width=200,height=30)

        #make a frame for the table
        table_frame=tk.Frame(frame,bd=2,bg="#0b4a51",relief=tk.RIDGE)
        table_frame.place(x=5,y=150,width=590,height=400)

        #adding scroll bars
        scroll_x=ttk.Scrollbar(table_frame,orient=tk.HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=tk.VERTICAL)

        self.details_table=ttk.Treeview(table_frame,column=("rollnumber","name","time","date","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=tk.BOTTOM,fill=tk.X)
        scroll_y.pack(side=tk.RIGHT,fill=tk.Y)

        self.details_table.heading("rollnumber",text="Roll Number")
        self.details_table.heading("name",text="Name")
        self.details_table.heading("time",text="Time")
        self.details_table.heading("date",text="Date")
        self.details_table.heading("status",text="Status")
        self.details_table["show"]="headings"

        self.details_table.pack(fill=tk.BOTH,expand=1)

        scroll_x.config(command=self.details_table.xview)
        scroll_y.config(command=self.details_table.yview)

        

    def display_specific_data(self):
        with open('attendance.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                file=open("session_detail.txt",'r')
                roll=file.readlines()[0].strip('\n')
                file.close()
                if str(row['rollno'])==str(roll):
                    rollnumber = row['rollno']
                    name = row['name']
                    time = row['time']
                    date = row['date']
                    status = row['status']
                    self.details_table.insert("", 0, values=(rollnumber, name, time, date, status))












if __name__=="__main__":
    root=tk.Tk()
    root.resizable(width=False, height=False)
    object=attendance_record_student_page(root)
    root.mainloop()

