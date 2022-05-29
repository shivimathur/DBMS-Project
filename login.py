import tkinter as tk
from tkinter import Toplevel, ttk
from PIL import Image, ImageTk
from tkinter import messagebox 
import mysql.connector
from new_user import New_User
from student_page import student_page
from admin_page import admin_page


class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Parousia - Login")
        window_width = 1204
        window_height = 750
        window_res = str(window_width)+'x'+str(window_height)+'+'+'0'+'+'+'0' 
        self.root.geometry(window_res)
        
        self.roll_no_variable=tk.StringVar()
        
        #add background image
        bg_image=Image.open('images\\admin_page_bg.jpg')
        bg_image=bg_image.resize((window_width,window_height),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg_image)
        label_bg=tk.Label(self.root,image=self.bg)
        label_bg.place(x=0,y=0,relheight=1,relwidth=1)

        #add label for title
        page_title_label=tk.Label(self.root,text="Parousia - Login Page",font=("Candara",30,"bold"),fg="black",bg="#edf4fa")
        page_title_label.place(x=0,y=0,width=1203,height=50)

        #add login frame
        frame=tk.Frame(self.root,bg="#262424")
        frame.place(x=452,y=175,width=300,height=300)

        #label for roll number
        roll_number_label=tk.Label(frame,text="Enter Roll Number/Username:",font=("Candara",14,"bold"),bg="#262424",fg="white")
        roll_number_label.place(x=20,y=20)

        #entry field for roll number
        self.roll_number=ttk.Entry(frame,font=("Candara",14),textvariable=self.roll_no_variable)
        self.roll_number.place(x=20,y=50,width=260)

        #label for password
        password_label=tk.Label(frame,text="Enter Password:",font=("Candara",14,"bold"),bg="#262424",fg="white")
        password_label.place(x=20,y=100)

        #entry field for password
        self.password=ttk.Entry(frame,font=("Candara",14),show='*')
        self.password.place(x=20,y=130,width=260)

        #making a login button
        login_button=tk.Button(frame,text="Login",font=("Candara",14,"bold"),fg="black",bg="#e29c70",bd=3,command=self.login)
        login_button.place(x=75,y=180,width=150)

        #button for forgotten password
        forget_password_button=tk.Button(frame,text="Forgot Password?",font=("Candara",14,"bold"),fg="black",bg="#e29c70",bd=3,command=self.forgot_password)
        forget_password_button.place(x=50,y=240,width=200)



    
    def login(self):
        if self.roll_number.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All Fields Are Compulsory!!")
        
        elif self.roll_number.get()=="admin" and self.password.get()=="admin":
            self.new_window=Toplevel(self.root)
            self.app=admin_page(self.new_window)

        else:
            connect=mysql.connector.connect(host="localhost",user="root",password="mysqlroot",database="mydata")
            cursor=connect.cursor()
            cursor.execute("select * from userdetails where rollnumber=%s and password=%s",(self.roll_number.get(),self.password.get()))

            row=cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Roll Number or Password")
            else:
                file=open("session_detail.txt",'w')
                file.write(self.roll_no_variable.get())
                file.close()

                self.new_window=Toplevel(self.root)
                self.app=student_page(self.new_window)
            connect.commit()
            connect.close()

    #function to reset password to new password entered by user
    def reset_password(self):
        if self.sq_combobox.get()=="----Select a question----" or self.sq_combobox.get()=="":
            messagebox.showerror("Error","Select Valid Security Question",parent=self.new_window_fp)
        
        elif self.sq_answer.get()=="":
            messagebox.showerror("Error","Please Answer the Security Question",parent=self.new_window_fp)

        elif self.new_password.get()=="":
            messagebox.showerror("Error","Please enter new password",parent=self.new_window_fp)

        else:
            connect=mysql.connector.connect(host="localhost",user="root",password="mysqlroot",database="mydata")
            cursor=connect.cursor()
            query=("select * from userdetails where rollnumber=%s and securityquestion=%s and securityanswer=%s")
            value=(self.roll_number.get(),self.sq_combobox.get(),self.sq_answer.get())
            cursor.execute(query,value)
             
            row=cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Incorrect Answer to Security Question")
            else:
                query1=("update userdetails set password=%s where rollnumber=%s")
                value1=(self.new_password.get(),self.roll_number.get())
                cursor.execute(query1,value1)
                connect.commit()
                connect.close()
                messagebox.showinfo("Success","Password Reset Successful!",parent=self.new_window_fp)
            

    #fuction in case user forgets password
    def forgot_password(self):
        if self.roll_number.get()=="":
            messagebox.showerror("Error","Enter valid Roll Number to reset password")
        else:
            connect=mysql.connector.connect(host="localhost",user="root",password="mysqlroot",database="mydata")
            cursor=connect.cursor()
            query=("select * from userdetails where rollnumber=%s")
            value=(self.roll_number.get(),)
            cursor.execute(query,value)
            row=cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Invalid Roll Number")
            else:
                connect.close()
                self.new_window_fp=Toplevel(self.root)
                self.new_window_fp.title("Forgot Password")
                self.new_window_fp.geometry("400x400+200+200")

                reset_password_label=tk.Label(self.new_window_fp,text="Reset Password",font=("Candara",16),fg="black",bg="white")
                reset_password_label.place(x=115,y=10)

                sq_label=tk.Label(self.new_window_fp,text="Choose Security Question:",font=("Candara",14),fg="black",bg="white")
                sq_label.place(x=70,y=70)

                #combo box for security question
                self.sq_combobox=ttk.Combobox(self.new_window_fp,font=("Candara",14),state="readonly")
                self.sq_combobox["values"]=('----Select a question----','Which city were you born in?','What is your middle name?','What was the name of your first pet?')
                self.sq_combobox.place(x=70,y=100)
                self.sq_combobox.current(0)

                #label for answer to security question
                sq_answer_label=tk.Label(self.new_window_fp,text="Answer to Security Question:",font=("Candara",14),bg="white",fg="black")
                sq_answer_label.place(x=70,y=140)

                #entry field for answer to security question
                self.sq_answer=ttk.Entry(self.new_window_fp,font=("Candara",14))
                self.sq_answer.place(x=70,y=170,width=275)

                #label for entering new password
                new_password_label=tk.Label(self.new_window_fp,text="Enter New Password:",font=("Candara",14),bg="white",fg="black")
                new_password_label.place(x=70,y=220)

                #entry field for entering new password
                self.new_password=ttk.Entry(self.new_window_fp,font=("Candara",14))
                self.new_password.place(x=70,y=250,width=275)


                #button to reset password
                reset_password_button=tk.Button(self.new_window_fp,text="Reset Password",font=("Candara",14),fg="black",bg="white",bd=3,command=self.reset_password)
                reset_password_button.place(x=70,y=300,width=275,height=30)
        
    #function to open new user window
    def new_user_window(self):
        self.user_window=Toplevel(self.root)
        self.app=New_User(self.user_window)

        

if __name__=="__main__":
    root=tk.Tk()
    root.resizable(width=False, height=False)
    app=login_window(root)
    root.mainloop()