Web VPython 3.2

# 공전속도 및 반지름
earth_orbit_radius = 5
moon_orbit_radius = 1
mars_orbit_radius = 10

# 구체 생성 (원점에서 일정 거리 떨어진 위치에 초기화)
sun = sphere(pos = vec(0,0,0), radius = 1, color = color.yellow)
earth = sphere(pos=vector(earth_orbit_radius,0,0), radius=0.5, texture = textures.earth)
moon = sphere(pos = vec(earth_orbit_radius + moon_orbit_radius ,0,0), radius = 0.2, color = color.white)
mars = sphere(pos = vec(-1*mars_orbit_radius, 0,0), radius = 0.6, color = color.red)


# 공전을 위한 각속도 및 시간 변수 초기화
earth_angular_speed = 0.1  # 각속도 (라디안 단위)
moon_angular_speed = 0.3
mars_augular_speed = 0.2


dt = 0.1  # 시간 간격
t = 0  # 초기 시간

# 달을 우주선으로 생각하여 발사하는 것을 생각해볼 수 있음

while True:
    rate(100)  # 초당 100회 반복으로 애니메이션 속도 제어
    
    # 구체의 위치 업데이트 (원점을 중심으로 하는 회전)
    earth_x = earth_orbit_radius * cos(earth_angular_speed*t)
    earth_y = earth_orbit_radius * sin(earth_angular_speed*t)
    
    mars_x = mars_orbit_radius*cos(pi + mars_augular_speed*t)
    mars_y = mars_orbit_radius*sin(pi + mars_augular_speed*t)

    # 위치 업데이트
    earth.pos = vector(earth_x, earth_y,0)
    moon.pos = vec(earth_x + moon_orbit_radius* cos(moon_angular_speed*t), earth_y + moon_orbit_radius*sin(moon_angular_speed*t),0)
    mars.pos = vec(mars_x, mars_y, 0)



    # 시간 업데이트
    t += dt
