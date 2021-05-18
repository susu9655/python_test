#for문 안에서 실행되는 문장은 반드시 한 탭 들여써야 한다
for x in range(10): #0부터 9까지 반복
    print("Hello")

for x in range(3): #0부터 2까지 반복
    print(x)
    print("--")#for문안에서 반복됨(들여쓰기 안 하면 for문 끝나고 한번 실행)

#1부터 100까지 합계구하기
s=0
for x in range(1,101):
    s=s+x
print("1부터 100까지의 합은",s,"입니다.")
