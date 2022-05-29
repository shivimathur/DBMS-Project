import tkinter as tk
from tkinter import Toplevel, ttk
from PIL import Image, ImageTk
from tkinter import messagebox 
import mysql.connector
from login import login_window
import cv2
import datetime




class home_page:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1204x750+0+0")
        self.root.title("Parousia - Attendance Management System")

        #add background image
        bg_image=Image.open('images\\admin_page_bg.jpg')
        bg_image=bg_image.resize((1204,750),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg_image)
        label_bg=tk.Label(self.root,image=self.bg)
        label_bg.place(x=0,y=0,relheight=1,relwidth=1)

        #add label for title
        page_title_label=tk.Label(self.root,text="Parousia",font=("Candara",35,"bold"),fg="black",bg="#edf4fa")
        page_title_label.place(x=0,y=0,width=1203,height=50)


        #add label for title
        page_title_label=tk.Label(self.root,text="Attendance Management System",font=("Candara",20,"bold"),fg="black",bg="#edf4fa")
        page_title_label.place(x=0,y=45,width=1203,height=50)

        #button to record attendance
        record_attendance_image=Image.open('images\\record_attendance_button.jpg')
        record_attendance_image=record_attendance_image.resize((175,140),Image.ANTIALIAS)
        self.record_attendance=ImageTk.PhotoImage(record_attendance_image)
        button_record_attendance=tk.Button(label_bg,image=self.record_attendance,cursor="hand2",command=self.mark_attendance)
        button_record_attendance.place(x=516,y=200,width=175,height=140)
        button_record_attendance_title=tk.Button(label_bg,text="Record Attendance",font=("Candara",16),cursor="hand2",fg="black",bg="#FD8F3B",command=self.mark_attendance)
        button_record_attendance_title.place(x=516,y=340,width=175,height=30)

        #button to login
        button_login_title=tk.Button(label_bg,text="LOGIN",font=("Candara",16),cursor="hand2",fg="black",bg="#FD8F3B",command=self.go_to_login_window)
        button_login_title.place(x=516,y=650,width=172,height=30)

        #function to go to login page
    def go_to_login_window(self):
        self.go_login_window=Toplevel(self.root)
        self.app=login_window(self.go_login_window)

    def mark_attendance(self):
        def markAttendance(roll,name):
            with open('attendance.csv','r+',newline="\n") as f:
                myDataList = f.readlines()
                rollList = []
                
                now = datetime.datetime.now()
                time = now.strftime('%I:%M:%S:%p')
                date = now.strftime('%d-%B-%Y')

                for line in myDataList:
                    entry=line.split(',')
                    if entry[3]==date:
                        rollList.append(entry[0])

                if str(roll) not in rollList: 
                    f.writelines(f'\n{roll},{name},{time},{date},Present')

        def draw_boundary(img):

            scalefactor=1.1
            minNeighbour=10

            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=faceCascade.detectMultiScale(gray_image,scalefactor,minNeighbour)

            coord=[]
        

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+h])#inference
                confidence=int((100*(1-predict/300)))

                connect=mysql.connector.connect(host="localhost",user="root",password="mysqlroot",database="mydata")
                cursor=connect.cursor()
                cursor.execute("select firstname from userdetails where rollnumber="+str(id))
                row=cursor.fetchone()
                row='+'.join(row)
                

                if confidence>70 and row!=None:
                    cv2.putText(img,f"Name:{row}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Roll number:{id}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    markAttendance(id,row)


                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)

                coord=[x,y,w,h]
            return img


        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        cap=cv2.VideoCapture(0)
        while(True):
            ret,img=cap.read()
            img=draw_boundary(img)
            cv2.imshow("Welcome",img)

            if cv2.waitKey(1)==13:
                break
        cap.release()
        cv2.destroyAllWindows()

  

if __name__=="__main__":
    root=tk.Tk()
    root.resizable(width=False, height=False)
    app=home_page(root)
    root.mainloop()
