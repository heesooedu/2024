Web VPython 3.2

# 구 생성
ball1 = sphere(pos=vector(-5, 0, 0), radius=0.5, color=color.red)
ball2 = sphere(pos=vector(-5, 5, 0), radius=0.5, color=color.blue)

# 속도 설정 (예: x축 방향으로 초당 1단위)
# 벡터는 크기와 방향을 가짐을 이해시켜야 함

ball1.velocity = vec(1, 0, 0)
ball2.velocity2 = vec(5, 0, 0)

# 시뮬레이션 루프
while True:
    rate(30) # 초당 30회 업데이트(while문이 1초에 30번 돌아간다), 시뮬레이션의 부드러움을 조절, 
    
    # 구의 위치 업데이트
    ball1.pos = ball1.pos + ball1.velocity * 1/30 # 속도 * 시간(1/30초)
    ball2.pos = ball2.pos + ball2.velocity2 * 1/30 # 속도 * 시간(1/30초)


# sphere를 사용하여 구를 생성하고 초기 위치, 반지름, 색상을 설정합니다.
# 구의 속도를 정의합니다. 여기서는 x축을 따라 양의 방향으로 이동하도록 설정되어 있습니다.
# 무한 루프 안에서, rate(30)은 루프가 초당 약 30회 실행되도록 제어하여 시뮬레이션의 시간 경과를 모방합니다.
# 각 반복에서 구의 위치는 velocity * 1/30만큼 변경됩니다. 이는 구가 초당 velocity만큼 이동한다는 것을 의미합니다. 1/30은 각 rate(30) 호출 사이의 시간 간격을 대략적으로 나타냅니다.