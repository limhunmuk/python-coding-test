# 입력
cnt = int(input())
nums = list(map(int, input().split()))

# 초기화
current_sum = nums[0]
max_sum = nums[0]

# 배열 순회
for i in range(1, cnt):
    current_sum = max(nums[i], current_sum + nums[i])  # 이전 합을 포함할지, 현재 값만 선택할지 결정
    max_sum = max(max_sum, current_sum)  # 최대값 갱신

print(max_sum)  # 최대 부분합 출력
