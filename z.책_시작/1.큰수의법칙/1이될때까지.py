

n, k = map(int, input().split())
print(n ,k)

result = 0
while n >= k :
        
     
    while n % k != 0:
       n -= 1
       result += 1
          
    # k로 나누기
    n = n / k
    result += 1

while(n > 1) :
    n -= 1
    result += 1
    
print(result)

# 전제
# n에서 1을 뺀다
# n을 k로 나눈다
# 위 경우를 돌아가면서 수행 둘중 하나