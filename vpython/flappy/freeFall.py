Web VPython 3.2

#자유낙하

ball1 = sphere(color = color.red, pos = vec(0,10,0), make_trail = True)
ball2 = sphere(color = color.blue, pos = vec(10,10,0), make_trail = True)


ball1.v = vec(0,0,0)   # 처음에는 y방향으로 속도 없이 정지상태
ball2.v = vec(0,-10,0) # y방향으로등속운동중

while True :
    rate(100)
    
    
    ball1.pos = ball1.pos + ball1.v * 0.01
    ball1.v = ball1.v + vec(0,-9.8,0)*0.01
    
    ball2.pos = ball2.pos + ball2.v * 0.01
    
    

    
    # ball1 은 자유낙하
    # ball2 는 등속도 운동
    