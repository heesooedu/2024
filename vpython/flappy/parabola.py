Web VPython 3.2

# 공 생성
ball = sphere(pos=vector(-9, 0, 0), radius=0.5, color=color.red, make_trail= True)

# 운동 변수 설정
velocity = vector(5, 5, 0)  # 초기 속도 (x축과 y축 방향)
gravity = vector(0, -9.8, 0)  # 중력 가속도
dt = 0.01  # 시간 간격

# 애니메이션 루프
while True:  # 공이 땅에 닿을 때까지 반복
    rate(100)  # 애니메이션 속도 조절
    ball.pos = ball.pos + velocity * dt  # 위치 업데이트
    velocity = velocity + gravity * dt  # 속도 업데이트 (중력의 영향)
