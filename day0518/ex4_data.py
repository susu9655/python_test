num_data=350#정수 타입
str_data='235'#문자 타입
print(type(num_data))
print(type(str_data))
#sum1=num_data+str_data

#타이을 맞춘 후 계산해야 한다
sum1=num_data+int(str_data)
print(sum1)
sum1=str(num_data)+str_data
print(sum1)

#immutable타입->변경 안됨
#파이썬의 모든 변수는 참조변수(자바의 레퍼런스 타입과 비슷)
hello="안녕하세요"
print(hello)
print(id(hello))

hello="반가워요"
print(hello)
print(id(hello))

str2="hello"
print(str2)
str2[1]="x"#오류 발생-immutable타입이라 한 글자 변경은 불가능, 에러 확인 후 주석 처리
print(str2)