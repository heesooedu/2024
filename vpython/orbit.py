Web VPython 3.2

# 천체 및 상수 정의
G = 6.67430e-11  # 중력 상수 (m^3 kg^-1 s^-2)
sun_mass = 2e30
earth_mass = 5.972e24  # 지구 질량 (kg)
moon_mass = 7.346e22  # 달 질량 (kg)
mars_mass = 6.39e23   # 화성 질량  (kg)

# 평균 반지름
sun_radius = 696.3e6 # (m)
earth_radius = 6.371e6 # (m)
moon_radius = 1.737e6 # (m)
mars_radius = 3.389e6 # (m)

# (평균) 공전 반지름
earth_orbit_radius = 149.6e9  # 지구 평균 궤도 반지름 (m), 1 AU
moon_orbit_radius = 384.4e6 # 지구에서 달까지의 거리 (m)
mars_orbit_radius = 227.9e9 # 화성 평균 궤도 반지름 , 1.52 AU

# 구체 생성 (원점에서 일정 거리 떨어진 위치에 초기화)
sun = sphere(pos = vec(0,0,0), radius = sun_radius*30, color = color.yellow)
earth = sphere(pos=vector(earth_orbit_radius,0,0), radius=earth_radius*1000, texture = textures.earth)
moon = sphere(pos = vec(earth_orbit_radius + 100*moon_orbit_radius ,0,0), radius = moon_radius*2500, color = color.white)
mars = sphere(pos = vec(-1*mars_orbit_radius, 0,0), radius = mars_radius*2000, color = color.red)


# 공전을 위한 각속도 및 시간 변수 초기화 / 속도 빠르게 멈춘것 처럼 보임
# 1초가 24시간의 움직임 86400초 = 24시간
earth_angular_speed = 86400*sqrt((G*(earth_mass+sun_mass)/earth_orbit_radius))/earth_orbit_radius  # 각속도 (라디안 단위)
moon_angular_speed = 86400*sqrt((G*(earth_mass+moon_mass)/moon_orbit_radius))/moon_orbit_radius
mars_augular_speed = 86400*sqrt((G*(mars_mass+sun_mass)/mars_orbit_radius))/mars_orbit_radius


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



    # 위치 업데이트 / 달과 지구 사이 거리 100배 멀게 설정, 안 그러면 달이 안 보임
    earth.pos = vector(earth_x, earth_y,0)
    moon.pos = vec(earth_x + 100*moon_orbit_radius* cos(moon_angular_speed*t), earth_y + 100*moon_orbit_radius*sin(moon_angular_speed*t),0)
    mars.pos = vec(mars_x, mars_y, 0)



     # 시간 업데이트
    t += dt
