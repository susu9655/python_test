print("안녕하세요\n반가워요\n다음에 또 봐요!!")#\n은 개행
print("""
오늘 점심은 뭐로
먹을까?
배고파
""")#큰 따옴표 3개 안에서 쓴 건 그 모양 그대로 출력

print('''
red
green
orange
yellow
blue
''')

#문자열 함수 공부하기
test="파이썬 프로그래밍 재미있다!"
result=test.startswith("파이썬")
print(result)#문자열 파이썬으로 시작하면 true

result=test.endswith("?")#문자열 ?으로 끝나면 true
print(result)#false
result=test.replace("파이썬","Python")#파이썬으로 Python으로 변경해서 리턴
print(result)

str="have a Nice Day"
r=str.upper()
print(r)
r=str.lower()
print(r)
r='/'.join(str)#문자열의 각 사이에 /문자 넣기
print(r)
r=','.join(str)#문자열의 각 사이에 ,문자 넣기
print(r)