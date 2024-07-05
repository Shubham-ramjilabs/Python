from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def handle_login():
    email=emial_input.get()
    password=pass_input.get()
   

    if email=="shubham@gmail.com" and password=='123':
        messagebox.showinfo('Login',"login Sccessfull")
    else:
        messagebox.showerror('Error',"Login failed")





root=Tk()#Create object of tkinter
root.title("Login page")#Title of window
root.iconbitmap('D:/Python/Project/s.jpg')#Icon of window
root.geometry("400x500")#Size of window
root.configure(background="#856ff8")#Background of window colour

img1=Image.open('D:/Python/Project/flipkart.png')#open image
resize_img=img1.resize((70,70))#resize image

img=ImageTk.PhotoImage(resize_img)#convert image

img_label=Label(root,image=img)#add image
img_label.pack(pady=(10,10))#padding
text_label=Label(root,text='Flipkart',bg='#856ff8',fg='white')
text_label.pack()
text_label.config(font=("verdana",16,"bold"))

email_label=Label(root,text='Enter Email',fg='white',bg='#856ff8')
email_label.pack(pady=(20,5))
email_label.config(font=("verdana",12,"bold"))
emial_input=Entry(root,width=(50))
emial_input.pack(ipady=6,pady=(1,15))

pass_label=Label(root,text='Enter passwprd',fg='white',bg='#856ff8')
pass_label.pack(pady=(20,5))
pass_label.config(font=("verdana",12,"bold"))
pass_input=Entry(root,width=(50))
pass_input.pack(ipady=6,pady=(1,15))

login_btn=Button(root,text='Login',fg='black',bg='white',width=9,height=2,command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',10))

root.mainloop()#run the window