#영단어가 나오면 타이핑해서 따라 쓰기
#총 다섯번을 한 후 초 재기
import random
import time

#단어 리스트
w=["cat","dog","fox","monkey","mouse","panda","javascript","strawberry","python","happyday"]
n=1 #문제 번호
print("[타자 게임]준비가 되면 엔터를 누르고 시작하세요")
input() #엔터만 누르고 변수에 저장은 필요없음

start=time.time() #시작시간 재기
q=random.choice(w)#단어 리스트에서 랜덤으로 한 개를 뽑아서 반환

while n<=5:
    print("*문제 ",n)
    print(q)
    x=input()
    if q==x:
        print("통과!")
        n+=1 #정답인 경우 숫자 증가
        q=random.choice(w) #정답인 경우 다음 문제

    else:
        print("오타!! 다시 도전!!")

#while문 빠져나와서 실행되는 코드
end=time.time()#끝난 시간 기록
et=end-start
et=format(et,".2f")
print("총 타자 시간: ",et,"초")
