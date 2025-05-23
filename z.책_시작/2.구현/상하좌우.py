#상하좌우 
n=int(input())
steps=input().split()

print("n = ", n)
print("step = ", len(steps))

x, y = 1, 1

# x,y가 수학에서는 가로축 새로축인데
# 프로그램 [배열 혹은 행렬]에서는 반대임
# arr[x][y] x는 로우 y는 컬럼

#dx=[0, 0, -1, 1]
#dy=[-1 ,1, 0, 0]

#move_type=['L', 'R', 'U', 'D']

move = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}

# steps는 입력값 R R R U D D
for step in steps :
    for i in range(len(move)) :
       # if step == move[i] :
       #     nx = x + dx[i]
       #     ny = y + dy[i]
       dx, dy = move[step]
       nx = x + dx
       ny = y + dy
            
    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue
    x, y = nx, ny
        
print(x, y)
    