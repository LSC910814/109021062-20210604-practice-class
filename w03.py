from tkinter import*
import random

def Rn():
    x,x1,x2,x3,x4,x5=random.sample(range(1, 42),6) #整數中選擇一系列樣本(範圍,回傳長度),非重置抽樣 
    labl1.config(text=x)
    labl2.config(text=x1)
    labl3.config(text=x2)
    labl4.config(text=x3)
    labl5.config(text=x4)
    labl6.config(text=x5)
    

window = Tk() 
window.title("test1") 
window.geometry("600x400+300+200") 
window.config(bg = "light blue") 

labl1 = Label(window, text=">_<", width=10, height=2)
labl1.pack()
labl2 = Label(window, text=">_<", width=10, height=2)
labl2.pack()
labl3 = Label(window, text=">_<", width=10, height=2)
labl3.pack()
labl4 = Label(window, text=">_<", width=10, height=2)
labl4.pack()
labl5 = Label(window, text=">_<", width=10, height=2)
labl5.pack()
labl6 = Label(window, text=">_<", width=10, height=2)
labl6.pack()

addbtn = Button(window, text="Generate", command= Rn) # Rn = Random number(亂數)
addbtn.pack()
exitbtn = Button(window, text="exit", command=window.destroy)
exitbtn.pack()

window.mainloop() 