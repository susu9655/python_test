a=[3,1,5]
print(a)
a.append(100)
print(a) #추가
a.sort() #오름차순 정렬
print(a)
a.reverse() #내림차순 정렬
print(a)
a.remove(1) #값 1을 찾아서 삭제
print(a)
del a[0] #0번 인덱스 값 삭제
print(a)
print(len(a)) #총 개수
print(a.count(5)) #5라는 값의 개수