from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def Logout():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")
st =Tk()
st.title("Shutdown App")
st.geometry("500x400")
st.config(bg="Blue")

r_button = Button(st, text="Restart", font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=20,height=40,width=200)

r_button = Button(st, text="Restart Time", font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart_time)
r_button.place(x=150,y=80,height=40,width=200)

r_button = Button(st, text="Log-Out", font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=Logout)
r_button.place(x=150,y=130,height=40,width=200)

r_button = Button(st, text="Shut_Down", font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=shutdown)
r_button.place(x=150,y=190,height=40,width=200)
st.mainloop()