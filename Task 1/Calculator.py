from tkinter import*

def click(event):
    global scvalue
    text=event.widget.cget("text")
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value="Error"

        scvalue.set(value)
        screen.update()

    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root=Tk()
root.geometry("644x900")
root.title("Calculator By Shiya")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f=Frame(root, bg="black")

buttons=[
    'C','/','%','*',
    '9','8','7','-',
    '6','5','4','+',
    '3','2','1','=',
    '0','','.'
]

row_val=1
col_val=0

for button in buttons:
    b=Button(f,text=button, padx=18, pady=18, font="lucida 20 bold")
    b.grid(row=row_val, column=col_val, padx=5, pady=5, sticky=N+S+E+W)
    b.bind("<Button-1>",click)

    if button =='0':
        b.grid(columnspan=2)
    elif button == '=':
        b.grid(row=row_val, rowspan=2)

    col_val+=1
    if col_val>3:
        col_val=0
        row_val+=1

f.pack()
root.mainloop()

