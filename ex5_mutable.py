#mutable타입의 예제


hello_list=['안녕하세요'] #리스트형 변수 선언
print(hello_list)
print(id(hello_list)) #리스트값 객체 식별자 확인

#mutable타입은 부분 수정도 가능
hello_list[0]="반갑습니다"
print(hello_list)
print(id(hello_list))#리스트값 객체 식별자 확인

#리스트 자료형에 여러 개의 데이터 넣기
arr=[1,2,3,4,5]
print(arr)
print(arr[2])
arr[2]=15 #부분적으로 값 변경 가능
print(arr)
print(arr[2])
print(arr[0:2]) #0~1번지까지 출력
print(arr[1:4]) #1~3번지까지 출력

arr2=[5,6,7]
arr3=arr+arr2 #리스트 타입끼리는 연산도 가능
print(arr3)
