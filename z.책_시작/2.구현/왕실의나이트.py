# nxn좌표판
# 수평이동2 수직이동1
# 수평이동1 수직이동2


input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a'))+1

print(row)
print(column)

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]

count = 0

# 각 방향에 대해 이동 가능한지 확인
for dx, dy in steps:
    nx = row + dx
    ny = column + dy

    # 체스판 안에 있는 경우만 카운트
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)