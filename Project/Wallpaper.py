from tkinter import *
from PIL import ImageTk,Image
import os
def next_img():
 global counter
 img_label.config(image=img_arr[counter%len(img_arr)])
 counter=counter+1


counter=1
root=Tk()
root.title("Wallpaper Viwer")
root.geometry("250x400")
root.config(bg='black')
files=os.listdir("D:/Python/Project/Wallpaper")

img_arr=[]
for file in files:
 img=Image.open(os.path.join('D:/Python/Project/Wallpaper',file)) 
 resized_img = img.resize((300, 300))
 img_arr.append(ImageTk.PhotoImage(resized_img))

img_label=Label(root,image=img_arr[0])
img_label.pack(pady=(15,10))
next_but=Button(root,text='Next',bg='white',fg='black',width=25,height=2,command=next_img)
next_but.pack()
root.mainloop()