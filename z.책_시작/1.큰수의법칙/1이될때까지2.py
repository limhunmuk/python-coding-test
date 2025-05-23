

n, k = map(int, input().split())
print(n ,k)

result=0

while True :
    
    # n == k  로 나누어 떨어지는 수가 될때까지 1씩 빼기
    target = (n//k) * k
    result += (n - target)
    # n이 k보다 작을때 ( 더이상 나눌수 없을때 ) 반복문 탈출
    n = target
    
    if n < k :
        break
    
    # k로 나누기
    result += 1
    n //= k
    
# 마지막 남은 수에 대해서 1씩 빼기
result += (n-1)
print(result)