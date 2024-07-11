from tkinter import *
import math
first_num=second_num=result=None

def get_Digit(digit):
    if digit in ('00','000'):
        current=result_lable['text']
        new=current+'00'
        result_lable.config(text=new)
    else:
        current=result_lable['text']
        new=current+str(digit)
        result_lable.config(text=new)
    



def get_del():
        result_lable.config(text=result_lable['text'][:-1])

def clear():
    result_lable.config(text='')


def get_operation(op):
    global first_num,operator
    temp=result_lable['text']
    if '.' not in temp:
        first_num=int(temp)
        operator=op
        result_lable.config(text='')
    else:
        first_num=float(temp)
        operator=op
        result_lable.config(text='')

def get_result():
    global first_num,operator
    temp=result_lable['text']
    if '.' not in temp:
        second_num=int(temp)
    else:
        second_num=float(temp)
    if operator=='+':
        result_lable.config(text=first_num + second_num)
    elif operator=='-':
        result_lable.config(text=first_num - second_num)
    elif operator=='*':
        result_lable.config(text=first_num * second_num)
    elif operator=='/':
        if second_num==0:
            result_lable.config(text='Error')
        else:
            result_lable.config(text=first_num / second_num)
    elif operator=='%':
            result_lable.config(text=first_num % second_num)
    
    
def get_square():
    # global first_num
    first_num=int(result_lable['text'])
    if first_num<0 and first_num==0 and type(first_num)==int:
        result_lable.config(text=first_num ** 2)
    else:
        result_lable.config(text='Error')

def get_square_root():
    first_num=int(result_lable['text'])
    result_lable.config(text=math.sqrt(first_num))

root=Tk()
root.title("Calculator")
root.geometry("422x452")
root.resizable(0,0)
root.iconbitmap('D:/Python/Project/Wallpaper/s.jpg')


root.config(bg='black')

result_lable=Label(root,text='',fg='white',bg='black',font=('verdana',20,'bold'))
result_lable.grid(row=0,column=0,pady=(50,25),columnspan=6,sticky='w')

btn_mod=Button(root,text='%',fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'),command= lambda:get_operation('%'))
btn_mod.grid(row=1,column=0)

btn_All_Clear=Button(root,text='AC',fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'),command=clear)
btn_All_Clear.grid(row=1,column=1)

btn_Cancel=Button(root,text='C',fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'),command=clear)
btn_Cancel.grid(row=1,column=3)

btn_last_delete=Button(root,text="DEL",fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'),command=get_del)
btn_last_delete.grid(row=1,column=4,)

btn_history=Button(root,text='history',fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'))
btn_history.grid(row=2,column=0,)

btn_Squar=Button(root,text='x\u00b2',fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'),command=lambda:get_square())
btn_Squar.grid(row=2,column=1,)

btn_6=Button(root,text='√',fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'),command=lambda:get_square_root())
btn_6.grid(row=2,column=3,)

btn_div=Button(root,text='÷',fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'),command=lambda:get_operation('/'))
btn_div.grid(row=2,column=4,)

btn_7=Button(root,text='7',fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'),command=lambda:get_Digit(7))
btn_7.grid(row=3,column=0,)

btn_8=Button(root,text='8',fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'),command=lambda:get_Digit(8))
btn_8.grid(row=3,column=1,)

btn_9=Button(root,text='9',fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'),command=lambda:get_Digit(9))
btn_9.grid(row=3,column=3,)

btn_mul=Button(root,text='x',fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'),command=lambda:get_operation('*'))
btn_mul.grid(row=3,column=4,)

btn_4=Button(root,text='4',fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'),command=lambda:get_Digit(4))
btn_4.grid(row=4,column=0,)

btn_5=Button(root,text='5',fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'),command=lambda:get_Digit(5))
btn_5.grid(row=4,column=1,)

btn_6=Button(root,text='6',fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'),command=lambda:get_Digit(6))
btn_6.grid(row=4,column=3,)

btn_sub=Button(root,text='-',fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'),command=lambda:get_operation('-'))
btn_sub.grid(row=4,column=4,)

btn_1=Button(root,text='1',fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'),command=lambda:get_Digit(1))
btn_1.grid(row=5,column=0,)

btn_2=Button(root,text='2',fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'),command=lambda:get_Digit(2))
btn_2.grid(row=5,column=1,)

btn_3=Button(root,text='3',fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'),command=lambda:get_Digit(3))
btn_3.grid(row=5,column=3,)

btn_add=Button(root,text='+',fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'),command=lambda:get_operation('+'))
btn_add.grid(row=5,column=4,)

btn_plus_minus=Button(root,text='00',fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'),command=lambda:get_Digit('00'))
btn_plus_minus.grid(row=6,column=0,)

btn_Zero=Button(root,text='0',fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'),command=lambda:get_Digit(0))
btn_Zero.grid(row=6,column=1,)

btn_Decimal=Button(root,text='.',fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'),command=lambda:get_Digit('.'))
btn_Decimal.grid(row=6,column=3,)

btn_Equal=Button(root,text='=',fg='white',bg='#666666',width=5,height=1,font=('verdana',20,'bold'),command=get_result)
btn_Equal.grid(row=6,column=4,)



root.mainloop()