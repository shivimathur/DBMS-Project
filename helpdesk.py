import tkinter as tk
from tkinter import Toplevel, ttk
from PIL import Image, ImageTk
from tkinter import messagebox 
import mysql.connector
import cv2
import datetime


class help_desk:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1204x750+0+0")
        self.root.title("Parousia - Help Desk")

        #add background image
        bg_image=Image.open('images\helpdesk_bg.jpg')
        bg_image=bg_image.resize((1204,750),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg_image)
        label_bg=tk.Label(self.root,image=self.bg)
        label_bg.place(x=0,y=0,relheight=1,relwidth=1)

        #add label for title
        page_title_label=tk.Label(self.root,text="Parousia - Helpdesk",font=("Candara",30,"bold"),bg="black",fg="white")
        page_title_label.place(x=0,y=0,width=1203,height=50)

        #add label for email id
        email_label=tk.Label(self.root,text="Email-Id : stutiaswani13@gmail.com",font=("Candara",18,"bold"),bg="black",fg="white")
        email_label.place(x=390,y=130)

        #add label for phone number
        email_label=tk.Label(self.root,text="Phone : +919172881932",font=("Candara",18,"bold"),bg="black",fg="white")
        email_label.place(x=457,y=170)



      

if __name__=="__main__":
    root=tk.Tk()
    root.resizable(width=False, height=False)
    app=help_desk(root)
    root.mainloop()
