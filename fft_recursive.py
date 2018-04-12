import math
import random

a=[random.randrange(50)for i in range(random.randrange(100))]
b=[random.randrange(50)for i in range(random.randrange(100))]

def extension(a):
    n=int(math.log(len(a),2))+2
    return a+[0]*(2**n-len(a))
def ttf(a,inv):
    n=len(a)
    if n==1:
        return a
    wn=math.exp(1)**(math.pi*1j*2/n*inv)
    w=1
    ye=ttf(a[0::2],inv)
    yo=ttf(a[1::2],inv)
    ya,yb=[],[]
    for i in range(n//2):
        ya+=ye[i]+(w*yo[i]),
        yb+=ye[i]-(w*yo[i]),
        w=w*wn
    return ya+yb
def ittf(a):
    n=len(a)
    return [i/n for i in ttf([*reversed(a)],1)]
def poly(a,b):
    a=extension(a)
    b=extension(b)
    c=ttf(a,1)
    d=ttf(b,1)
    if len(a)>len(b):
        d=d+[0]*(len(a)-len(b))
    else:
        c=c+[0]*(len(b)-len(a))
    e=[c[i]*d[i]for i in range(len(c))]
    n=len(e)
    return [i/n for i in ttf(e,-1)]
