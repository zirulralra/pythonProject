#lab 7-4
import turtle
temp = 0
def tree(length):
    global temp
    print(length)
    if length>5:
        t.fd(length)
        t.rt(20)
        tree(length-15)
        t.lt(40)
        tree(length-15)
        t.rt(20)
        t.backward(length)
    temp += 1
print(temp)
t = turtle.Turtle()
t.left(90)
t.color("green")
t.speed(1)
tree(50)