from tkinter import*
from random import randint

def Rn():
    x=randint(1, 1000) #隨機整數randint(a,b)回傳從 a 到 b 之間的整數
    labl.config(text=x)

window = Tk() 
window.title("test1") 
window.geometry("600x400+300+200") 
window.config(bg = "light blue") 

labl = Label(window, text=">_<", width=10, height=2)
labl.pack()

addbtn = Button(window, text="Generate", command= Rn) # Rn = Random number(亂數)
addbtn.pack()
exitbtn = Button(window, text="exit", command=window.destroy)
exitbtn.pack()

window.mainloop() 