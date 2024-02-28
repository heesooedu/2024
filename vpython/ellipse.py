Web VPython 3.2


# 타원 궤도를 위한 초기 설정
a = 15  # 장반경
b = 10   # 단반경
e = (1 - (b/a)**2)**0.5  # 이심률
angle = 0  # 초기 각도

# 타원의 초점 거리 계산
f = a * e

# 지구 설정
earth = sphere(pos=vector(f, 0, 0), radius=0.5, color=color.blue)

# 행성 설정
planet = sphere(pos=vector(15, 0, 0), radius=0.2, color=color.red, make_trail=True)





# 애니메이션 속도
dt = 0.1

while True:
    rate(300)  # 초당 프레임 수

    # 타원 궤도 계산
    r = a * (1 - e**2) / (1 + e * cos(angle))  # 타원 궤도 상의 행성과 초점 사이 거리
    x = r * cos(angle) + f  # 지구를 초점에 위치시키기 위해 f를 더함
    y = r * sin(angle)
    
    # 행성 위치 업데이트
    planet.pos = vector(x, y, 0)
    
    # 각도 업데이트 - 행성이 지구 근처에 있을 때 더 빠른 속도
    angle += dt * (1 + e * cos(angle))**2 / (a**2 * (1 - e**2)**1.5)

    # 각도가 2π를 초과하면 0으로 초기화
    if angle >= 2 * pi:
        angle -= 2 * pi
