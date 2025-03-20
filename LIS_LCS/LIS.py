# 완전탐색> 재귀 > 탑다운 > 바텀업
# 안되는경우가 있음
# -- > 대표 냅색, 동전, LIS

# LCS(Longest Common Subsequence, 최장 공통 부분 수열)

# dp
#    10   20   10   30   20   50
#     1    2    1    3   2    4 

N = int(input())
arr = list(map(int, input().split()))

DP = [1 for _ in range(N+1)]
arr_cp = [1 for _ in range(N+1)]

#print ("N ", N)
#print ("M ", arr)

#print(len(DP))

for i in range(N) :
    for j in range(i) :
        if arr[i] > arr[j] :
            DP[i] = max(DP[i], DP[j]+1)
            arr_cp[i] = max(arr[i], arr[j]+1)
            
            
print(max(DP))
print(arr_cp)
            