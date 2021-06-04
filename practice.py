from tkinter import * # import* 元件....  tk 開放原始碼(open source)

def setLabText(): #建立函式 更改標籤內文字
    labl.config(text="hello")

window = Tk() # 建立空白視窗
window.title("First Python Window") # 視窗title
window.geometry("600x400+100+50") # 指定視窗所在位置(+位移量x,y)
window.config(bg = "#ccddff") # 背景顏色 

labl = Label(window, text =">_<", width =12, height =3, bg ="#ccfddd") #標籤(寬,高(數字兼不能太大))
labl.pack() #打包至視窗容器裡

btn1 = Button(window, text="change", command=setLabText) # 按鈕按下改變字 (command後面為函式名稱)
btn1.pack() #打包至視窗容器裡

btnExit = Button(window, text="Leave", command=window.destroy) # 按鈕按下會離開 
btnExit.pack() #打包至視窗容器裡

window.mainloop() # 顯示