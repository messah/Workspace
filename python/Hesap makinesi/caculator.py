from Tkinter import *
#~ import ImageTk
import kod
root = Tk()
root.title("Simple Calculator")

entry = Entry(root, width=33, bg="blue")
entry.grid(row=0, column=0, columnspan=5)
memory=""
def click(key):
    global memory
    if key in "0123456789+-/*().":
        entry.insert(END,key)
        memory = memory + key 

    if key == "=":
        entry.delete(0,END)
        
        result = kaynakkod.infixtopostfix(memory)
        memory = str(result)  
        if result !=1:
            entry.insert(END,memory)
        else:
            entry.insert(END,"yanlis girdi")	
    if key == 'C':
        entry.delete(0, END)  
        memory=""



btn_list = [
'7',  '8',  '9',  '*',  'C',
'4',  '5',  '6',  '/',  '(',
'1',  '2',  '3',  '-',  ')',
'0',  '.',  '=',  '+',  ' ' ]


r = 1
c = 0
for b in btn_list:
    rel = 'ridge'
    cmd = lambda x=b: click(x)
    Button(text=b,width=5,relief=rel,command=cmd).grid(row=r,column=c)
    c += 1
    if c > 4:
        c = 0
        r += 1




mainloop()
