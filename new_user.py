import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class New_User:
    def __init__(self,root):
        self.root=root

        #set window title
        self.root.title("Parousia - New User")

        window_width = 1204
        window_height = 750
        window_res = str(window_width)+'x'+str(window_height)+'+'+'0'+'+'+'0'
        self.root.geometry(window_res)
        
        #add background image
        bg_image=Image.open('images\\admin_page_bg.jpg')
        bg_image=bg_image.resize((window_width,window_height),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg_image)
        label_bg=tk.Label(self.root,image=self.bg)
        label_bg.place(x=0,y=0)
        
        #add label for title
        page_title_label=tk.Label(self.root,text="Parousia - Create New User",font=("Candara",30,"bold"),fg="black",bg="#edf4fa")
        page_title_label.place(x=0,y=0,width=1204,height=50)

        #adding a frame
        frame=tk.Frame(self.root,bg="#262424")
        frame.place(x=102,y=150,height=500,width=650)

        #adding icon
        icon_image=Image.open('images\\new_user_icon.jpg')
        self.icon=ImageTk.PhotoImage(icon_image)
        label_icon=tk.Label(self.root,image=self.icon)
        label_icon.place(x=752,y=150,height=500,width=350)

        #creating variables to store data
        self.first_name_variable=tk.StringVar()
        self.last_name_variable=tk.StringVar()
        self.roll_no_variable=tk.StringVar()
        self.password_variable=tk.StringVar()
        self.confirm_password_variable=tk.StringVar()
        self.sq_variable=tk.StringVar()
        self.sq_answer_variable=tk.StringVar()


        #label for login details
        login_details_label=tk.Label(frame,text="ENTER DETAILS",font=("Candara",22,"bold"),bg="#262424",fg="white")
        login_details_label.place(x=205,y=10)


        #label for first name
        first_name_label=tk.Label(frame,text="Enter First Name:",font=("Candara",14,"bold"),bg="#262424",fg="white")
        first_name_label.place(x=20,y=70)

        #entry field for first name
        self.first_name=ttk.Entry(frame,font=("Candara",14),textvariable=self.first_name_variable)
        self.first_name.place(x=20,y=95,width=275)

        #label for last name
        last_name_label=tk.Label(frame,text="Enter Last Name:",font=("Candara",14,"bold"),bg="#262424",fg="white")
        last_name_label.place(x=350,y=70)

        #entry field for last name
        self.last_name=ttk.Entry(frame,font=("Candara",14),textvariable=self.last_name_variable)
        self.last_name.place(x=350,y=95,width=275)

        #label for roll number
        rollno_label=tk.Label(frame,text="Enter Roll Number:",font=("Candara",14,"bold"),bg="#262424",fg="white")
        rollno_label.place(x=20,y=160)

        #entry field for roll number
        self.roll_no=ttk.Entry(frame,font=("Candara",14),textvariable=self.roll_no_variable)
        self.roll_no.place(x=20,y=185,width=275)

        #label for password
        password_label=tk.Label(frame,text="Enter Password:",font=("Candara",14,"bold"),bg="#262424",fg="white")
        password_label.place(x=20,y=250)

        #entry field for password
        self.password=ttk.Entry(frame,font=("Candara",14),textvariable=self.password_variable,show='*')
        self.password.place(x=20,y=275,width=275)

        #label for confirming password
        confirm_password_label=tk.Label(frame,text="Confirm Password:",font=("Candara",14,"bold"),bg="#262424",fg="white")
        confirm_password_label.place(x=350,y=250)

        #entry field for confirming password
        self.confirm_password=ttk.Entry(frame,font=("Candara",14),textvariable=self.confirm_password_variable,show='*')
        self.confirm_password.place(x=350,y=275,width=275)

        #label for answer to security question
        sq_answer_label=tk.Label(frame,text="Answer to Security Question:",font=("Candara",14,"bold"),bg="#262424",fg="white")
        sq_answer_label.place(x=350,y=340)

        #entry field for answer to security question
        self.sq_answer=ttk.Entry(frame,font=("Candara",14),textvariable=self.sq_answer_variable)
        self.sq_answer.place(x=350,y=365,width=275)

        #label for security question
        sq_label=tk.Label(frame,text="Choose Security Question:",font=("Candara",14,"bold"),bg="#262424",fg="white")
        sq_label.place(x=20,y=340)

        #combo box for security question
        self.sq_combobox=ttk.Combobox(frame,font=("Candara",14,"bold"),state="readonly",textvariable=self.sq_variable)
        self.sq_combobox["values"]=('----Select a question----','Which city were you born in?','What is your middle name?','What was the name of your first pet?')
        self.sq_combobox.place(x=20,y=365,width=275)
        self.sq_combobox.current(0)

        #button to save details
        save_details_button=tk.Button(frame,text="Save details",font=("Candara",14,"bold"),fg="black",bg="#e29c70",bd=3,command=self.store_login_data)
        save_details_button.place(x=180,y=445,width=275,height=30)


    #function to store login data 
    def store_login_data(self):
        if self.first_name_variable.get()=="" or self.roll_no_variable.get()=="" \
            or self.sq_variable.get()=="----Select a question----" or self.sq_answer_variable.get()=="" \
                 or self.password_variable.get()=="" or self.confirm_password_variable.get=="":
            messagebox.showerror("Error","All Fields Are Compulsory!!")
        
        elif self.password_variable.get()!=self.confirm_password_variable.get():
            messagebox.showerror("Error","Both Passwords Must Be Same")

        else:
            connect=mysql.connector.connect(host="localhost",user="root",password="mysqlroot",database="mydata")
            cursor=connect.cursor()
            query=("select * from userdetails where rollnumber=%s")
            value=(self.roll_no_variable.get(),)
            cursor.execute(query,value)

            row=cursor.fetchone()

            if row!=None:
                messagebox.showerror("Error","User Already Exists, please try another Roll Number")
            else:
                cursor.execute("insert into userdetails(firstname,lastname,rollnumber,password,securityquestion,securityanswer) values(%s,%s,%s,%s,%s,%s)",(self.first_name_variable.get(),self.last_name_variable.get(),self.roll_no_variable.get(),self.password_variable.get(),self.sq_variable.get(),self.sq_answer_variable.get()))
                connect.commit()
                connect.close()
                messagebox.showinfo("Success","Details Saved Successfully")
                self.root.destroy()




if __name__=="__main__":
    root=tk.Tk()
    root.resizable(width=False, height=False)
    app=New_User(root)
    root.mainloop()
