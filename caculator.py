from tkinter import*
import math
import tkinter.messagebox

root= Tk()
root.title('Scientific calculator')
root.config(bg= 'blue')
root.resizable(width= False, height= False)
root. geometry("510x620+0+0")

calci= Frame(root)
calci.grid()

class Calci():
    def __init__(self):
        self.total=0
        self.current=""
        self.input_value=True
        self.check_sum=False
        self.op=""
        self.result=False

    def numENTER(self, num):
        self.result= False
        Firstnum=display.get()
        secondnum= str(num)   
        if self.input_value:
            self.current= secondnum
            self.input_value= False
        else:
            if secondnum == '.':
                if secondnum in Firstnum:
                    return
            self.current= Firstnum+secondnum 
        self.display(self.current)

    def totalsum(self):
        self.result = True
        self.current= float(self.current)
        if self.check_sum==True:
            self.valid_func()
        else:
            self.total= float(display.get())       

    def display(self, val):
           display.delete(0, END) 
           display.insert(0, val)

    def valid_func(self):
        if self.op =="add":
            self.total +=self.current
        if self.op =="sub":
            self.total -=self.current    
        if self.op =="multiplication":
            self.total *=self.current 
        if self.op =="divide":
            self.total /=self.current 
        if self.op =="mod":
            self.total %=self.current 
        self.input_value= True
        self.check_sum= False
        self.display(self.total)   

    def operation(self, op):
        self.current= float(self.current) 
        if self.check_sum:
            self.valid_func()
        elif not self.result:
            self.total= self.current
            self.input_value= True
        self.check_sum= True
        self.op= op
        self.result= False  

    def clr(self):
        ex = display.get()
        ex = ex[0:len(ex) - 1]  # 78
        display.delete(0, END)
        display.insert(0, ex)
        return
            
    def allclr(self):
        display.delete(0, END)

    def PM(self):
        self.result  = False
        self.current = -(float(display.get()))
        self.display(self.current)

    def sqr(self):
        self.result  = False
        self.current = math.sqrt(float(display.get()))
        self.display(self.current)

    def pi(self):
        self.result  = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result  = False
        self.current = math.tau
        self.display(self.current) 

    def e(self):
        self.result  = False
        self.current = math.e
        self.display(self.current) 

    def cos(self):
        self.result= False
        self.current= math.cos(math.radians(float(display.get()))) 
        self.display(self.current) 

    def cosh(self):
        self.result= False
        self.current= math.cosh(math.radians(float(display.get()))) 
        self.display(self.current) 

    def sin(self):
        self.result= False
        self.current= math.sin(math.radians(float(display.get()))) 
        self.display(self.current)

    def sinh(self):
        self.result= False
        self.current= math.sinh(math.radians(float(display.get()))) 
        self.display(self.current)

    def tan(self):
        self.result= False
        self.current= math.tan(math.radians(float(display.get()))) 
        self.display(self.current)

    def tanh(self):
        self.result= False
        self.current= math.tanh(math.radians(float(display.get()))) 
        self.display(self.current) 

    def log(self):
        self.result  = False
        self.current = math.log(float(display.get()))
        self.display(self.current) 

    def Exp(self):
        self.result  = False
        self.current = math.exp(float(display.get()))
        self.display(self.current)

    def mod(self):
        self.result  = False
        self.current = math.modf(float(display.get()))
        self.display(self.current)
        
    def acosh(self):
        self.result  = False
        self.current = math.acosh(float(display.get()))
        self.display(self.current)

    def asinh(self):
        self.result  = False
        self.current = math.asinh(float(display.get()))
        self.display(self.current) 

    def log2(self):
        self.result  = False
        self.current = math.log2(float(display.get()))
        self.display(self.current)       

    def log1p(self):
        self.result  = False
        self.current = math.log1p(float(display.get()))
        self.display(self.current)

    def log10(self):
        self.result  = False
        self.current = math.log10(float(display.get()))
        self.display(self.current)

    def degree(self):
        self.result  = False
        self.current = math.degrees(float(display.get()))
        self.display(self.current) 
    def lgama(self):
        self.result  = False
        self.current = math.lgamma(float(display.get()))
        self.display(self.current)

    def Exp1(self):
        self.result  = False
        self.current = math.expm1(float(display.get()))
        self.display(self.current)          

add_val= Calci()           
display= Entry(calci, font=('arial', 20, 'bold'), bg= "blue", bd=25, width=30, justify= RIGHT )
display.grid(row=0, column=0, columnspan=4, pady=1)
display.insert(0, "0")
 

number= "789456123"
i=0
buton=[]
for j in range(2,5):
    for k in range(3):
        buton.append(Button(calci, width=6, height=2, font=('arial', 23, 'bold'), bd=4, text=number[i]))
        buton[i].grid(row= j, column= k, pady= 1)
        buton[i]["command"]=lambda X= number[i]: add_val.numENTER(X)
        i=i+1

#=============+++++++++++++++++++++++++++BUTTON+++++++++++++++++++=============#
btnclr= Button(calci, text= chr(67),  width=6, height=2, font=('arial', 23, 'bold'), bd=4,
                bg= "powder blue", command= add_val.clr).grid(row=1, column=0, pady=1)      

btnAllclr=Button(calci, text= chr(67)+chr(69),  width=6,height=2, font=('arial', 23, 'bold'), bd=4,
                  bg= "powder blue", command= add_val.allclr).grid(row=1, column=1, pady=1)  

btnSQ= Button(calci, text= "√",  width=6, height=2, font=('arial', 23, 'bold'), bd=4,
                bg= "powder blue",command= add_val.sqr).grid(row=1, column=2, pady=1)
btnADD= Button(calci, text="+",  width=6, height=2, font=('arial', 23, 'bold'), bd=4,
                bg= "powder blue", command=lambda: add_val.operation("add")).grid(row=1, column=3, pady=1)      

btnSUB= Button(calci, text="-",  width=6, height=2, font=('arial', 23, 'bold'), bd=4,
                bg= "powder blue",  command=lambda: add_val.operation("sub")).grid(row=2, column=3, pady=1)       

btnMUL= Button(calci, text='*',  width=6, height=2, font=('arial', 23, 'bold'), bd=4,
                bg= "powder blue",  command=lambda: add_val.operation("multiplication")).grid(row=3, column=3, pady=1)      

btnDIV= Button(calci, text= '/',  width=6, height=2, font=('arial', 23, 'bold'), bd=4,
                bg= "powder blue",  command=lambda: add_val.operation("divide")).grid(row=4, column=3, pady=1) 

btnEQl= Button(calci, text="=",  width=6, height=2, font=('arial', 23, 'bold'), bd=4,
                bg= "powder blue",command= add_val.totalsum).grid(row=5, column=0, pady=1)      

btnDOT= Button(calci, text=".",  width=6, height=2, font=('arial', 23, 'bold'), bd=4,
                bg= "powder blue",command=lambda: add_val.numENTER(".")).grid(row=5, column=1, pady=1)       

btnPLS_MINS= Button(calci, text= chr(177),  width=6, height=2, font=('arial', 23, 'bold'), bd=4,
                bg= "powder blue", command= add_val.PM).grid(row=5, column=2, pady=1)      

btnzero= Button(calci, text= '0',  width=6, height=2, font=('arial', 23, 'bold'), bd=4,
                bg= "powder blue", command=lambda: add_val.numENTER(0) ).grid(row=5, column=3, pady=1)
     

#=============++++++++++++++++++++++++Scientific Function+++++++++++++++++++=============#
btnclr= Button(calci, text= chr(67),  width=6, height=2, font=('arial', 23, 'bold'), bd=4,
                bg= "powder blue", command= add_val.clr).grid(row=1, column=0, pady=1) 
     

btnAllclr=Button(calci, text= chr(67)+chr(69),  width=6, height=2, font=('arial', 23, 'bold'), bd=4,
                  bg= "powder blue", command= add_val.allclr).grid(row=1, column=1, pady=1)  

btnSQ= Button(calci, text= "√",  width=6, height=2, font=('arial', 23, 'bold'), bd=4,
                bg= "powder blue",command= add_val.sqr).grid(row=1, column=2, pady=1)
btnADD= Button(calci, text="+",  width=6, height=2, font=('arial', 23, 'bold'), bd=4,
                bg= "powder blue",  command=lambda: add_val.operation("add")).grid(row=1, column=3, pady=1)      

btnSUB= Button(calci, text="-",  width=6, height=2, font=('arial', 23, 'bold'), bd=4,
                bg= "powder blue", command=lambda: add_val.operation("sub")).grid(row=2, column=3, pady=1)       

btnMUL= Button(calci, text='*',  width=6, height=2, font=('arial', 23, 'bold'), bd=4,
                bg= "powder blue",  command=lambda: add_val.operation("multiplication")).grid(row=3, column=3, pady=1)      

btnDIV= Button(calci, text= '/',  width=6, height=2, font=('arial', 23, 'bold'), bd=4,
                bg= "powder blue",  command=lambda: add_val.operation("divide")).grid(row=4, column=3, pady=1) 

btnEQl= Button(calci, text="=",  width=6, height=2, font=('arial', 23, 'bold'), bd=4,
                bg= "powder blue", command= add_val.totalsum).grid(row=5, column=0, pady=1)      

btnDOT= Button(calci, text=".",  width=6, height=2, font=('arial', 23, 'bold'), bd=4,
                bg= "powder blue", command=lambda: add_val.numENTER(".")).grid(row=5, column=1, pady=1)       

btnPLS_MINS= Button(calci, text= chr(177),  width=6, height=2, font=('arial', 23, 'bold'), bd=4,
                bg= "powder blue", command= add_val.PM).grid(row=5, column=2, pady=1)      

btnzero= Button(calci, text= '0',  width=6, height=2, font=('arial', 23, 'bold'), bd=4,
                bg= "powder blue", command=lambda: add_val.numENTER(0)).grid(row=5, column=3, pady=1)       
                                             
#=============+++++++++++++++++++++++++++BUTTON+++++++++++++++++++=============#
btnPI= Button(calci, text="π",  width=6, height=2, font=('arial', 22, 'bold'), bd=4,
                bg= "powder blue", command = add_val.pi).grid(row=1, column=4, pady=1)      

btnCOS=Button(calci, text="cos",  width=6, height=2, font=('arial', 22, 'bold'), bd=4,
                command= add_val.cos).grid(row=1, column=5, pady=1)  

btntan= Button(calci, text= "tan",  width=6, height=2, font=('arial', 22, 'bold'), bd=4,
                command= add_val.tan).grid(row=1, column=6, pady=1)
btnsin= Button(calci, text="sin",  width=6, height=2, font=('arial', 22, 'bold'), bd=4,
                command= add_val.sin).grid(row=1, column=7, pady=1)             



btn2pi= Button(calci, text='2π',  width=6, height=2, font=('arial', 22, 'bold'), bd=4,
                bg= "powder blue", command = add_val.tau).grid(row=2, column=4, pady=1)      

btncosh= Button(calci, text= 'cosh',  width=6, height=2, font=('arial', 22, 'bold'), bd=4,
                bg= "powder blue", command= add_val.cosh).grid(row=2, column=5, pady=1) 

btntanh= Button(calci, text="tanh",  width=6, height=2, font=('arial', 22, 'bold'), bd=4,
                bg= "powder blue",command= add_val.tanh).grid(row=2, column=6, pady=1)      

btnsinh= Button(calci, text="sinh",  width=6, height=2, font=('arial', 22, 'bold'), bd=4,
                bg= "powder blue", command= add_val.sinh).grid(row=2, column=7, pady=1)  


btnLOG= Button(calci, text="log",  width=6, height=2, font=('arial', 22, 'bold'), bd=4,
             bg= "powder blue", command= add_val.log).grid(row=3, column=4, pady=1)      

btnEX= Button(calci, text= 'EXP',  width=6, height=2, font=('arial', 22, 'bold'), bd=4,
                command= add_val.Exp).grid(row=3, column=5, pady=1) 

btnMOD= Button(calci, text="MOD",  width=6, height=2, font=('arial', 22, 'bold'), bd=4,
                command=lambda: add_val.operation("mod")).grid(row=3, column=6, pady=1)

btnE= Button(calci, text="e",  width=6, height=2, font=('arial', 22, 'bold'), bd=4,
                command = add_val.e).grid(row=3, column=7, pady=1)


btnlog2= Button(calci, text="log2",  width=6, height=2, font=('arial', 22, 'bold'), bd=4,
                bg= "powder blue", command= add_val.log2).grid(row=4, column=4, pady=1)      

btnDEG= Button(calci, text= 'deg',  width=6, height=2, font=('arial', 22, 'bold'), bd=4,
                command= add_val.degree).grid(row=4, column=5, pady=1) 

btnAcosh= Button(calci, text="acosh",  width=6, height=2, font=('arial', 22, 'bold'), bd=4,
                command= add_val.acosh).grid(row=4, column=6, pady=1)

btnAsinh= Button(calci, text="asinh",  width=6, height=2, font=('arial', 22, 'bold'), bd=4,
                command= add_val.asinh).grid(row=4, column=7, pady=1)  


btnLOG10= Button(calci, text="log10",  width=6, height=2, font=('arial', 22, 'bold'), bd=4,
                bg= "powder blue",command=add_val.log10).grid(row=5, column=4, pady=1)      

btnLOG1p= Button(calci, text= 'log1p',  width=6, height=2, font=('arial', 22, 'bold'), bd=4,
                bg= "powder blue",command= add_val.log1p).grid(row=5, column=5, pady=1) 

btnEXMP= Button(calci, text="expm1",  width=6, height=2, font=('arial', 22, 'bold'), bd=4,
                bg= "powder blue",command=add_val.Exp1).grid(row=5, column=6, pady=1)

btnlgamma= Button(calci, text="lgamma",  width=6, height=2, font=('arial', 22, 'bold'), bd=4,
                bg= "powder blue",command= add_val.lgama).grid(row=5, column=7, pady=1)

LBldisplay= Label(calci, text="Scientific caculator", font=('arial', 22, 'bold'), justify= CENTER)
LBldisplay.grid(row=0, column=4, columnspan=4)


#========== ++++++++++++++++++++MENU & FUNCTION+++++++++++++++++++++++++++======#
def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific caculator", "Do you want to Exit")
    if iExit > 0:
        root.destroy()
        return

def Scientific():
    root.resizable(width= False, height= False)
    root.geometry('1000x620+0+0')

def Standard():  
    root.resizable(width= False, height= False)
    root.geometry("510x620+0+0")  

menubar= Menu(calci)
fliename= Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fliename)
fliename.add_command(label="Standard", command= Standard)
fliename.add_command(label="Scientific", command=Scientific)
fliename.add_separator()
fliename.add_command(label="EXIT", command=iExit)

root.config(menu=menubar)
root.mainloop()