from tkinter import *
def click(event):
     global str
     text=event.widget.cget("text")
     #print(text)
     if text=="=":
         if str.get().isdigit():
             value=int(str.get())
         else:
             value=eval(ans.get())

         str.set(value)
         ans.update()

     elif text == "Clear":
         str.set("")
         ans.update()
     else:
         str.set(str.get()+text)
         ans.update()


root=Tk()
root.title("Calculator")
root.wm_iconbitmap("")

str= StringVar()
str.set("")

f1=Frame(root,width=265,height=320,bg="grey")
f1.pack()

# lbl1=Label(f1,width=35)
ans=Entry(f1,width=35,textvariable=str)
# lbl1.place(x=10,y=10)
ans.place(x=10,y=10)

b1=Button(f1,text="1",bg="red",padx=15,pady=7)
b1.place(x=10,y=40)
b1.bind("<Button-1>",click)

b2=Button(f1,text="2",bg="red",padx=15,pady=7)
b2.place(x=75,y=40)
b2.bind("<Button-1>",click)

b3=Button(f1,text="3",bg="red",padx=15,pady=7)
b3.place(x=140,y=40)
b3.bind("<Button-1>",click)

b4=Button(f1,text="4",bg="red",padx=15,pady=7)
b4.place(x=10,y=95)
b4.bind("<Button-1>",click)

b5=Button(f1,text="5",bg="red",padx=15,pady=7)
b5.place(x=75,y=95)
b5.bind("<Button-1>",click)

b6=Button(f1,text="6",bg="red",padx=15,pady=7)
b6.place(x=140,y=95)
b6.bind("<Button-1>",click)


b7=Button(f1,text="7",bg="red",padx=15,pady=7)
b7.place(x=10,y=150)
b7.bind("<Button-1>",click)

b8=Button(f1,text="8",bg="red",padx=15,pady=7)
b8.place(x=75,y=150)
b8.bind("<Button-1>",click)

b9=Button(f1,text="9",bg="red",padx=15,pady=7)
b9.place(x=140,y=150)
b9.bind("<Button-1>",click)

b10=Button(f1,text="*",bg="red",padx=15,pady=7)
b10.place(x=205,y=40)
b10.bind("<Button-1>",click)

b11=Button(f1,text="-",bg="red",padx=15,pady=7)
b11.place(x=205,y=95)
b11.bind("<Button-1>",click)

b12=Button(f1,text="+",bg="red",padx=13,pady=7)
b12.place(x=205,y=150)
b12.bind("<Button-1>",click)

b13=Button(f1,text="/",bg="red",padx=15,pady=7)
b13.place(x=205,y=205)
b13.bind("<Button-1>",click)

b14=Button(f1,text="0",bg="red",padx=15,pady=7)
b14.place(x=10,y=205)
b14.bind("<Button-1>",click)

b15=Button(f1,text="Clear",bg="red",padx=5,pady=7)
b15.place(x=75,y=205)
b15.bind("<Button-1>",click)

b16=Button(f1,text="=",bg="red",padx=14,pady=7)
b16.place(x=140,y=205)
b16.bind("<Button-1>",click)

b17=Button(f1,text=".",bg="red",padx=16,pady=7)
b17.place(x=110,y=260)
b17.bind("<Button-1>",click)

root.mainloop()



