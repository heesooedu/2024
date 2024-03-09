Web VPython 3.2

import random

# 게임 환경 설정
scene.width = 600
scene.height = 400
scene.range = 20

# 맵 지정
wallN = box(pos = vec(0,scene.range+1,0), size = vec(2*scene.range+1, 1, 1))
wallW = box(pos = vec(scene.range+1,0,0), size = vec(1 , 2*scene.range+1+2, 1))
wallE = box(pos = vec(-scene.range-1,0,0), size = vec(1 , 2*scene.range+1+2, 1))
wallS = box(pos = vec(0,-scene.range-1,0), size = vec(2*scene.range+1, 1, 1))


# 시점
scene.camera.pos = vec(0,0,2*scene.range)

# 뱀 생성(처음에는 1개)
snake = [box(pos=vector(0, 0, 0), size=vector(1, 1, 1), color=color.red)]

# 먹이 생성
#def create_food():
#    return box(pos=vector(random.randint(-scene.range, scene.range), random.randint(-scene.range, scene.range), 0), size=vector(1, 1, 1), color=color.green)

food = box(pos=vector(random.randint(-scene.range, scene.range), random.randint(-scene.range, scene.range), 0), size=vector(1, 1, 1), color=color.green)


# 방향 설정
direction = vector(1, 0, 0)

# 키 입력 처리
# def onKeyDown(evt):
#     global direction
#     s = evt.key
#     if s == 'left' and direction.x == 0:
#         direction = vector(-1, 0, 0)
#     elif s == 'right' and direction.x == 0:
#         direction = vector(1, 0, 0)
#     elif s == 'up' and direction.y == 0:
#         direction = vector(0, 1, 0)
#     elif s == 'down' and direction.y == 0:
#         direction = vector(0, -1, 0)

# 키보드 이벤트 리스너 등록
#scene.bind('keydown', onKeyDown)

while True:
    rate(10)  # 게임 속도 조절
    
    key = keysdown()
    if 'left' in key :
        direction = vec(-1,0,0)
    if 'right' in key :
        direction = vec(1,0,0)
    if 'up' in key :
        direction = vec(0,1,0)
    if 'down' in key :
        direction = vec(0,-1,0)


    # 뱀 머리 위치 업데이트
    new_head = box(pos=snake[0].pos + direction, size=vector(1, 1, 1), color=color.red)
    
    # 먹이 먹기 체크
    if new_head.pos == food.pos:
        food.visible = False
        food = box(pos=vector(random.randint(-scene.range, scene.range), random.randint(-scene.range, scene.range), 0), size=vector(1, 1, 1), color=color.green)
    else:  # 먹이를 먹지 않았다면 뱀 꼬리 제거
        snake[-1].visible = False
        snake.pop()

    # 뱀 몸통 업데이트
    snake.insert(0, new_head)

    # 충돌 체크 (벽 또는 자기 자신) 고1 학생은 절댓값을 포함하는 부등식에 대해 학습함(수학 상)
    #if abs(new_head.pos.x) > scene.range or abs(new_head.pos.y) > scene.range or new_head.pos in [segment.pos for segment in snake[1:]]:
    #    print("Game Over!")
    #    break
    
    # 머리가 사각형을 벗어나면 -> 나중에 일차부등식으로 바꿔버려도 됨
    if (new_head.pos.x > scene.range) or (new_head.pos.x < -scene.range) or (new_head.pos.y > scene.range) or (new_head.pos.y < -scene.range) :
        print("Game Over")
        break
    # 자시 자신과 충돌했는지 검사
    for i in range(1, len(snake)) :
        if snake[i].pos == new_head.pos :
            break

    
