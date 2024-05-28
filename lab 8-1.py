import random #라이브러리를 불러옴.

capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbol = ['!', '@', '#', '$', '%']
number = '0123456789'

capital_list = [] #빈 리스트 생성
for x in range(len(capital)): #문자열 형태를 리스트 형식으로 바꿔준다.
    capital_list += capital[x]

number_list = [] #위와 같은 과정
for y in range(len(number)):
    number_list += number[y]

for p in range(10): #10개 생성
    Password_list = [] #비밀번호를 저장할 빈 리스트 생성
    for i in range(12): #열 두 번 랜덤으로 추가한다
        Password_list.append(random.choice(capital_list+small+symbol+number_list))

    i=0
    password = ''
    for i in range(12): #문자열로 바꿔서 출력해준다.
        password += Password_list[i]

    print(password)
