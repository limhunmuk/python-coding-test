n=int(input())

#print('분배 가능한 사탕 수 ==== >', n)

rtn = 0
for a in range(0, n+1) :
    for b in range(0, n+1) :
        for c in range(0, n+1) :
            if( a + b + c) == n :
                if( a >= b+2 ) :
                    if ( a != 0 and b != 0 and c != 0) :
                        if ( c % 2 == 0) :
                            rtn = rtn + 1

print(rtn)
        
    
