Web VPython 3.2

# 기본 설정
scene.width = 600
scene.height = 400


# 구체 생성
ball = sphere(pos=vector(-5, 0, 0), radius=0.5, color=color.blue, make_trail=True)

# 운동 변수 설정
velocity_x = 0.05  # X축 방향 속도
velocity_y = 0  # Y축 방향 속도 (초기에는 0)
gravity = -0.005  # 중력 가속도 (음수로 설정하여 아래로 작용하게 함)
jump_speed = 0.5  # 점프 속도

# 마우스 클릭 이벤트 처리
# 함수 개념은 다루지 않고 조건문으로 처리
# def jump(evt):
#     global velocity_y
#     velocity_y = jump_speed

# 마우스 클릭 이벤트 연결
# scene.bind('click', jump)

# 애니메이션 루프
while True:
    rate(50)  # 프레임 레이트 설정
    
    k = keysdown()
    if 'up' in k :
        velocity_y = jump_speed
    
    
    # X축 방향 이동
    ball.pos.x += velocity_x

    velocity_y += gravity
    ball.pos.y += velocity_y


