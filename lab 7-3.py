#lab 7-3
import turtle as t

def graph(): #좌표평면을 그린다.
    t.goto(-300,0)
    t.fd(600)
    t.back(300)
    t.goto(0, -300)
    t.goto(0,300)
    t.up()

def find_y(x): #x맞는 y값을 구함.
    y = (x ** 2 + 1)/100
    y = int(y)
    return y

graph()
t.down()
t.speed(0.5)

for i in range(150): #150번 반복함.
    t.goto(i, find_y(i))
    t.circle(0.3)

t.done()