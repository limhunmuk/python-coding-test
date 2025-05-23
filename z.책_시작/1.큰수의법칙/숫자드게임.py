# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

n, m = map(int, input().split())
result = 0 

for i in range(n):
    data = list(map(int, input().split()))
    min_val = min(data)
    
    result = max(result, min_val)
    
print(result)

#  가로 세로 배열 크기를 받아
# 루프를 도며 최소값을 받고 그중 가장 큰값
            