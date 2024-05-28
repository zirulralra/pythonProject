#lab 8-2
dic = {}
while True : #엔터가 눌리기 전 까지 반복
    name = input("Enter your name: ") #이름을 입력받음.
    if name == '':
        break #엔터가 눌리면 반복문 탈출
    phone_call = input("Enter your phone call: ") #전화번호를 입력받음
    dic[name] = phone_call #사전에 추가해준다.


while True : #검색을 시작한다.
    Guess = input("이름 입력 : ") #Guess에 이름 저장
    Ph = dic.get(Guess) #밸류값을 찾아서 ph에 저장
    print(Ph) #출력해준다.
    if Guess == '': #엔터가 눌리면 탈출
        break


