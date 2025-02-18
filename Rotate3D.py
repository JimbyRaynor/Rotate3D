from tkinter import *
import datetime
import math

mainwin = Tk()
mainwin.geometry("600x330")
mainwin.configure(bg="black")


fontmedium = ("Arial",45)
fontsmall = ("Arial",24)
fonttiny = ("Arial",18)

def DoRot_x():
    print(MatrixRot_x(0.3))

def MatrixRot_x(phi):
    return [ [1,0,0],[0,math.cos(phi),-math.sin(phi)],[0,math.sin(phi),math.cos(phi)]]

def MatrixRot_y(phi):
    return [ [math.cos(phi),0,-math.sin(phi)],[0,1,0],[math.sin(phi),0,math.cos(phi)]]

def MatrixRot_z(phi):
    return [ [math.cos(phi),-math.sin(phi),0],[0,math.sin(phi),math.cos(phi)],[0,0,1]]


btnRot_x = Button(mainwin,text="Rotation about x-axis",font=fontsmall,command=DoRot_x, bg="black",fg="orange")
btnRot_x.place(x=400,y=10)

textbox1 = Text(mainwin,width=30,height=6,font=fonttiny,bg="black",fg="orange")
textbox1.place(x=0,y=60)



mainwin.mainloop()