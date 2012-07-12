class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

   
import string   
def infixtopostfix(infixexpr):
    prec = {}
    prec["/"] = 3
    prec["*"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    
    opstack = Stack()
    postfixlist = []
    
    if control(infixexpr):
        tokenlist = token_ayirma(infixexpr)
        
    else:
        print "hatali ifade"
        return 1
    
    for token in tokenlist:
       
        if isFloat(token):
            postfixlist.append(token)
            
        elif token == '(':
            opstack.push(token)
            
        elif token == ')':
            toptoken = opstack.pop()
            
            while toptoken != '(':
                postfixlist.append(toptoken)
                toptoken = opstack.pop()
        
        else:
            while (not opstack.isEmpty()) and \
                  (prec[opstack.peek()] >= prec[token]):
                    postfixlist.append(opstack.pop())
            opstack.push(token)
     
    while not opstack.isEmpty():
        postfixlist.append(opstack.pop())
    x=string.join(postfixlist)

    return postfixeval(x)
    
       
def postfixeval(postfixexpr):
    operandstack = Stack()
    tokenlist =postfixexpr.split()
    
    for token in tokenlist:
        if isFloat(token):
            operandstack.push(float(token))
            
        else:
            operand2 = operandstack.pop()
            operand1 = operandstack.pop()
            result = domath(token,operand1,operand2)
            operandstack.push(result)

    return operandstack.pop()

def domath(op,op1,op2):
    if op == "*":
        return op1 * op2
    
    else:
        if op == "/":
            return op1 / op2
        
        else:
            if op == "+":
                return op1 + op2
            
            else:
                return op1 - op2

def token_ayirma(s):
    yeni=""
    news=[]
    i=0
    op="-+*/()"
    
    while i<len(s):

        try:
            if s[i] in "0123456789":
                while s[i] not in op:
                    yeni=yeni+s[i]
                    i=i+1
                news.append(yeni)

            else:
                if s[i] in op:
                    news.append(s[i])  
                    i=i+1
   
        except IndexError:
            news.append(yeni)    
        yeni=""
        
    return news  


def control(s):
    balanced=True
    sayi="0123456789()"
    op="+-*/"
    k=0
    t=0
    
    for i in range(len(s)):
    
           
                if not s[0] in sayi:
                    balanced=False
                      
                else:
                    if s[i] in op and s[i-1] in op  :
                        balanced=False
                        break

                    elif s[len(s)-1] in op:
                        balanced=False
                    
                    elif s[i] == " " :
						s[i].split()
                        
                    else:
                        balanced=True
                
    return balanced   

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

from Tkinter import *
#~ import ImageTk
#~ import kod
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
        
        result = infixtopostfix(memory)
        memory = str(result)  
        if result !=1:
            entry.insert(END,memory)
        else:
            entry.insert(END,"yanlis girdi")	
    if key == 'C':
        entry.delete(0, END)  
        memory=""
       
    #~ if key == ' ':
		#~ entry.insert(END,key)
		#~ memory=memory + key    



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
