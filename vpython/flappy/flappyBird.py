Web VPython 3.2

import random


# 위 아래 벽 생성
up_wall = box(pos = vec(0,10,0), size = vec(1000,1,1), color = color.white)
down_wall = box(pos = vec(0,-10,0), size = vec(1000,1,1), color = color.white)


# 벽의 초기위치
wall_xpos = 20
wall_ypos = 3 # random.randint(-5,5)

# 벽 사이 공간(통과하는 공간)
#gap_size = random.randint(3,6)
gap_size = 3

wall_width = 1 # 벽 두께
# wall_interval = random.randint(15,25)
wall_interval = 20 # 벽 사이 거리 


# 벽 만들기
walls = []

for i in range(20) :
    wall_xpos += random.randint(10,20)
    wall_ypos += random.randint(-5, 5)
    if wall_ypos >=6 or wall_ypos <= -6 :
        wall_ypos = 0
    
    temp_top = top_wall2 = box(pos = vec(wall_xpos, 0.5*(9.5+wall_ypos+0.5*gap_size), 0), size = vec(wall_width, 9.5-wall_ypos-0.5*gap_size, 1), color = color.green)
    temp_bottom = bottom_wall2 = box(pos = vec(wall_xpos, 0.5*(wall_ypos-0.5*gap_size-9.5) ,0), size = vec(wall_width, wall_ypos-0.5*gap_size+9.5, 1), color = color.green)
    walls.append([temp_top, temp_bottom])


# 새 생성
    
bird = sphere(pos = vec(0,0,0), radius = 0.5, make_trail = True)
#scene.camera.follow(bird)

scene.camera.pos = bird.pos + vec(0,0,30)
scene.camera.range = 10

bird.vx = vec(5,0,0) # 가독성을 위해 x축 방향으로 속도를 vx라 표기함
bird.vy = vec(0,-1,0) # y축 방향으로 속도를 vy라 표기함
bird.jump = vec(0,3,0) # 수직으로 점프!

game_Flag = True

#게임 플레이
while game_Flag :
    rate(100) # 값을 바꿔 움직임이 조금 더 부드럽게 바꿔보세요
    
    # x축 움직임
    bird.pos = bird.pos + bird.vx * 0.01 
    
    # y축 움직임
    bird.pos = bird.pos + bird.vy * 0.01
    bird.vy = bird.vy + vec(0,-3,0) * 0.01

    k = keysdown()
    if 'up' in k : # 방향키 위가 눌렸을 때 y축 속도를 위로 바꾸기
        bird.vy = bird.jump
    
    scene.camera.pos = bird.pos + vec(0,0,30)
    scene.camera.range = 10

    # 충돌 감지
    
    # 벽과의 충돌 검사
    if bird.pos.y >= 9 or bird.pos.y <= -9 :
        game_Flag = False
    
    for wall_pair in walls:
        top_wall, bottom_wall = wall_pair
        # x 위치가 가까운지 확인
        if abs(bird.pos.x - top_wall.pos.x) < wall_width / 2 + bird.radius:
            # y 위치가 벽 사이에 없는지 확인
            if bird.pos.y > top_wall.pos.y - top_wall.size.y / 2 or bird.pos.y < bottom_wall.pos.y + bottom_wall.size.y / 2:
                game_Flag = False
                
                break  # 충돌이 발생하면 게임 루프를 중단

text(text = 'Game Over', align = 'center', pos = bird.pos)
