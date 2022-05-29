import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from cv2 import COLOR_BGR2GRAY
import mysql.connector
import dlib 
import cv2

class course_details_student_page:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1204x750+0+0")
        self.root.title("Parousia - Student Details")

        file=open("session_detail.txt",'r')
        roll=file.readlines()[0].strip('\n')
        file.close()

        #creating variables to store data
        self.department_variable=tk.StringVar()
        self.roll_no_variable=roll
        self.course_variable=tk.StringVar()
        self.prof_variable=tk.StringVar()
        self.semester_variable=tk.StringVar()
        self.year_variable=tk.StringVar()
 
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
        course_details_label=tk.Label(frame,text="Course Details",font=("Candara",23,"bold"),fg="black",bg="#49bbc6",bd=2,relief="solid")
        course_details_label.place(x=0,y=0,width=600,height=50)

        #label for department
        department_label=tk.Label(frame,text="Enter Department:",font=("Candara",14,"bold"),fg="black",bg="#49bbc6")
        department_label.place(x=175,y=70)

        #combo box for department
        self.department_combobox=ttk.Combobox(frame,font=("Candara",14),state="readonly",textvariable=self.department_variable)
        self.department_combobox["values"]=('----Select Department----','CSE','AIDE','EE')
        self.department_combobox.place(x=175,y=95,width=250)
        self.department_combobox.current(0)

        #label for semester
        semester_label=tk.Label(frame,text="Enter Semester:",font=("Candara",14,"bold"),fg="black",bg="#49bbc6")
        semester_label.place(x=0,y=160)

        #combo box for semester
        self.semester_combobox=ttk.Combobox(frame,font=("Candara",14),state="readonly",textvariable=self.semester_variable)
        self.semester_combobox["values"]=('----Select Semester----','1','2')
        self.semester_combobox.place(x=0,y=185,width=250)
        self.semester_combobox.current(0)

        #label for year
        year_label=tk.Label(frame,text="Enter Year:",font=("Candara",14,"bold"),fg="black",bg="#49bbc6")
        year_label.place(x=350,y=160)

        #combo box for year
        self.year_combobox=ttk.Combobox(frame,font=("Candara",14),state="readonly",textvariable=self.year_variable)
        self.year_combobox["values"]=('----Select Year---','AY 21-22','AY 22-23')
        self.year_combobox.place(x=350,y=185,width=250)
        self.year_combobox.current(0)

        #label for course
        course_label=tk.Label(frame,text="Enter Course:",font=("Candara",14,"bold"),fg="black",bg="#49bbc6")
        course_label.place(x=0,y=250)

        #combo box for course
        self.course_combobox=ttk.Combobox(frame,font=("Candara",14),state="readonly",textvariable=self.course_variable)
        self.course_combobox["values"]=('----Select Course----','DSA','ML','WebDev')
        self.course_combobox.place(x=0,y=275,width=250)
        self.course_combobox.current(0)

        #label for Professor
        prof_label=tk.Label(frame,text="Enter Professor:",font=("Candara",14,"bold"),fg="black",bg="#49bbc6")
        prof_label.place(x=350,y=250)

        #entry field for professor
        self.prof=ttk.Entry(frame,font=("Candara",14),textvariable=self.prof_variable)
        self.prof.place(x=350,y=275,width=250)

        #button to save details
        save_button=tk.Button(frame,text="Save details",font=("Candara",14),fg="black",bg="#00a4b7",bd=3,command=self.add_details_to_database)
        save_button.place(x=100,y=360,width=400,height=30)

        #button to take photo sample
        reset_button=tk.Button(frame,text="Take Photo Sample",font=("Candara",14),fg="black",bg="#00a4b7",bd=3,command=self.create_dataset)
        reset_button.place(x=100,y=445,width=400,height=30)

    #function to add data to database
    def add_details_to_database(self):
        if self.department_variable.get()=="----Select Department----" or str(self.roll_no_variable)=="" \
        or self.prof.get()=="" or self.semester_variable.get()=="----Select Semester----" \
                or self.year_variable.get()=="----Select Year----" or self.course_variable.get=="----Select Course----":
            messagebox.showerror("Error","All Fields Are Compulsory!!")
    

        else:
            connect=mysql.connector.connect(host="localhost",user="root",password="mysqlroot",database="mydata")
            cursor=connect.cursor()
            query=("select * from userdetails where rollnumber=%s")
            value=(str(self.roll_no_variable),)
            cursor.execute(query,value)

            row=cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","User does not exist, please try another Roll Number or create a new account")
            else:
                sql_update_query = """Update userdetails set department=%s,semester=%s,course=%s,year=%s,professor=%s where rollnumber = %s"""
                input_data = (self.department_variable.get(),self.semester_variable.get(),self.course_variable.get(),self.year_variable.get(),self.prof_variable.get(), str(self.roll_no_variable))
                cursor.execute(sql_update_query, input_data)

                connect.commit()
                connect.close()
                messagebox.showinfo("Success","Details Saved Successfully")


    def create_dataset(self):
        classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        def face_cropped(img):
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=classifier.detectMultiScale(gray,1.3,5)

            for (x,y,w,h) in faces:
                face_cropped=img[y:y+h,x:x+w]
                return face_cropped

        cap=cv2.VideoCapture(0)
        image_id=0
        while(True):
            ret,frames=cap.read()
            if face_cropped(frames) is not None:
                image_id+=1
                face=cv2.resize(face_cropped(frames),(400,400))
                face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                file_name_path="data/user"+"."+str(self.roll_no_variable)+"."+str(image_id)+".jpg"
                cv2.imwrite(file_name_path,face)
                cv2.putText(face,str(image_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,0),2)
                cv2.imshow("cropped face",face)
            if face_cropped(frames) is None:
                messagebox.showerror("error","No face detected!")
                break

            if cv2.waitKey(1)==13 or int(image_id)==10:
                break

        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("result","data set generated")



if __name__=="__main__":
    root=tk.Tk()
    root.resizable(width=False, height=False)
    object=course_details_student_page(root)
    root.mainloop()

