Web VPython 3.2
# 구 생성 및 초기화
ball = sphere(pos=vector(-5, 0, 0), radius=0.5, color=color.blue)

# 초기 속도와 가속도 설정
ball.velocity = vector(0, 0, 0) # 초기 속도
ball.acceleration = vector(0.5, 0, 0) # x축 방향으로의 가속도

# 시뮬레이션 루프
while True:
    rate(100) # 초당 100회 업데이트, 시뮬레이션의 부드러움 조절

    # 속도 업데이트 (가속도 적용)
    ball.velocity = ball.velocity + ball.acceleration * 1/100

    # 위치 업데이트 (속도 적용)
    ball.pos = ball.pos + ball.velocity * 1/100
