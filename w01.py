from tkinter import * # import* 元件....  tk 開放原始碼(open source)

x1=0
def increase():
    global x1 #宣告全域變數
    x1 = x1+1
    labl.config(text=int(x1))

def decrease():
    global x1
    x1= x1-1
    labl.config(text=int(x1))

window = Tk() # 建立空白視窗
window.title("test1") # 視窗title
window.geometry("600x400+300+200") # 指定視窗所在位置(+位移量x,y)
window.config(bg = "light blue") # 背景顏色 

labl = Label(window, text=int(x1), width=10, height=2) #標籤
labl.pack()

addbtn = Button(window, text="add", command=increase) # 按鈕按下增加數值 (command後面為函式名稱)
addbtn.pack()
subbtn = Button(window, text="sub", command=decrease)
subbtn.pack()
exitbtn = Button(window, text="exit", command=window.destroy)
exitbtn.pack()

window.mainloop() # 顯示