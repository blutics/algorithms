import sys
import array
import math

def fft(x,y):
    n=len(x)
    p=int(math.log(n,2))+1
    x=reverse_bit_order(x)
    for s in range(1,p):
        m=2**s
        if s==1:
            wm=1
            for i in range(p):
                wm=wm*y%786433
        else:
            wm=round(wm**.5)
        for k in range(0,n,m):
            for j in range(m//2):
                x[k+j+m//2]*=wm
                x[k+j+m//2]%=786433
    return sum(x)

def reverse_bit_order(x):
    n=len(x)
    q='%0'+'%d'%(len(bin(n-1))-2)+'d'
    r=[int((q%int(bin(i)[2:]))[::-1],2) for i in range(n)]
    tmp=[]
    for i in r:
        tmp+=x[i],
    return array.array('Q',tmp)
def extension(a):
    n=int(math.log(len(a),2))+1
    a.extend([0 for i in range(2**n-len(a))])
    return a
def oper(a,b):
    return fft(extension(a),b)
def solution(a,b):
    return oper(a,b)%786433

input()
x=array.array('Q',[*map(int,input().split())])
input()
for i in map(int,input().split()):
    print(solution(x,i))
