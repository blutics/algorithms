import collections
import timeit
import random
def sortsTime():
    a=[ ("버블",bubbleSort),
        ("선택",selectionSort),
        ("퀵" ,quickSort),
        ("삽입",insertionSort),
        ("병합",mergeSort) ]
    for i in a:
        print("%s정렬입니다"%i[0])
        sortTimelab(i[1],size=10000,num=10000)
        print("\n")

def sortTimelab(f,size=300,num=1000):
    print("정렬 알고리즘 시간측정을 시작하겟습니다.")
    x=[random.randrange(num) for i in range(size)]
    start=timeit.default_timer()
    x=f(x)
    end=timeit.default_timer()
    print("랩타임 : %d초 입니다."%(end-start))
def vSort(f):
    vlist=[]
    for i in range(1):
        x=[random.randrange(1000) for i in range(300)]
        print("문제 : %s"%x)
        print("예상 : %s"%sorted(x))
        print("결과 : %s"%f(x))
        if sorted(x)==f(x):
            a="참"
        else:
            a="거짓"
        print("판정 : %s"%(a),end="\n\n")
        vlist+=a,
    print(vlist)
def sTest(f):
    x=[random.randrange(100) for i in range(20)]
    print("문제 : %s\n결과 : %s"%(x,f(x)))
def swap(x,i,j):
    x[i],x[j]=x[j],x[i]
def selectionSort(x):
    for i in range(len(x)):
        y=i
        for j in range(i+1,len(x)):
            if x[y]>x[j]:y=j
        swap(x,i,y)
    return x
def insertionSort(x):
    for i in range(1,len(x)):
        for j in range(i+1):
            if x[i]>x[i-j]:
                x=x[:i-j+1]+x[i:i+1]+x[i-j+1:]
                x.pop(i+1)
                break
    return x
def bubbleSort(x):
    k=len(x)
    for i in range(k):
        for j in range(k-i-1):
            if x[j]>x[j+1]:swap(x,j,j+1)
    return x
def pivot(x,left,right):
    a,b=left,right
    if a>b:
        return
    pidx=left
    while left<right:
        while x[pidx]<=x[right] and right!=pidx:
            right-=1
        while x[pidx]>=x[left] and left!=pidx:
            left+=1
        pidx=(left,right)[left==pidx]
        swap(x,left,right)
        pvalue=x[pidx]
    pivot(x,a,pidx-1)
    pivot(x,pidx+1,b)
def pTest(x):
    for i in range(x):
        y=[random.randrange(300) for i in range(20)]
        print(y)
        print(pivot(y,0,19),end="\n\n")
def quickSort(x):
    pivot(x,0,len(x)-1)
    return x
def mergeSort(x):
    length=len(x)
    a=x[:len(x)//2]
    b=x[len(x)//2:]
    c=[]
    if len(a)>1:
        a=mergeSort(a)
    if len(b)>1:
        b=mergeSort(b)
    while len(a)!=0 and len(b)!=0:
        if a[0]<b[0]:
            c+=a.pop(0),
        else:
            c+=b.pop(0),
    if len(a)==0:
        c+=b
    else:
        c+=a
    return c
