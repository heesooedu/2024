Web VPython 3.2

#자유낙하

ball1 = sphere(color = color.red, pos = vec(0,10,0), make_trail = True)
ball2 = sphere(color = color.red, pos = vec(10,10,0), make_trail = True)

# y방향으로등속운동중
ball1.v = vec(0,-10,0)
ball2.v = vec(0,-10,0)

while True :
    rate(100)
    
    #변위
    ball1.pos = ball1.pos + ball1.v * 0.01
    
    ball2.pos = ball2.pos + ball2.v * 0.01
    
    

    ball1.v.y = ball1.v.y - 9.8*0.01
    # ball1 은 등가속도 운동
    # ball2 는 등속도 운동
    