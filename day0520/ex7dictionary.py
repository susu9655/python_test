#파이썬의 딕셔너리(dict)는 키(Key)와 값(Value)의 쌍으로 처리되는 데이타 타입
#자바의 Map과 같다
a={0:"zero",1:"one",2:"two",3:"three"}
print(a)
print(a.keys()) #키값들만 출력
print(a.values())#매칭된 값들만 출력
print(a.get(0)) #0번에 저장된 값 출력
print(a.get(3)) #3번에 저장된 값 출력
print(len(a)) #총 개수

ebook={"제목":"살인자의 기억법","저자":"김영하","가격":"15000원"}
print(ebook.keys()) #키값들만 출력
print(ebook.values())#매칭된 값들만 출력
print("제목=",ebook.get("제목"))
print("저자=",ebook.get("저자"))
print("가격=",ebook.get("가격"))