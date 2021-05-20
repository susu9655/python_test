#랜덤하게 나오는 수식 문제 맟추기
import random

#사용자 함수 추가
def make_question():
    a=random.randint(1,9)
    b=random.randint(1,9)
    op=random.randint(1,3)

    #eval을 사용하기위해서 문자열 형태로 수식을 만들어보자
    q=str(a) #첫번째 숫자를 일단은 문자열로 변환
    if op==1:
        q+="+"
    elif op==2:
        q+="-"
    else:
        q+="*"

    #두번째 숫자를 문자열로 변환 후 더한다
    q+=str(b)
    return q
###함수 정의 끝
#총 5번의 수식을 반복해서 맞추기
n1=0 #정답개수
n2=0 #오답개수

for x in range(5):
    q=make_question() #질문 수식을 함수로부터 받기
    print(q)
    ans=input("=") #답 입력받기
    r=int(ans) #입력한 값을 정수로 변환

    #eval("2+3") 결과는 5:수식 계산하는 함수(자바스크립트의 함수와 같다)
    if eval(q)==r:
        print("0 정답!!")
        n1+=1
    else:
        print("X 오답!!!")
        n2+=1

print("모든 문제가 끝났습니다. 결과 발표..")
print("정답 {}개, 오답 {}개.".format(n1,n2))
if n2==0:
    print("당신은 수학의 귀재입니다!!")
if n1==0:
    print("산수 기초부터 공부하세요!!")

