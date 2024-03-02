Web VPython 3.2

import random

# 시점 설정
scene.width = 900
scene.height = 600
scene.camera.pos = vector(0, 0, 50)  # 카메라 위치를 Z축으로 이동하여 XY 평면을 볼 수 있게 설정
#scene.camera.axis = vector(0, 0, -1)  # 카메라가 Z축을 따라 내려다보도록 설정


# 위 아래 벽 생성
up_wall = box(pos = vec(0,10,0), size = vec(1000,1,1), color = color.white)
down_wall = box(pos = vec(0,-10,0), size = vec(1000,1,1), color = color.white)

# 1차 벽 생성
top_wall1 = box(pos = vec(0,9,0), color = color.green)
bottom_wall1 = box(pos = vec(0,-9,0), color = color.green)

# 2차 벽 만드는 과정 

# 벽의 위치
wall_xpos = 20
wall_ypos = 3 # random.randint(-5,5)


# 벽 사이 공간(통과하는 공간)
#gap_size = random.randint(3,6)
gap_size = 3


wall_width = 1 # 벽 두께
# wall_interval = random.randint(15,25)
wall_interval = 20 # 벽 사이 거리 

# 2차 벽 생성 (좌표 평면에서 중점 개념을 도입해야함)
top_wall2 = box(pos = vec(wall_xpos, 0.5*(9.5+(9.5-wall_ypos-0.5*gap_size)), 0), size = vec(wall_width, 9.5-wall_ypos-0.5*gap_size, 1), color = color.green)

bottom_wall2 = box(pos = vec(wall_xpos, 0.5*(wall_ypos-0.5*gap_size-9.5) ,0), size = vec(wall_width, wall_ypos-0.5*gap_size+9.5, 1), color = color.green)

# 3차 벽 생성 (좌표 평면에서 중점 개념을 도입해야함)
wall_xpos += 10
wall_ypos -= 4
top_wall2 = box(pos = vec(wall_xpos, 0.5*(9.5+wall_ypos+0.5*gap_size), 0), size = vec(wall_width, 9.5-wall_ypos-0.5*gap_size, 1), color = color.green)

bottom_wall2 = box(pos = vec(wall_xpos, 0.5*(wall_ypos-0.5*gap_size-9.5) ,0), size = vec(wall_width, wall_ypos-0.5*gap_size+9.5, 1), color = color.green)

# 4차 벽 생성
wall_xpos += 11
wall_ypos +=2 
top_wall2 = box(pos = vec(wall_xpos, 0.5*(9.5+wall_ypos+0.5*gap_size), 0), size = vec(wall_width, 9.5-wall_ypos-0.5*gap_size, 1), color = color.green)

bottom_wall2 = box(pos = vec(wall_xpos, 0.5*(wall_ypos-0.5*gap_size-9.5) ,0), size = vec(wall_width, wall_ypos-0.5*gap_size+9.5, 1), color = color.green)


# 이 과정을 통해 반복문으로 이해시킴

walls = []

for i in range(10) :
    wall_xpos += random.randint(10,20)
    wall_ypos += random.randint(-5, 5)
    if wall_ypos >=6 or wall_ypos <= -6 :
        wall_ypos = 0
    
    temp_top = top_wall2 = box(pos = vec(wall_xpos, 0.5*(9.5+wall_ypos+0.5*gap_size), 0), size = vec(wall_width, 9.5-wall_ypos-0.5*gap_size, 1), color = color.green)
    temp_bottom = bottom_wall2 = box(pos = vec(wall_xpos, 0.5*(wall_ypos-0.5*gap_size-9.5) ,0), size = vec(wall_width, wall_ypos-0.5*gap_size+9.5, 1), color = color.green)
    walls.append([temp_top, temp_bottom])