#lab 4-3
import random #라이브러리를 불러옴.
characters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"

#패스워드를 저장할 빈 리스트 생성.
Password = []

#5번 반복한다.
for x in range(5) :
    Random = random.randint(0,1) #알파벳, 숫자 중 어떤 것을 리스트에 추가할지 결정.
    if Random == 0 : #랜덤 숫자가 0이면 알파벳을 추가
        Password.append(random.choice(characters)) #함수를 이용하여 리스트의 아무 알파벳을 불러와서 추가함.
    else : #랜덤 숫자가 1이면 숫자를 추가
        Password.append(random.choice(digits)) #함수를 이용하여 리스트의 아무 숫자를 불러와서 추가함.

#문자열 형태로 출력하기 위해 인덱스 번호에 따라 문자로 변환. (이후에 합쳐서 문자열이 된다.)
Str_Password = str(Password[0])+str(Password[1])+str(Password[2])+str(Password[3])+str(Password[4])

#랜덤 비밀번호를 출력함.
print ("Password : ", Str_Password)