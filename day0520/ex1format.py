#fomat 출력 양식
from locale import format
#
# print(format(4.12345,'8.3f')) #총 8자리에 소수점 3자리
# print(format(1234567,'20d'))  #정수 출력인데 총 20칸(앞 부분이 공백으로 처리)
# print(format(123456789,'3,d')) #정수출력, 3자리마다 컴마찍기
# """
# %기호 (자바나 c언어와 같다)
# %f:실수, %d:정수, %s:문자열, %c:단일 문자
# """
#
# num1=10
# num2=20
# print('%d+%d=%d' %(num1,num2,(num1+num2))) #변수 바인딩
# score=98
# name="홍길동"
# print('%s 님의 수학점수는 %d점 입니다'%(name,score))

a="파이썬"
b="자바"
c="안드로이드"

print('a={} 재밌어요!, b={} 어려워요, c={} 공부하고 싶어요!'.format(a,b,c))

d=123.456
e=456.7890
print('d=[{0:20.10f}],e=[{1:10.2f}]'.format(d,e)) #d:총 20자리에 소숫점 10자리
print('d=[{0:.10f}],e=[{1:.2f}]'.format(d,e)) #전체 자리수 생략시 첫 번째 칸부터 출력