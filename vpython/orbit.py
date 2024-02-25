Web VPython 3.2

# 공전속도 및 반지름
earth_orbit_radius = 5
moon_orbit_radius = 1


# 구체 생성 (원점에서 일정 거리 떨어진 위치에 초기화)
sun = sphere(pos = vec(0,0,0), radius = 1, color = color.blue)
earth = sphere(pos=vector(earth_orbit_radius,0,0), radius=0.5, color=color.yellow)
moon = sphere(pos = vec(earth_orbit_radius + moon_orbit_radius ,0,0), radius = 0.2, color = color.white)



# 공전을 위한 각속도 및 시간 변수 초기화
earth_angular_speed = 0.1  # 각속도 (라디안 단위)
moon_angular_speed = 0.05

dt = 0.1  # 시간 간격
t = 0  # 초기 시간

while True:
    rate(100)  # 초당 100회 반복으로 애니메이션 속도 제어
    
    # 구체의 위치 업데이트 (원점을 중심으로 하는 회전)
    earth_x = 5*cos(earth_angular_speed*t)
    earth_y = 5*sin(earth_angular_speed*t)
    
    earth.pos = vector(earth_orbit_radius * earth_x, earth_orbit_radius*earth_y,0)
    moon.pos = vec(earth_x + moon_orbit_radius* cos(moon_angular_speed*t), earth_y + moon_orbit_radius*sin(moon_angular_speed*t),0)
    
    # 시간 업데이트
    t += dt
