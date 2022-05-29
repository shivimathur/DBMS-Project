import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from student_details_admin_page import student_details_admin_page
import numpy as np
import cv2
from student_record_admin_page import student_record_admin_page
from helpdesk import help_desk
from tkinter import Toplevel
from new_user import New_User

class admin_page:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1204x750+0+0")
        self.root.title("Parousia - Admin Portal")

        #add background image
        bg_image=Image.open('images\\admin_page_bg.jpg')
        bg_image=bg_image.resize((1204,750),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg_image)
        label_bg=tk.Label(self.root,image=self.bg)
        label_bg.place(x=0,y=0,relheight=1,relwidth=1)

        #add label for title
        page_title_label=tk.Label(self.root,text="Parousia - Admin Portal",font=("Candara",30,"bold"),fg="black",bg="#edf4fa")
        page_title_label.place(x=0,y=0,width=1204,height=50)

        #button for student details
        student_details_image=Image.open('images\student_details_button.jpg')
        student_details_image=student_details_image.resize((172,140),Image.ANTIALIAS)
        self.student_details=ImageTk.PhotoImage(student_details_image)
        button_student_details=tk.Button(label_bg,image=self.student_details,cursor="hand2",command=self.student_details_window)
        button_student_details.place(x=172,y=190,width=172,height=140)
        button_student_details_title=tk.Button(label_bg,text="Student Details",font=("Candara",16),cursor="hand2",fg="black",bg="#FD8F3B",command=self.student_details_window)
        button_student_details_title.place(x=172,y=330,width=172,height=30)

        #button to train model
        train_model_image=Image.open('images\\train_model_button.jpg')
        train_model_image=train_model_image.resize((172,140),Image.ANTIALIAS)
        self.train_model=ImageTk.PhotoImage(train_model_image)
        button_train_model=tk.Button(label_bg,image=self.train_model,cursor="hand2",command=self.train_classifier)
        button_train_model.place(x=516,y=190,width=172,height=140)
        button_train_model_title=tk.Button(label_bg,text="Train Model",font=("Candara",16),cursor="hand2",fg="black",bg="#FD8F3B",command=self.train_classifier)
        button_train_model_title.place(x=516,y=330,width=172,height=30)

        #button to create new user
        create_image=Image.open('images\create_new_button.jpg')
        create_image=create_image.resize((172,140),Image.ANTIALIAS)
        self.create=ImageTk.PhotoImage(create_image)
        button_create=tk.Button(label_bg,image=self.create,cursor="hand2",command=self.new_user_window)
        button_create.place(x=860,y=190,width=172,height=140)
        button_create_title=tk.Button(label_bg,text="Create New User",font=("Candara",16),cursor="hand2",fg="black",bg="#FD8F3B",command=self.new_user_window)
        button_create_title.place(x=860,y=330,width=172,height=30)



        #button to check student attendance record
        student_record_image=Image.open('images\student_record_button.jpg')
        student_record_image=student_record_image.resize((172,140),Image.ANTIALIAS)
        self.student_record=ImageTk.PhotoImage(student_record_image)
        button_student_record=tk.Button(label_bg,image=self.student_record,cursor="hand2",command=self.student_record_window)
        button_student_record.place(x=344,y=500,width=177,height=140)
        button_student_record_title=tk.Button(label_bg,text="Attendance Record",font=("Candara",16),cursor="hand2",fg="black",bg="#FD8F3B",command=self.student_record_window)
        button_student_record_title.place(x=344,y=640,width=177,height=30)

        #button for helpdesk
        helpdesk_image=Image.open('images\helpdesk_button.jpg')
        helpdesk_image=helpdesk_image.resize((172,140),Image.ANTIALIAS)
        self.helpdesk=ImageTk.PhotoImage(helpdesk_image)
        button_helpdesk=tk.Button(label_bg,image=self.helpdesk,cursor="hand2",command=self.helpdesk_window)
        button_helpdesk.place(x=688,y=500,width=172,height=140)
        button_helpdesk_title=tk.Button(label_bg,text="Help Desk",font=("Candara",16),cursor="hand2",bg="#FD8F3B",fg="black",command=self.helpdesk_window)
        button_helpdesk_title.place(x=688,y=640,width=172,height=30)

        #button to logout
        button_logout_title=tk.Button(label_bg,text="LOGOUT",font=("Candara",16),cursor="hand2",fg="black",bg="#d7f0f5",command=self.logout_button)
        button_logout_title.place(x=1032,y=50,width=172,height=30)


    def student_details_window(self):
        self.user_window=tk.Toplevel(self.root)
        self.app=student_details_admin_page(self.user_window)



    def student_record_window(self):
        self.user_window=tk.Toplevel(self.root)
        self.app=student_record_admin_page(self.user_window)


    def helpdesk_window(self):
            self.user_window=tk.Toplevel(self.root)
            self.app=help_desk(self.user_window)

    def new_user_window(self):
        self.user_window=Toplevel(self.root)
        self.app=New_User(self.user_window)



    def logout_button(self):
        file=open("session_detail.txt",'w')
        file.write("")
        file.close()
        self.root.destroy()




    #function to train model with avaliable student data
    def train_classifier(self):
        data_directory=("data")
        paths=[os.path.join(data_directory,file) for file in os.listdir(data_directory)]
        
        faces=[]
        id=[]

        for image in paths:
            img=Image.open(image).convert("L") #grayscacling
            imageNp=np.array(img,'uint8')
            id_image=int(os.path.split(image)[1].split('.')[1])
            

            faces.append(imageNp)
            id.append(id_image)
            cv2.waitKey(1)==13

        id=np.array(id)

        #train classifier
        classifier=cv2.face.LBPHFaceRecognizer_create()
        classifier.train(faces,id)
        classifier.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("result","training completed")


if __name__=="__main__":
    root=tk.Tk()
    root.resizable(width=False, height=False)
    object=admin_page(root)
    root.mainloop()

