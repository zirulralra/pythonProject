#lab 5-3
import turtle
import os

t = turtle.Turtle() #필요한 라이브러리를 불러옴.

x = int(input("x 좌표를 입력하세요 : ")) #사용자에게 입력받음.
y = int(input("y 좌표를 입력하세요 : "))

Count = 0
if abs((x-0)) and abs((y-0)) <= 100: #중심점과 x좌표와 y좌표의 차가 둘 다 100 이하이면 범위 안에 속한다고 간주한다.
    Count += 1
if abs((x-100)) and abs((y-0)) <= 100 :
    Count += 1
if abs((x - 50)) and abs((y - 100)) <= 100:
    Count += 1

print("(%.2f, %.2f)를 포함하는 원은 %d개 있습니다."%(x, y, Count)) #출력해준다.

t.up() #거북이 그림을 그림.
t.goto(0,-100) #시작점을 중심으로 한 바퀴 위로 돌기 때문에 y좌표 -100이 시작점이 된다.
t.down()
t.circle(100)
t.up()
t.goto(100,-100)
t.down()
t.circle(100)
t.up()
t.goto(50,0)
t.down()
t.circle(100)
t.up()
t.goto(x,y)
os.system("pause")