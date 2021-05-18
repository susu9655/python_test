import userdef #외부 파이썬 파일 가져오기
#사용자 정의 함수 만들기
def plus(x,y):
    #print(x,"+",y,"=",x+y)
    print("{} 더하기 {} 는 {} 입니다!!".format(x,y,x+y)) #format을 이용한 출력

def info(a, b, c):
        print("안녕하세요 ", a, "님~")
        print(a, "님의 학교는 ", b, "입니다.")
        print("전공은 ", c, "입니다")
        print("*" * 50)


#사용자 함수 호출하기
plus(5,4)
plus(100,200)
info("강호동","홍익대","작곡과")
info("유미리","서울대","미술과")

print("총 세번의 점수를 입력하세요")
for sc in range(3):
    sc=input("당신의 점수를 입력하세요")
    sc=int(sc)
    g=userdef.score(sc)
    print(sc,"점수는 ",g,"학점입니다.")