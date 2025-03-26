
def search(x, y):
    
    if(dp[x][y] != 0):
        return dp[x][y]
    #point=0
    #               상 하 좌 우 표현 -- > 인강에선 그래서 y, x 순으로 루프를 돈다
#    for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]] :
    for dx, dy in [[0,-1], [0,1], [-1,0], [1,0]] :
        ex = x+dx
        ey = y+dy
        
        if 0 <= ex < N and 0 <= ey < N :
            if arr[x][y] < arr[ex][ey] :
               # point=max(point, search(ex, ey) +1)
               #dp[x][y] = max(dp[x][y], search(x, y)+1)
               dp[x][y] = max(dp[x][y], search(ex,ey) + 1) 
                
    #return point
    return dp[x][y]
    
 
N=int(input())
arr=[list(map(int, input().split())) for _ in range(N)]
dp=[[ 0 for _ in range(N)] for _ in range(N)]
#print(N)

for x in range(len(arr)) :
    for y in range(len(arr)) :
        
        search(x, y)
        #point = search(x, y)
        #print(x, y, point)
        
#print(max(map(max, dp)) +1)
#이케하면 2차원 배얄에서 최대값이 자동으로 나옴
print(max(map(max, dp)) + 1)

