a=50
b=[10,20,30,40,50]
print(type(a))
print(type(b))
print(len(b)) #개수 구하기
b.append(60)  #리스트의 마지막에 추가
print(b)
b.pop() #리스트의 마지막 요소 꺼냄
print(b)
print(b.count(10)) #10이라는 데이타의 개수 반환 1
print(b.count(70)) #70이라는 데이타의 개수 반환 0
print(b.index(10)) #데이타의 인덱스 반환
b.insert(2,80) #2번 인덱스에 80끼워 넣기
print(b)
b.insert(0,"겨울")#문자도 insert
print(b)
b.clear()#모두 지움
print(b)