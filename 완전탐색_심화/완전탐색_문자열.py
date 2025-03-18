# 재귀호출로 수열

def recur(in_number, out_text) :
    
    if(in_number == CHASOO) :
    
        trim_output = out_text.strip();
        if(len(trim_output) > 1) :
            a, b = map(int, out_text.split())
            #if(a != b) :
            if a == b :
                #print(out_text)
                return
            else :
                print(out_text)
                return
        
            
    
    #print("check = ", 1, N+1)
    for i in range(1, RANGE+1) :
        #print("in_number=", in_number+1, ", out_text=", out_text+str(i)+" ")
        recur(in_number+1, out_text+str(i)+" ")
        
    
RANGE, CHASOO = map(int, input().split())    
#arr = []
#print("start")
recur(0, "")
