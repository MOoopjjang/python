#!python3
#-*- coding:utf-8 -*-




import turtle as t
import random



te = t.Turtle()   # 악당거북이 ( 빨간색 )
te.shape('turtle')
te.color('red')
t.speed(0)
te.up()
te.goto( 0  , 200 )


ts = t.Turtle()  #먹이 ( 초록색 동그라미 )
ts.shape('circle')
ts.color('green')
ts.up()
ts.goto(0 , -200)


def turn_right():     #오른쪽으로 방향을 바꿉니다
	t.setheading( 0 )


def turn_up():			#위로 방향을 바꿉니다.
	t.setheading( 90 )

def turn_left():		#왼쪽으로 방향을 바꿉니다.
	t.setheading( 180 )

def turn_down():
	t.setheading( 270 )


def play():						# 게임을 실제로 플레이하는 함수
	t.forward( 10 )				# 주인공 거북이가 10만큼 앞으로 이동합니다.
	ang = te.towards( t.pos() )
	te.setheading( ang )
	te.forward( 9 ) 
	if t.distance( ts ) < 12:		#주인공과 먹이의 거리가 12보다 작으면 ( 가까우면 )
		star_x = random.randint( -230 , 230 )
		star_y = random.randint( -230 , 230 )
		ts.goto(star_x , star_y)	#먹이를 다른곳으로 옮깁니다.

	if t.distance(te) >= 12:		# 주인공과 악당의 거리가 12이상이면 ( 멀면 )
		t.ontimer( play , 100 )


t.setup( 500 , 500 )
t.bgcolor('orange')	
t.shape('turtle')				# 거북이 모양의 커서를 사용합니다.
t.speed( 0 )					# 거북이의 속도를 가장 빠르게 지정합니다.
t.up()
t.color('white')
t.onkeypress(turn_right , 'Right')
t.onkeypress(turn_up , 'Up')
t.onkeypress(turn_left , 'Left')
t.onkeypress(turn_down , 'Down')
t.listen()					# 거북이 그래픽 창이 키보드 입력을 받도록 합니다.
play()



