Web VPython 3.2


import random

# 게임 설정
scene.width = 600
scene.height = 400
gap_size = 6  # 장애물 사이의 공간
wall_width = 1
wall_interval = 20  # 장애물 사이의 간격
bird_radius = 0.5
gravity = -0.2  # 중력을 반대 방향으로 적용
flap_strength = 5
bird_velocity = 0

# 새 생성
bird = sphere(pos=vec(-10,0,0), radius=bird_radius, color=color.yellow)

# 벽 생성 함수
def create_wall(pos):
    top = box(pos=pos + vec(0, (gap_size + wall_width) / 2, 0), size=vec(wall_width, 10-gap_size, 1), color=color.green)
    bottom = box(pos=pos - vec(0, (gap_size + wall_width) / 2, 0), size=vec(wall_width, 10-gap_size, 1), color=color.green)
    return top, bottom

# 초기 벽 생성
walls = []
for i in range(5):
    walls.extend(create_wall(vec(i * wall_interval, random.uniform(-3, 3), 0)))

# 마우스 클릭 이벤트 처리
def on_click(evt):
    global bird_velocity
    bird_velocity = flap_strength

# 마우스 클릭 이벤트 연결
scene.bind('click', on_click)

game_over_flag = True
    
while game_over_flag:
    rate(30)  # 게임 속도
    
    # 새의 위치 업데이트
    bird_velocity += gravity
    bird.pos.y += bird_velocity * 0.1
    
    # 벽 이동
    for wall in walls:
        wall.pos.x -= 0.2
        if wall.pos.x < -20:
            wall.pos.x += 5 * wall_interval
            wall.pos.y = random.uniform(-3, 3)
    
    # 충돌 체크
    for wall in walls:
        if abs(bird.pos.x - wall.pos.x) < bird_radius + wall_width/2 and abs(bird.pos.y - wall.pos.y) < gap_size/2:
            print("Game Over!")
            game_over_flag = False
            break





