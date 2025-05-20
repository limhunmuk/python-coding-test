size, addCnt, loopCnt = map(int, input().split())
lists = list(map(int, input().split()))


lists.sort()

# 정렬 첫빠따
first = lists[size - 1]
second = lists[size - 2]

result=0

while True :
    for i in range(loopCnt) :
        if addCnt == 0 :
            break
        result += first
        addCnt -= 1
    if addCnt == 0 :
        break
    result += second
    addCnt -= 1
    
print("======================")
print(result)
print("======================")
