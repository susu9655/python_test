#파이썬의 GUI프로그래밍 하는 방법
import tkinter #window생성에 필요한 라이브러리
t=tkinter.Tk() #TK는 window생성을 하기 위한 함수

#버튼 이벤트에서 호출할 사용자 함수를 만들어보자
def process():
    print("버튼 클릭했나요?")

t.geometry('300x200') #가로X세로
t.resizable(0,0) #크기 고정
print("파이썬 tkinter공부하기") #콘솔 출력

#위젯을 추가해보자(자바의 컴포넌트) ex)button,canvas,checkbutton,label등
#컨테이너 위젯:Frame,LabelFrame 등등

#버튼 클릭시 process함수 호출
a1=tkinter.Button(t,text="Hello Python",command=process)
a1.pack() #실제 화면에 나타나게 해주는 메서드

#버튼의 배경색과 글자색을 변경해보자
a1['bg']='orange'
a1['fg']='blue'
#버튼의 라벤 글꼴 변경
a1.configure(font='Arial 15 bold')
a2=tkinter.Label(t,text="비트캠프 501")
a2.pack()

t.mainloop() #모든 이벤트나 시스템 이벤트 처리하기 위한 코드

