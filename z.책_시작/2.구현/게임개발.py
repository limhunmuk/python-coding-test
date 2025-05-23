n, m = map(int, input().split())

# 4 * 4 배열 초기화
d = [[0] * m for _ in range(n)]

# 현재 캐릭터 x, y, direction
x, y, direction = map(int, input().split())
d[x][y] = 1 
count = 1  # 시작 위치 포함

# 지형 정보 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]  # 수정: 동쪽이 +1, 서쪽이 -1

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_time = 0

print(count)
