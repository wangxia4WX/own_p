"""包含了P+语言的所有语法，是程序的主体

"""
import sys
variable = {}
def out(fun, sep=' ', end='\n', file=sys.stdout, flush=False):
    if fun[0:3] == "out" and fun [3:4] == " ":
        fun = fun[4:]
        d = variable.get(fun,None)    
        if d is not None:
            print(d)
        elif d is None:
            print(fun)        
        
def s(fun):
    if fun[0:1]== "s" and fun[1:2] ==" ":
        fun = fun[2:]
        fun = int(fun)
        print(abs(fun))
def inp(fun):
    if fun[0:3] == "inp" and fun[4:5] == " ":
        fun = fun[5:]
        if fun == "" or fun == " ":
            input()
        else:
            input(fun)
def var(fun):
    global i
    i = 0
    if fun[0:3] == "var" and fun[3:4] == " ":
        fun = fun[4:]
        a = fun.index(" ")
        k = fun[:a]
        j = fun[a+1:]
        try:
            b = float(j)
            c = int(j)
            if b == c:
                j = c
            else:
                j = b
        except:
            j = j
        variable[k] = j