import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from course_details_student_page import course_details_student_page
from attendance_record_student_page import attendance_record_student_page
from helpdesk import help_desk

class student_page:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1204x750+0+0")
        self.root.title("Parousia - Student Portal")

        #add background image
        bg_image=Image.open('images\\admin_page_bg.jpg')
        bg_image=bg_image.resize((1204,750),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg_image)
        label_bg=tk.Label(self.root,image=self.bg)
        label_bg.place(x=0,y=0,relheight=1,relwidth=1)

        #add label for title
        page_title_label=tk.Label(self.root,text="Parousia - Student Portal",font=("Candara",30,"bold"),fg="black",bg="#edf4fa")
        page_title_label.place(x=0,y=0,width=1204,height=50)

        #button for course details
        course_details_image=Image.open('images\student_details_button.jpg')
        course_details_image=course_details_image.resize((172,140),Image.ANTIALIAS)
        self.course_details=ImageTk.PhotoImage(course_details_image)
        button_course_details=tk.Button(label_bg,image=self.course_details,cursor="hand2",command=self.course_details_window)
        button_course_details.place(x=172,y=330,width=172,height=140)
        button_course_details_title=tk.Button(label_bg,text="Student Details",font=("Candara",16),cursor="hand2",fg="black",bg="#FD8F3B",command=self.course_details_window)
        button_course_details_title.place(x=172,y=470,width=172,height=30)

        
        #button to check attendance record
        student_record_image=Image.open('images\student_record_button.jpg')
        student_record_image=student_record_image.resize((172,140),Image.ANTIALIAS)
        self.student_record=ImageTk.PhotoImage(student_record_image)
        button_student_record=tk.Button(label_bg,image=self.student_record,cursor="hand2",command=self.attendance_record_window)
        button_student_record.place(x=513,y=330,width=175,height=140)
        button_student_record_title=tk.Button(label_bg,text="Attendance Record",font=("Candara",16),cursor="hand2",fg="black",bg="#FD8F3B",command=self.attendance_record_window)
        button_student_record_title.place(x=513,y=470,width=175,height=30)

        #button for helpdesk
        helpdesk_image=Image.open('images\helpdesk_button.jpg')
        helpdesk_image=helpdesk_image.resize((172,140),Image.ANTIALIAS)
        self.helpdesk=ImageTk.PhotoImage(helpdesk_image)
        button_helpdesk=tk.Button(label_bg,image=self.helpdesk,cursor="hand2",command=self.helpdesk_window)
        button_helpdesk.place(x=860,y=330,width=172,height=140)
        button_helpdesk_title=tk.Button(label_bg,text="Help Desk",font=("Candara",16),cursor="hand2",fg="black",bg="#FD8F3B",command=self.helpdesk_window)
        button_helpdesk_title.place(x=860,y=470,width=172,height=30)

        #button to logout
        button_logout_title=tk.Button(label_bg,text="LOGOUT",font=("Candara",16),cursor="hand2",fg="black",bg="#9AD8E6",command=self.logout_button)
        button_logout_title.place(x=1032,y=50,width=172,height=30)

    
    def course_details_window(self):
        self.user_window=tk.Toplevel(self.root)
        self.app=course_details_student_page(self.user_window)


    def attendance_record_window(self):
        self.user_window=tk.Toplevel(self.root)
        self.app=attendance_record_student_page(self.user_window)

    def helpdesk_window(self):
        self.user_window=tk.Toplevel(self.root)
        self.app=help_desk(self.user_window)

    def logout_button(self):
        file=open("session_detail.txt",'w')
        file.write("")
        file.close()
        self.root.destroy()




if __name__=="__main__":
    root=tk.Tk()
    root.resizable(width=False, height=False)
    object=student_page(root)
    root.mainloop()

