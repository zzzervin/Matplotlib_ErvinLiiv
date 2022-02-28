from tkinter import *
from math import *
import matplotlib.pyplot as plt#y=...
import numpy as np #x =[max , min ]
global D,t
D=-1
t=""
T=0



def txt_to_lbl(t:str): 
    t=Arv1.get()
    TX2.configure(text=t)

def discriminant():
    
    a=float(Arv1.get())
    b=float(Arv2.get())
    c=float(Arv3.get())
    if a>0:
        D=b**2-4*a*c
        TX2.configure(text=f"D={D}")
        if D>0:
            X1=(-b+D**0.5)/(2*a)
            X2=(-b-D**0.5)/(2*a)
            TX2.configure(text=f"D={D}\n x1={X1}\n x2={X2}")
            graf=True
        elif D==0:
            X1=-b/(2*a)
            TX2.configure(text=f"1 корня={D}\n x1,2={X1}")
            graf=True
        else:
             TX2.configure(text=f"корня нет= D= {D}")
             graf=False
    
    return D,t,graf

def graafik():
    D,t,graf=discriminant()
    if graf==True:
        a=float(Arv1.get())
        b=float(Arv2.get())
        c=float(Arv3.get())
        x0=(-b)/(2*a)
        y0=a*x0*x0+b*x0+c
        x1= np.arange(x0-10,x0+10, 0.5)#Диапозон
        y1=a*x1*x1+b*x1+c
        fig = plt.figure()
        plt.plot(x1,y1,"r-d")
        plt.title("квадратного уравнения")
        plt.ylabel("y")
        plt.xlabel("x")
        plt.grid(True)
        plt.show()
        text=f"Вершина порабулы({x0},{x0})"
    else:
        text=f"Графика нет "
    TX2.configure(text=f"D={D}\n {t}\n {text}")
    
def veel() :
    global T 
    if T==0:
        akkan.geometry(str(akkan.winfo_width())+"x"+str(akkan.winfo_width()+50))
        btn_veel.config(text="Уменьшить окно")
        T=1
    else:
        akkan.geometry(str(akkan.winfo_width())+"x"+str(akkan.winfo_width()-500))
        btn_veel.config(text="Увеличеть окно")
        T=0

def figura():
    valik=var.get()
    if valik==1:
        glass()
    elif valik==2:
        liblikas()
    elif valik==3:
        vihmavari()

def glass():
        x1 = np.arange(-9, -0.5 , 0.5)#min max step
        y1=(-1/16)*(x1+5)**2 +2       
        x2 = np.arange(1, 9.5, 0.5)
        y2=(-1/16)*(x2-5)**2 +2        
        x3 = np.arange(-9, -0.5 , 0.5)
        y3= (1/4)*(x3+5)**2 -3
        x4 = np.arange(1, 9.5 , 0.5)
        y4= (1/4)* (x4-5)** 2 -3
        x5 = np.arange(-9, -5.5 , 0.5)
        y5= у = -(x5+7)** 2 +5
        x6 = np.arange(6, 9.5 , 0.5)
        y6= -(x6-7)** 2 +5
        x7 = np.arange(-1, 1.5, 0.5)
        y7= -0.5*x7**2+1.5

        plt.plot(x1, y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
        plt.title('очки')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()

def liblikas():
    x1 = np.arange(-9, -0.5, 0.5)
    y1=-(1/8)*(x1+9)**2+8
    x2 = np.arange(1, 9.5, 0.5)#
    y2=-(1/8)*(x2-9)**2+8
    x3 = np.arange(-9, -7.5, 0.5)
    y3=7*(x3+8)**2+1
    x4 = np.arange(8, 9.5, 0.5)
    y4=7*(x4-8)**2+1
    x5 = np.arange(-8, -0.5, 0.5)
    y5=1/49*(x5+1)**2
    x6 = np.arange(1, 8.5, 0.5)
    y6=1/49*(x6-1)**2
    x7 = np.arange(-8, -0.5, 0.5)
    y7=-4/49*(x7+1)**2
    x8=np.arange(1, 8.5, 0.5)
    y8=-4/49*(x8-1)**2
    x9=np.arange(-8, -1.5, 0.5)
    y9=1/3*(x9+5)**2-7
    x10=np.arange(2, 8.5, 0.5)
    y10=1/3*(x10-5)**2-7
    x11=np.arange(-2, -0.5, 0.5)
    y11=-2*(x11+1)**2-2
    x12=np.arange(1, 2.5, 0.5)
    y12=-2*(x12-1)**2-2
    x13=np.arange(-1, 1.5, 0.5)
    y13=-4*x13**2+2
    x14=np.arange(-1, 1.5, 0.5)
    y14=4*x14**2-6
    x15=np.arange(-2, 0.5, 0.5)
    y15=-1.5*x15+2
    x16=np.arange(0, 2.5, 0.5)
    y16=1.5*x16+2
    fig = plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13,x14,y14,x15,y15,x16,y16)
    plt.title('Бабочка')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

def vihmavari():
    x1=np.arange(-12, 12.5, 0.5)
    y1=(-1/18)*x1*x1+12
    x2=np.arange(-4, 4.5, 0.5)
    y2=(-1/8)*x2*x2+6
    x3=np.arange(-12, -3.5, 0.5)
    y3=(-1/8)*(x3+8)**2+6
    x4=np.arange(4, 12.5, 0.5)
    y4=(-1/8)*(x4-8)**2+6
    x5=np.arange(-4, -0.3, 0.5)
    y5=2*(x5+3)**2-9
    x6=np.arange(-4, 0.2, 0.5)
    y6=1.5*(x6+3)**2-10
    fig=plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
    plt.title('')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()



akkan=Tk()# главное окно приложения
akkan.title("Kвадратного уравнения")
akkan.geometry("900x375")
f1=Frame(akkan,width=900,height=300,bg="blue")
f1.place(x=0,y=0)
f2=Frame(akkan,width=900,height=600,bg="yellow")
f2.place(x=0,y=300)



TX=Label(f1,text="Решение квадратного уравнения",height=1,font="Arial 20",bg="lightblue",fg="green")
TX2=Label(f1,text="Решение",height=4,width=60,font="Arial 10",bg="orange")
TX3=Label(f1,text="x**2+",font="Arial 20",fg="green")
TX4=Label(f1,text="x+",font="Arial 20",fg="green")
TX5=Label(f1,text="=0",font="Arial 20",fg="green")


Arv1=Entry(f1,width=5,font="Arial 20",bg="lightblue",justify=CENTER)
Arv2=Entry(f1,width=5,font="Arial 20",bg="lightblue",justify=CENTER)
Arv3=Entry(f1,width=5,font="Arial 20",bg="lightblue",justify=CENTER)

BT=Button(f1,text="Решить",height=2,width=10,font="Arial 20",bg="green",command=discriminant)
#BT.bind("<Button-1>",discriminant)
BT2=Button(f1,text="График",height=2,width=10,font="Arial 20",bg="green",command=graafik)

var=IntVar()
btn_veel=Button(f2,text="Увеличеть окно", font="Calibri 26", bg="green",command=veel)

r1=Radiobutton(f2,text="очки",variable=var,value=1,font="Calibri 26",command=figura)#command=figura
r2=Radiobutton(f2,text="бабочка",variable=var,value=2,font="Calibri 26",command=figura)
r3=Radiobutton(f2,text="зонтик",variable=var,value=3,font="Calibri 26",command=figura)


TX5.place(x=390,y=130)
TX4.place(x=250,y=130)
TX3.place(x=80,y=130)
    #############
TX2.place(x=150,y=230)
    #############
TX.place(x=100,y=0)


BT2.place(x=640,y=100)
BT.place(x=440,y=100)
btn_veel.place(x=260,y=0)

r1.place(x=360,y=200)
r2.place(x=360,y=300)
r3.place(x=360,y=400)

Arv1.place(x=0,y=130)
Arv2.place(x=160,y=130)
Arv3.place(x=300,y=130)

akkan.mainloop()

