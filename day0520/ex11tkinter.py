#파이썬의 GUI프로그래밍 하는 방법
import tkinter #window생성에 필요한 라이브러리
t=tkinter.Tk() #TK는 window생성을 하기 위한 함수
#입력후 엔터를 누를 경우 이벤트 핸들러
def change_img():
    path=inputbox.get()
    img=tkinter.PhotoImage(file=path)
    imgLabel.configure(image=img)
    imgLabel.image=img

#프레임
t.title="이미지 배경화면"

#이미지라벨,입력창,버튼 추가
photo=tkinter.PhotoImage(file='08.png')
imgLabel=tkinter.Label(t,image=photo)
imgLabel.pack()

inputbox=tkinter.Entry(t)#입력박스
inputbox.pack()

button=tkinter.Button(t,text="전송",command=change_img)
button.pack()

t.geometry('300x300') #가로X세로
t.resizable(0,0) #크기 고정


t.mainloop() #모든 이벤트나 시스템 이벤트 처리하기 위한 코드