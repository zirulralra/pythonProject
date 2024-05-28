#lab 4-2
import turtle as t
# 여러분이 사용할 함수입니다.
def draw_circle(circle_color, circle_radius): #원을 그려주는 함수
    t.pendown()
    t.fillcolor(circle_color)
    t.begin_fill()
    t.circle(circle_radius)
    t.end_fill()
    t.penup()
colorList = ["red", "yellow", "blue", "purple"]
# 여러분의 코드를 여기에 넣으세요.


#유저에게 색깔 리스트를 입력받는다. (처음에는 정수 형태)
User = int(input('color : [ 1)red 2)yellow 3)blue 4)purple ] Ex) 4213 : '))
#정수 형태로 입력받았으므로 리스트에 인덱스하여 넣기 위해 문자열 변환
User = str(User)

#유저가 입력한 색깔을 저장할 빈 리스트 생성.
U_List = []

#문자열 리스트를 인덱싱한 후 정수로 변환하고 1을 빼줌. (리스트 순서에 맞게)
#그리고 순차적으로 리스트에 추가한다.
U_List.append(int(User[0])-1)
U_List.append(int(User[1])-1)
U_List.append(int(User[2])-1)
U_List.append(int(User[3])-1)

#사용자에게 반지름값을 입력받는다.
Radius = int(input('radius : '))


#입력받은 반지름만큼 오른쪽으로 이동해가며
#함수를 이용해 원을 그린다.
draw_circle(colorList[U_List[0]],Radius)
t.setpos(Radius, 0)
draw_circle(colorList[U_List[1]],Radius)
t.setpos(Radius * 2,0)
draw_circle(colorList[U_List[2]],Radius)
t.setpos(Radius * 3,0)
draw_circle(colorList[U_List[3]],Radius)

t.exitonclick()