from tkinter import *
from PIL import Image,ImageTk
def func():
    pass
root=Tk()
root.title("SMART INDIA HACKATHON")
root.geometry("1350x800")
root.minsize(1350,800)
root.iconbitmap("q.ico.ico")
root.wm_attributes("-transparentcolor", 'grey')
img=Image.open("govern.jpg")
img=img.resize((1370,700))
photo=ImageTk.PhotoImage(img)
canvas=Canvas(root,width=1400,height=700)
canvas.create_image(0,0,image=photo,anchor="nw")
canvas.pack()
lbl2 = Label(root,text="SEARCH  SCHOOLS  BY", font=('calibri', 25, 'bold'),foreground='red')
lbl2.place(x=550,y=40)
lbl2 = Label(root,text="STATE", font=('calibri', 25, 'bold'),foreground='black')
lbl2.place(x=350,y=140)
lbl2 = Label(root,text="DISTRICT", font=('calibri', 25, 'bold'),foreground='black')
lbl2.place(x=340,y=240)
lbl2 = Label(root,text="BLOCK", font=('calibri', 25, 'bold'),foreground='black')
lbl2.place(x=350,y=340)
Button(root,text="SEARCH",command=func,font="comicsansms 20 bold",bg="red").place(x=590,y=460)
svar=StringVar()
pvar=StringVar()
scidvar=StringVar()
a=Entry(root,textvariable=svar,font="courier 20 bold",selectborderwidth=4)
a.place(x=700,y=145)
a.focus_force()
b=Entry(root,textvariable=pvar,font="courier 20 bold")
b.place(x=700,y=250)
c=Entry(root,textvariable=scidvar,font="courier 20 bold")
c.place(x=700,y=345)
root.mainloop()