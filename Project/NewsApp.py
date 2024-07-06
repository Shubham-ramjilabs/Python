import io
from urllib.error import URLError
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image
import webbrowser


class NewsApp:
    #fech data
    def __init__(self):
        #fech data
        self.data=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=5e061e96fd2c4853a1047ffb780f41b5').json()
        # initial gui
        self.load_gui()
        
        # load the firs news
        self.load_news(0)

    def load_gui(self):
        self.root=Tk()
        self.root.geometry('350x600')
        self.root.title('News App')
        self.root.config(bg='black')
        self.root.resizable(0,0)
        self.label=Label(self.root,text='News App',bg='black',fg='white',font=('verdana',20,'bold'))
        self.label.pack()

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    #img
    def load_news(self,index):
        #clear the screen for new news
        self.clear()
        img_url= self.data['articles'][index]['urlToImage']
        photo=None
        try:
            respone=urlopen(img_url,timeout=10)# Adjust timeout as needed
            row_data=respone.read()
            # row_data=urlopen(img_url).read()
            image=Image.open(io.BytesIO(row_data)).resize((350,250))
            photo=ImageTk.PhotoImage(image)
        except URLError as e:
            err_url='https://upload.wikimedia.org/wikipedia/commons/d/d1/Image_not_available.png'
            respone=urlopen(err_url,timeout=10)# Adjust timeout as needed
            row_data=respone.read()
            # row_data=urlopen(img_url).read()
            image1=Image.open(io.BytesIO(row_data)).resize((350,250))
            photo=ImageTk.PhotoImage(image1)
        except Exception as e:
            err_url='https://upload.wikimedia.org/wikipedia/commons/d/d1/Image_not_available.png'
            respone=urlopen(err_url,timeout=10)# Adjust timeout as needed
            row_data=respone.read()
            # row_data=urlopen(img_url).read()
            image1=Image.open(io.BytesIO(row_data)).resize((350,250))
            photo=ImageTk.PhotoImage(image1)
            
        if photo:
            lable=Label(self.root,image=photo)
            lable.pack()  
        else:
            if self.label.winfo_exists():
                self.label.config(text='Image not found')
            
        self.index=index
        #headline
        heading=Label(self.root,text=self.data['articles'][index]['title'],bg='black',fg='white',font=('verdana',14,'bold'),wraplength=350,justify=CENTER)
        heading.pack(pady=(10,20))
        
        #description
        details=Label(self.root,text=self.data['articles'][index]['description'],bg='black',fg='white',font=('verdana',11,'bold'),wraplength=350,justify=CENTER)
        details.pack(pady=(2,20))
        
        frame=Frame(self.root,bg='black') 
        frame.pack(expand=True,fill=BOTH) 

        #Buttons
        if index!=0:
            prev=Button(frame,text='Previous',bg='white',width=11,height=3 ,fg='black',font=('verdana',11,'bold'),command=lambda:self.load_news(index-1))     
            prev.pack(side=LEFT,)

        read=Button(frame,text='Read More',bg='white',width=11,height=3 ,fg='black',font=('verdana',11,'bold'),command=lambda:self.open_link(self.data['articles'][index]['url']))     
        read.pack(side=LEFT,)

        if index!=len(self.data['articles'])-1: 
            next=Button(frame,text='Next',bg='white',width=11,height=3 ,fg='black',font=('verdana',11,'bold'),command=lambda:self.load_news(index+1))     
            next.pack(side=LEFT)
        self.root.mainloop()
    def open_link(self,url): 
        webbrowser.open(url) 
        
        self.root.mainloop()
    




news=NewsApp()