import random

def fst_m_exp(down,top,modular):
    x=bin(top)[2:][::-1]
    y=[0 for i in range(len(x))]
    y[0]=down
    result=1
    for i in range(1,len(x)):
        y[i]=y[i-1]**2%modular
    for i in range(len(x)):
        if x[i]=='1':
            result*=y[i]
    return result%modular


def test_fe(down,top,modular):
    a=fst_m_exp(down,top,modular)
    b=down**top%modular
    print('down    : %d'%down)
    print('top     : %d'%top)
    print('modular : %d'%modular)
    print('result of fst_m_exp : %d'%a)
    print('result of origin  : %d'%b)
    print('result ==> %s'%('right' if a==b else 'wrong'),end='\n\n')
    return a==b

s=0
for i in range(1000):
    if test_fe(random.randrange(30),random.randrange(30),random.randrange(1,30))==1:
        s+=1
print('%d/1000'%s)
