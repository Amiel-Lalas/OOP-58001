from tkinter import *

window=Tk()
window.title("Midterms in OOP")
window.geometry("500x300+20+10")
Nm=Label( text="Enter your Full Name :", font=40,fg="green")
Nm.grid(row=3, column=0)
Nm=Label( text="", font=40)
Nm.grid(row=5, column=0)

E1=Entry(window)
E1.grid(row=3, column=1)
def C1():
    E1.insert(0, "")
    L2=Label(LF, text=E1.get())
    L2.pack()
Bttn=Button(window, text="Click to Display Full Name :", font=40, command=C1,fg="red")
Bttn.grid(row=6, column=0)
LF=Label(window)
LF.grid(row=6, column=1)
window.mainloop()