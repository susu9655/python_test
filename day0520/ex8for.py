#for문
a=["angel","mini","toto","nana"]

for i in a:
    print(i)

print("-"*10)
for i in 1,2,3:#1,2,3값 개수만큼 반복
    print(i)

print("-"*10)
for i in [1,2,3,4,5]: #리스트 형태의 값을 직접 설정
    print(i)

print("-"*10)
for s in 'korea','japan','china':
    print(s)

print("-"*10)
for a in range(5): #0~4까지 반복
    print(a)

print("-"*10)
for a in range(1,11): #1~10까지 반복
    print(a)

print("-"*10)
print("**구구단**")
for a in range(2,10):
    print('[',a,'단]')
    for b in range(1,10):
        print(a,'*',b,'=',a*b)
    print("\n") #2번째 반복문이 끝난후 한번 실행