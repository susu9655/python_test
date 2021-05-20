#숫자 입력후 출력하기
su1=input('첫 번째 숫자입력:')
su2=input('두 번째 숫자입력:')
#파이썬에서 입력시 모든 숫자는 문자로 인식
#형변환, str,int float
#sum=int(su1)+int(su2)

#입력값이 실수형인 경우
sum=float(su1)+float(su2)
print('{},{} 두수의 합계는 {}입니다'.format(su1,su2,sum))
print('{},{} 두수의 합계는 '.format(su1,su2),sum,"입니다.")