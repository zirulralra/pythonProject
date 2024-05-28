#lab 2-2
Name = input("이름을 입력하세요.") #이름을 Name변수에 입력받는다. (한글이므로 문자열형태로 저장.)
ID = int(input("학번을 입력하세요.")) #학번을 ID변수에 입력받는다. (숫자이므로 정수형태로 저장.)
Hobby = input("취미를 입력하세요.") #취미를 Hobby변수에 입력받는다.
Introduce = input("자기소개 하세요.") #자기소개를 Introduce변수에 입력받는다.

print("저의 이름은", Name, "입니다.") #print함수를 이용하여 출력함.
print("저의 학번은", ID, "입니다.")
print("저의 취미는", Hobby, "입니다.")
print(Introduce) #자기소개만 출력하므로 다른 문자열은 출력할 필요없음.
