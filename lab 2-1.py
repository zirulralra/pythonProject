#lab 2-1
import turtle #라이브러리를 불러옴.
t = turtle.Turtle()

x = int(input("가로 길이를 입력하세요."))
#input 함수를 이용하여 사용자에게 가로 길이를 입력받는다. (변수 x에 대입)
y = int(input("세로 길이를 입력하세요."))
#input 함수를 이용하여 사용자에게 세로 길이를 입력받는다. (변수 y에 대입)

print("가로의 길이는", x, "세로의 길이는", y, "입니다.")
#print함수를 이용하여 사용자에게 입력받은 길이 값을 보여준다.

t.fd(x) #앞으로 x길이만큼 이동
t.right(90) #오른쪽으로 90도만큼 돌림.
t.fd(y) #앞으로 y길이만큼 이동
t.right(90) #오른쪽으로 90도만큼 돌림.
t.fd(x) #반복함.
t.right(90)
t.fd(y)

turtle.done() #터틀그래픽스 종료.
