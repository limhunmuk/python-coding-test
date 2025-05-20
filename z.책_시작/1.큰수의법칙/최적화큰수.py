n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

first = arr[n - 1]
second = arr[n - 2]

# 전체 묶음에서 가장 큰 수가 등장하는 횟수
count = int(m / (k+1) * k)
# 남은 횟수 (연속 제한에 안 걸리는 부분 → 큰 수 사용 가능)
count += m % (k+1)

result = 0 
# 큰수 등장 횟수 = (묶음 수) * k + (남은 횟수)
result += (count) * first
# 작은수 등장 횟수 = m - 큰수 등장 횟수
result += (m - count) * second

print(result)
