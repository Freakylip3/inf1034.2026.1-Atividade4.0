from turtle import *
from time import sleep 


t = Turtle()
t.speed(0)

def soma_2 (x):
    return x + 2

def raiz(x):
    return x**0.5 

def divisao(x):
    return 1/x

def quadrado(x):
    return 2**x

#Plano cartesiano

def plano_cartesiano(X, Y, TAMANHO, x, y, tamanho):
    t.pu()
    t.goto(X, Y)
    t.pd()
    t.lt(90)
    t.fd(TAMANHO)
    t.stamp()
    t.pu()
    t.goto(x, y)
    t.pd()
    t.rt(90)
    t.fd(tamanho)
    t.stamp()


#função afim simples

#t.color('black')
#plano_cartesiano(0, -500, 900, -500, 0, 970)

#t.color('cyan')
#t.pu()
#t.goto(-200, soma_2(-200))
#t.pd()
#for x in range(-99, 101):
#    t.goto(x*2, soma_2(x*2))
#sleep(2)
#t.clear() 

#função - y = √x

t.color('black')
plano_cartesiano(0, -500, 900, -500, 0, 970)



t.color('red')
t.pu()
t.goto(0, 0)
t.pd()
for x in range(1, 201):
    t.goto(x*2, raiz(x*2))
sleep(2)
t.clear()

#função 1/x

t.color('black')
plano_cartesiano(0, -500, 900, -500, 0, 970)

t.color('purple')
#esq
t.pu()
x= -300
y= divisao(x/50) * 10
t.goto(x, y)
t.pd()
for x in range(-299, 0 ):
    y = divisao(x/50) * 10
    t.goto(x, y)

#dir
t.pu()
x= 1
y= divisao(x/50) *10
t.goto(x,y)
t.pd()
for x in range(2, 301):
    y= divisao(x/50) * 10
    t.goto(x,y)
sleep(2)
t.clear



#função 2^x

t.color('black')
plano_cartesiano(0, -500, 900, -500, 0, 970)


t.color('pink')
t.pu()
t.goto(0, 0)
t.pd()
for x in range(2, 201):
    t.goto(2*x, quadrado(2*x))
sleep(2)














mainloop()