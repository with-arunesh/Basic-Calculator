import tkinter
from tkinter import *
from tkinter import messagebox

val=''

def btn_1_isclicked():
              global val
              val=val+'1'
              data.set(val)

def btn_2_isclicked():
              global val
              val=val+'2'
              data.set(val)

def btn_3_isclicked():
              global val
              val=val+'3'
              data.set(val)

def btn_4_isclicked():
              global val
              val=val+'4'
              data.set(val)

def btn_5_isclicked():
              global val
              val=val+'5'
              data.set(val)

def btn_6_isclicked():
              global val
              val=val+'6'
              data.set(val)

def btn_7_isclicked():
              global val
              val=val+'7'
              data.set(val)

def btn_8_isclicked():
              global val
              val=val+'8'
              data.set(val)

def btn_9_isclicked():
              global val
              val=val+'9'
              data.set(val)

def btn_0_isclicked():
              global val
              val=val+'0'
              data.set(val)

def btn_00_isclicked():
              global val
              val=val+'00'
              data.set(val)

A=0.0
operator=''
def btn_plus_clicked():
              global A
              global operator
              global val
              A=float(val) or int(val)
              operator='+'
              val=val+'+'
              data.set(val)

def btn_sub_clicked():
              global A
              global operator
              global val
              A=float(val) or int(val)
              operator='-'
              val=val+'-'
              data.set(val)

def btn_mul_clicked():
              global A
              global operator
              global val
              A=float(val) or int(val)
              operator='*'
              val=val+'*'
              data.set(val)

def btn_dot_clicked():
              global A
              global operator
              global val
              A=float(val)
              operator='.'
              val=val+'.'
              data.set(val)

def btn_div_clicked():
              global A
              global operator
              global val
              A=float(val) or int(val)
              operator='÷'
              val=val+'÷'
              data.set(val)

def btn_by_clicked():
              global A
              global operator
              global val
              A=float(val) or int(val)
              operator='/'
              val=val+'/'
              data.set(val)

def btn_percentage_clicked():
              global A
              global operator
              global val
              A=float(val) or int(val)
              operator='%'
              val=val+'%'
              data.set(val)

def btn_c_clicked():
              global A
              global operator
              global val
              A=0
              operator=''
              val=''
              data.set(val)

def btn_back_space_clicked():
              global A
              global operator
              global val
              A=0
              operator='⌫'
              val=val[0:len(val)-1]
              data.set(val)

def btn_power_clicked():
              global A
              global operator
              global val
              A=float(val)
              operator='^'
              val=val+'^'
              data.set(val)

def btn_root_clicked():
              global A
              global operator
              global val
              A=float(val)
              operator='√'
              val=val+'√'
              data.set(val)

def btn_factorial_clicked():
              global A
              global operator
              global val
              A=float(val)
              operator='!'
              val=val+'!'
              data.set(val)

def btn_equal_clicked():
              global A
              global operator
              global val
              val2=val
              if operator=='+':
                            x=int((val2.split('+')[1]))
                            C=A+x
                            data.set(C)
                            val=str(C)
              elif operator=='-':
                            x=int((val2.split('-')[1]))
                            C=A-x
                            data.set(C)
                            val=str(C)
              elif operator=='*':
                            x=int((val2.split('*')[1]))
                            C=A*x
                            data.set(C)
                            val=str(C)
              elif operator=='÷':
                            x=int((val2.split('÷')[1]))
                            if x==0:
                                          messagebox.showerror('Error','Division by 0 not Supported')
                                          val=''
                                          A=''
                                          data.set(val)
                            else:
                                          C=A//x
                                          data.set(C)
                                          val=str(C)
              elif operator=='/':
                            x=int((val2.split('/')[1]))
                            if x==0:
                                          messagebox.showerror('Error','Division by 0 not Supported')
                                          val=''
                                          A=''
                                          data.set(val)
                            else:
                                          C=A/x
                                          data.set(C)
                                          val=str(C)
              elif operator=='.':
                            x=int((val2.split('.')[1]))
                            C=A+0.0
                            data.set(C)
                            val=str(C)

              elif operator=='%':
                            x=int((val2.split('%')[1]))
                            C=(A*x)/100
                            data.set(C)
                            val=str(C)
              
              elif operator=='^':
                            x=float((val2.split('^')[1]))
                            C=A**x
                            data.set(C)
                            val=str(C)

              elif operator=='√':
                            x=float((val2.split('√')[1]))
                            y=1/A
                            C=x**y
                            data.set(C)
                            val=str(C)
              
              elif operator=='!':
                            x = lambda num : 1 if num <= 1 else num*x(num-1)
                            C=x(A)
                            data.set(C)
                            val=str(C)

root=tkinter.Tk()
root.geometry('350x500+400+400')
# root.resizable(0,0)
root.title("Calculator")

data=StringVar()

lbl=Label(
              root,
              text='Label',
              anchor=SE,
              font=('verdana',20),
              textvariable=data,
              background='#ffffff',
              fg='#000000'
)
lbl.pack(expand=True,fill='both')

btnrow1=Frame(root,bg='#000000')
btnrow1.pack(expand=True,fill='both')

btnrow2=Frame(root)
btnrow2.pack(expand=True,fill='both')

btnrow3=Frame(root)
btnrow3.pack(expand=True,fill='both')

btnrow4=Frame(root)
btnrow4.pack(expand=True,fill='both')

btnrow5=Frame(root)
btnrow5.pack(expand=True,fill='both')

btnrow6=Frame(root)
btnrow6.pack(expand=True,fill='both')

btn1=Button(
              btnrow4,
              text='1',
              font= ('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_1_isclicked,
)
btn1.pack(side=LEFT,expand=True,fill='both')

btn2=Button(
              btnrow4,
              text='2',
              font=('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_2_isclicked,
)
btn2.pack(side=LEFT,expand=True,fill='both')

btn3=Button(
              btnrow4,
              text='3',
              font=('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_3_isclicked,
)
btn3.pack(side=LEFT,expand=True,fill='both')

btn_add=Button(
              btnrow4,
              text='+',
              font=('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_plus_clicked
)
btn_add.pack(side=LEFT,expand=True,fill='both')

btn4=Button(
              btnrow3,
              text='4',
              font= ('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_4_isclicked,
)
btn4.pack(side=LEFT,expand=True,fill='both')

btn5=Button(
              btnrow3,
              text='5',
              font=('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_5_isclicked,
)
btn5.pack(side=LEFT,expand=True,fill='both')

btn6=Button(
              btnrow3,
              text='6',
              font=('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_6_isclicked,
)
btn6.pack(side=LEFT,expand=True,fill='both')

btn_sub=Button(
              btnrow3,
              text='-',
              font=('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_sub_clicked
)
btn_sub.pack(side=LEFT,expand=True,fill='both')

btn7=Button(
              btnrow2,
              text='7',
              font= ('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_7_isclicked,
)
btn7.pack(side=LEFT,expand=True,fill='both')

btn8=Button(
              btnrow2,
              text='8',
              font=('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_8_isclicked,
)
btn8.pack(side=LEFT,expand=True,fill='both')

btn9=Button(
              btnrow2,
              text='9',
              font=('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_9_isclicked,
)
btn9.pack(side=LEFT,expand=True,fill='both')

btn_mul=Button(
              btnrow2,
              text='*',
              font=('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_mul_clicked
)
btn_mul.pack(side=LEFT,expand=True,fill='both')

btn_c=Button(
              btnrow1,
              text='C',
              font= ('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_c_clicked
)
btn_c.pack(side=LEFT,expand=True,fill='both')

btn_parcentage=Button(
              btnrow1,
              text='%',
              font=('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_percentage_clicked,
)
btn_parcentage.pack(side=LEFT,expand=True,fill='both')

btn_backspace=Button(
              btnrow1,
              text='⌫',
              font=('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_back_space_clicked
)
btn_backspace.pack(side=LEFT,expand=True,fill='both')



btn_div=Button(
              btnrow1,
              text='÷',
              font=('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_div_clicked
)
btn_div.pack(side=LEFT,expand=True,fill='both')

btn_00=Button(
              btnrow5,
              text='00',
              font=('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_00_isclicked,
)
btn_00.pack(side=LEFT,expand=True,fill='both')

btn_0=Button(
              btnrow5,
              text='0',
              font=('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_0_isclicked,
)
btn_0.pack(side=LEFT,expand=True,fill='both')

btn_dot=Button(
              btnrow5,
              text='.',
              font=('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_dot_clicked,

)
btn_dot.pack(side=LEFT,expand=True,fill='both')

btn_equal=Button(
              btnrow5,
              text='=',
              font=('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_equal_clicked,
)
btn_equal.pack(side=LEFT,expand=True,fill='both')

btn_power=Button(
              btnrow6,
              text='^',
              font=('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_power_clicked,
)
btn_power.pack(side=LEFT,expand=True,fill='both')

btn_root=Button(
              btnrow6,
              text='√',
              font=('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_root_clicked,
)
btn_root.pack(side=LEFT,expand=True,fill='both')

btn_by=Button(
              btnrow6,
              text='/',
              font=('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_by_clicked,
)
btn_by.pack(side=LEFT,expand=True,fill='both')

btn_factorial=Button(
              btnrow6,
              text='!',
              font=('verdana',22),
              relief=GROOVE,
              border=0,
              command=btn_factorial_clicked,
)
btn_factorial.pack(side=LEFT,expand=True,fill='both')

root.mainloop()