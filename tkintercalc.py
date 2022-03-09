'''Calculator that performs addition,
subtraction, division and multiplication 
on two values at a time
'''
from tkinter import *


root = Tk()
root.title("*Simple Calculator*")

entries = Entry(root, width = 40, borderwidth=5)
entries.grid(row=0,column=0,columnspan=3, padx = 10, pady = 10)


#functions
#division
def btn_division():
    first_number = entries.get()
    global f_num
    global operation
    operation = "division"
    f_num = int(first_number)
    entries.delete(0, END)

#multiplication
def btn_multiply():
    first_number = entries.get()
    global f_num
    global operation
    operation = "multiplication"
    f_num = int(first_number)
    entries.delete(0, END)

#subtraction
def btn_subtract():
    first_number = entries.get()
    global f_num
    global operation
    operation = "subtraction"
    f_num = int(first_number)
    entries.delete(0, END)

#display answer
def btn_ans():
    second_number = entries.get()
    entries.delete(0,END)
    global s_num
    s_num = int(second_number)

    if(operation == "addition"):
        entries.insert(0,f_num + s_num)
    elif(operation =="subtraction"):
        entries.insert(0,f_num - s_num)
    elif(operation == "multiplication"):
        entries.insert(0,f_num * s_num)
    elif(operation == "division"):
        if(s_num == 0):
            entries.insert(0, "DIVISION BY ZERO:ERROR")
        else:
            entries.insert(0,f_num / s_num)

#addition
def btn_sum():
    first_number = entries.get()
    global f_num
    global operation
    operation = "addition"
    f_num = int(first_number)
    entries.delete(0, END)


#clear the screen
def btn_clr():
    entries.delete(0,END)
    
#display numbers on click
def btn_add(num):
    current = entries.get()
    entries.delete(0, END)
    entries.insert(0, str(current)+str(num))



#buttons in the calc.
btn_1 = Button(root,text = '1', padx = 40,pady = 20, command =lambda: btn_add(1))
btn_2 = Button(root,text = '2', padx = 40,pady = 20, command =lambda: btn_add(2))
btn_3 = Button(root,text = '3', padx = 40,pady = 20, command =lambda: btn_add(3))
btn_4 = Button(root,text = '4', padx = 40,pady = 20, command =lambda: btn_add(4))
btn_5 = Button(root,text = '5', padx = 40,pady = 20, command =lambda: btn_add(5))
btn_6 = Button(root,text = '6', padx = 40,pady = 20, command =lambda: btn_add(6))
btn_7 = Button(root,text = '7', padx = 40,pady = 20, command =lambda: btn_add(7))
btn_8 = Button(root,text = '8', padx = 40,pady = 20, command =lambda: btn_add(8))
btn_9 = Button(root,text = '9', padx = 40,pady = 20, command =lambda: btn_add(9))
btn_0 = Button(root,text = '0', padx = 40,pady = 20, command =lambda: btn_add(0))


btn_sum = Button(root,text = '+', padx = 39,pady = 20, command =btn_sum)
btn_equal = Button(root,text = '=', padx = 140,pady = 20, command =btn_ans)
btn_clear = Button(root,text = 'C', padx = 39,pady = 20, command =btn_clr)
btn_div = Button(root,text = '/', padx = 40,pady = 20, command =btn_division)
btn_sub = Button(root,text = '-', padx = 40,pady = 20, command =btn_subtract)
btn_prod = Button(root,text = '*', padx = 40,pady = 20, command =btn_multiply)

#buttons to the screen
btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)
btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)
btn_0.grid(row=4, column=0)

btn_sum.grid(row=4, column=1)
btn_equal.grid(row=6, column=0,columnspan=3)
btn_clear.grid(row=5, column=0)

btn_div.grid(row=5, column=1)
btn_sub.grid(row=4, column=2)
btn_prod.grid(row=5, column=2)



root.mainloop()

