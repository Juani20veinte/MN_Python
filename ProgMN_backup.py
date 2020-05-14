from tkinter import *
from sympy import *
import numpy

main= Tk()
main.title("Metodos numericos-Equipo 1")
main.iconbitmap("icondragon.ico")
main.geometry("1050x570+100+100")
main.resizable(False,False)
main.configure(background='firebrick')
logouvm  = PhotoImage(file="lelogue.gif")
logouvm=logouvm.subsample(4,4)
labeluvm = Label(main, image=logouvm,bg='#E2E2E2')
labeluvm.place(relwidth=1.0,relheight=1.0)
labeluvm.pack(side= LEFT, anchor= W,padx=20,pady=2,fill='both')

#Funciones
def restaurar3():
	global labelmm
	global labelTM
	entradaF.delete(0,END)
	entradaC.delete(0,END)
	labelmatriz.grid_forget()
	entradaM.grid_forget()
	botonsig.grid_forget()
	labelmm.grid_forget()
	labelTM.grid_forget()
	labelResultadomatriz.grid_forget()
	labelResultadovector.grid_forget()
	labelresultadogauss.grid_forget()

def restaurar2():
	entrada2_1.delete(0,END)
	entrada2_2.delete(0,END)
	entrada2_3.delete(0,END)
	Text2_1.grid_forget()
	Scroll2_1.grid_forget()
	label2_R.grid_forget()

def volvermain1():
	primerframe.pack_forget()
	mainframe.pack()
	volverbutton.place_forget()

def volvermain2():
	restaurar2()
	segundoframe.pack_forget()
	mainframe.pack()
	volverbutton.place_forget()

def volvermain3():
	restaurar3()
	tercerframe.pack_forget()
	mainframe.pack()
	volverbutton.place_forget()

def ventaanayuda():
    vgj = Toplevel(main)
    vgj.title("Ayuda: como poner una funcion")
    vgj.configure(background="dark slate gray")
    vgj.resizable(False, False)
    labelA_1 = Label(vgj,text="Como poner una ecuacion\n*Suma +\n*Resta - \n*Multiplicacion *\n*Division /\n*Multiplicar variables: 2x -> 2*x\n*Exponentes: x^n -> x**n\n*La constante matemática 'e': e^-x -> exp(-x)",bg="dark slate gray",fg="white", font=("Berlin Sans FB", 15))
    labelA_1.grid(row=0, column = 0)
    btnA_1= Button(vgj,text= "Salir",bg="white",fg="Black",command= vgj.destroy, font=("Berlin Sans FB", 15))
    btnA_1.grid(row=1, column = 0)

def fbiseccion():
	volverbutton.configure(command= volvermain1)
	mainframe.pack_forget()
	primerframe.pack()
	volverbutton.place(x=70,y=450)

def fnr():
	volverbutton.configure(command= volvermain2)
	mainframe.pack_forget()
	segundoframe.pack()
	volverbutton.place(x=70,y=450)

def fgj():
	volverbutton.configure(command= volvermain3)
	mainframe.pack_forget()
	tercerframe.pack()
	volverbutton.place(x=70,y=450)

def calcularmatriz():
	global matrix
	labelmm.configure(text= matrix, font=("Berlin Sans FB", 20))
	labelmm.grid(row=4,column=0,columnspan=2)
	labelResultadovector.configure(text=vector, font=("Berlin Sans FB", 20))
	labelResultadovector.grid(row=5,column=0,columnspan=2,pady=10)
	entradaF.delete(0,END)
	entradaC.delete(0,END)
	labelmatriz.grid_forget()
	entradaM.grid_forget()
	botonsig.grid_forget()
	labelTM.grid_forget()

	for k in range(0,m):
		for f in range(k+1,m):
			factor=(matrix[f,k]/matrix[k,k])
			vector[f]=vector[f]-(factor*vector[k])
			for c in range(0,n):
				matrix[f,c]=matrix[f,c]-(factor*matrix[k,c])

	x[m-1]=vector[m-1]/matrix[m-1,m-1]
	for f in range(m-2,-1,-1):
		suma = 0
		for c in range(0,n):
			suma=suma+matrix[f,c]*x[c]
		x[f]=(vector[f]-suma)/matrix[f,f]

	labelResultadomatriz.configure(text= "Resultado de las Variables:", font=("Berlin Sans FB", 20))
	labelResultadomatriz.grid(row=6,column=0,columnspan=2,pady=10)
	labelresultadogauss.configure(text= x, font=("Berlin Sans FB", 20))
	labelresultadogauss.grid(row=7,column=0,columnspan=2,pady=10)





def sig():
	global f
	global c
	global m
	global n
	global matrix
	global vector

	if(f == m and c == n):
		botonsig.configure(text="Listo",command=calcularmatriz)
		entradaM.delete(0,END)
		entradaM.configure(state=DISABLED)
	else:
		if(c < n):
			matrix[(f),(c)]= float(entradaM.get())
			c = c + 1
		else:
			vector[(f)]= float(entradaM.get())
			f = f + 1
			if(f < m):
				c = 0
		if(f == m and c == n):
			botonsig.configure(text="Listo",command=calcularmatriz)
			entradaM.delete(0,END)
			entradaM.configure(state=DISABLED)
		else:
			if(c == n):
				labelmatriz.configure(text="Resultado No."+str(f+1)+":  ")
			else:
				labelmatriz.configure(text="Valor Posicion:["+str(f+1)+","+str(c+1)+"] ")
		entradaM.delete(0,END)

def fmatriz():
	global f 
	global c
	global m
	global n
	global x
	global matrix
	global vector
	f = 0
	c = 0
	botonsig.configure(text="Siguiente",command=sig, font=("Berlin Sans FB", 15))
	labelmatriz.configure(text="Valor Posicion:[1,1] ", font=("Berlin Sans FB", 15))
	entradaM.configure(state=NORMAL)
	m = int(entradaF.get())
	n = int(entradaC.get())
	matrix = numpy.zeros((m,n))
	vector = numpy.zeros((n))
	x = numpy.zeros((m))
	labelTM.grid(row=1,column=2,columnspan=2,padx=10)
	labelmatriz.grid(row=2,column=2)
	entradaM.grid(row=2,column=3)
	botonsig.grid(row=3, column=3)

def ptm(n):
    x = Symbol('x')
    ys = eval(expresion)
    c = diff(ys).subs(x,n)
    return(c)

def poli(x):
    y = eval(expresion)
    return(y)

def fnewtonraphson():
	global expresion
	expresion = (entrada2_1.get())
	x = int(entrada2_2.get())
	erroru= float(entrada2_3.get())
	vec=[]
	vec.insert(0,0)
	i = 0
	error= 1
	textos2 = ""
	while abs(error) > erroru:
	    x1 = x-(poli(x)/ptm(x))
	    x1 = round(x1,10)
	    vec.append(x1)
	    i = i + 1
	    x = x1
	    error=(vec[i]-vec[i-1])/vec[i]
	    textos2 = textos2 +"x" + str(i) + ": "
	    textos2 = textos2 + "{0:.6f}".format(round(x,6)) + "\n "

	Text2_1.delete('1.0', END)
	Text2_1.configure(width= 50, height = 5)
	Text2_1.grid(row=5,column=0,columnspan=2,pady=10)
	Text2_1.insert(INSERT,textos2)
	Scroll2_1.grid(row=5,column=2,sticky="nsew")
	label2_R.grid(row=6,column=0,columnspan=2,pady=10)
	label2_R.configure(text= " Resultado Final: {0:.6f}".format(round(x,6)))

#Mainframe
volverimage = PhotoImage(file="cubitotrukistrukis.gif")
volverimage=volverimage.subsample(4,4)
volverbutton = Button(main,image=volverimage,bg='#E2E2E2')

mainframe = Frame(main)
mainframe.pack()
mainframe.configure(background='firebrick', width= 1050, height =560)

etiqueta1=Label(mainframe,text="KUKULCAN-MN",bg="firebrick",fg="white")

etiqueta1.config(font=("Berlin Sans FB", 32))
etiqueta1.grid(row=0,column=0, columnspan=3,pady=20)

Biseccion= PhotoImage(file="btn1.gif")
BotonBiseccion= Button(mainframe,image=Biseccion,bg='firebrick',text="Gauss-Jordan",fg="white", command = fbiseccion)
BotonBiseccion.grid(row=1,column=0,padx=10)

Bohemia= PhotoImage(file="btn2.gif")
BotonBiseccion= Button(mainframe,image=Bohemia,bg='firebrick',command = fnr)
BotonBiseccion.grid(row=1,column=1,padx=10)

Gaussito= PhotoImage(file="btn3.gif")
BotonBiseccion= Button(mainframe,image=Gaussito,bg='firebrick',command = fgj)
BotonBiseccion.grid(row=1,column=2,padx=10,pady= 10)

kuku= PhotoImage(file="gugu.gif")
kuku=kuku.subsample(4,4)
labelkuku = Label(mainframe,image=kuku,bg='firebrick')
labelkuku.grid(row=2,column=2,sticky="e")

labelcopyright = Label(mainframe,text="Copyright. © 2020 KUKULCAN-MN. Todos los derechos reservados a: Fuentes Leon Juan Angel, Arias Diaz Ian, Hernandez Martines David, Ramirez Romero David.",bg="firebrick",fg="white", font=("Berlin Sans FB", 7))
labelcopyright.grid(row=2,column=0,columnspan=3, sticky= "sw")

#primerframe
primerframe = Frame(main)
primerframe.configure(background='blue', width= 1050, height =560)

#segundoframe
segundoframe = Frame(main)
segundoframe.configure(background='firebrick', width= 1050, height =560)
label2_0 = Label(segundoframe,text="Método de Newton-Raphson",bg="firebrick",fg="white", font=("Berlin Sans FB", 25))
label2_0.grid(row=0,column=0,pady=10,columnspan =2)
label2_1 = Label(segundoframe,text="Coloque funcion en terminos de x: ",bg="firebrick",fg="white", font=("Berlin Sans FB", 15))
label2_1.grid(row=1,column=0,pady=10)
label2_2= Label(segundoframe,text="Introduce el valor de inicio(x0): ",bg="firebrick",fg="white", font=("Berlin Sans FB", 15))
label2_2.grid(row=2,column=0,pady=10)
label2_3 = Label(segundoframe,text="Introduce el error : ",bg="firebrick",fg="white", font=("Berlin Sans FB", 15))
label2_3.grid(row=3,column=0,pady=10)
entrada2_1 = Entry(segundoframe, justify= CENTER, font=("Berlin Sans FB", 15),width=20)
entrada2_1.grid(row=1,column=1)
entrada2_2 = Entry(segundoframe, justify= CENTER, font=("Berlin Sans FB", 15),width=20)
entrada2_2.grid(row=2,column=1)
entrada2_3 = Entry(segundoframe, justify= CENTER, font=("Berlin Sans FB", 15),width=20)
entrada2_3.grid(row=3,column=1)
Boton2_1 = Button(segundoframe, bg='white',text= "Como poner una funcion",command = ventaanayuda, font=("Berlin Sans FB", 15))
Boton2_1.grid(row=4,column=0,pady=20)
Boton2_2 = Button(segundoframe, bg='white',text= "Calcular",command = fnewtonraphson, font=("Berlin Sans FB", 15))
Boton2_2.grid(row=4,column=1,pady=20)

Text2_1 = Text(segundoframe,fg="red", font=("Berlin Sans FB", 15))
Scroll2_1 = Scrollbar(segundoframe, command=Text2_1.yview)
label2_R = Label(segundoframe,bg="firebrick",fg="white", font=("Berlin Sans FB", 25))

#tercerframe
tercerframe = Frame(main)
tercerframe.configure(background='firebrick', width= 1050, height =560)
label3_0 = Label(tercerframe,text="Método de Gauss-Jordan",bg="firebrick",fg="white", font=("Berlin Sans FB", 25))
label3_0.grid(row=0,column=0,columnspan =4,pady=10)
labelfila = Label(tercerframe,text="Valor de la Fila: ",bg="firebrick",fg="white", font=("Berlin Sans FB", 15))
labelfila.grid(row=1,column=0,pady=10)
entradaF = Entry(tercerframe, justify= CENTER, font=("Berlin Sans FB", 15),width=10)
entradaF.grid(row=1,column=1)
labelcolumna = Label(tercerframe,text="Valor de la Columna: ",bg="firebrick",fg="white", font=("Berlin Sans FB", 15))
labelcolumna.grid(row=2,column=0)
entradaC = Entry(tercerframe, justify= CENTER, font=("Berlin Sans FB", 15),width=10)
entradaC.grid(row=2,column=1)
BotonMatriz = Button(tercerframe, bg='white',text= "Hacer Matriz",command = fmatriz, font=("Berlin Sans FB", 15))
BotonMatriz.grid(row=3,column=0,columnspan=2,pady=20)
labelmatriz = Label(tercerframe,bg="firebrick",fg="white")
labelTM = Label(tercerframe,text="Introduce los valores de la matriz y el vector solución",bg="firebrick",fg="white", font=("Berlin Sans FB", 15))
botonsig = Button(tercerframe,bg="white", text="Siguiente",command = sig)
entradaM = Entry(tercerframe, justify= CENTER, font=("Berlin Sans FB", 15),width=10)
labelmm = Label(tercerframe, bg="firebrick",fg="white")
labelResultadomatriz = Label(tercerframe, bg="firebrick",fg="white")
labelResultadovector = Label(tercerframe, bg="firebrick",fg="white")
labelresultadogauss = Label(tercerframe, bg="firebrick",fg="white")

main.mainloop()