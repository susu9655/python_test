sang=input("상품명을 입력하세요")
su=input("수량을 입력하세요")
su=int(su)
dan=input("단가를 입력하세요")
dan=int(dan)
sum=0
if su>=5:
    print("5개 이상은 10% 할인됩니다.")
    sum=su*dan*0.9
else:
    print("5개 미만이라 할인이 안 됩니다.")
    sum=su*dan
print(sang,"상품 ",su,"개는 총",sum,"원 입니다.")