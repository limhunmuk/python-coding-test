# 10, 2
A, B = map(int, input().split())
list = list(map(int, input().split()))

prefix = [0 for _ in range(0, A+1)] 
    
for i in range(A) :
    prefix[i+1] = prefix[i] + list[i]
    # 누적 합 리스트 생성    
    # 1, 2, 3, 4, 5
    # 0, 0, 0, 0, 0
    # 0, 1, 3, 6, 10
    
#print(list)
#print(prefix)
    
#print("=============")

answer = []
# 2 ~ 11
for j in range(B, A+1) :
    # 2 ~ 
    #     1 - (1-2)
    #     2 - (2-2)
    #     3 - (3-2)
    answer.append(prefix[j] - prefix[j-B])
    # B값 간격 값 -> j와 j-B 차이값을 배열에 저장하여 그중 최대값 구함 
    
#       2

# 3, -2, -4, -9,   0,  3,  7,  13,  8, -3
#     1, -6, -13, -9,  3,  10, 20, 21,  5 
# 3,  1, -3, -12, -12, -9, -2, 11, 19, 16
     
print(answer)
print("=======================")
print(max(answer))