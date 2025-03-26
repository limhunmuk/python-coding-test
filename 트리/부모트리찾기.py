N = int(input())

graph = [[] for _ in range(N+1)]
parent = [ 0 for _ in range(N+1)]

for _ in range(N-1) :
    a,b= map(int, input().split())
  
    graph[a].append(b)
    graph[b].append(a)
    
    

#print(graph)

def recur(node, prev) :

    
    parent[node] = prev
    for nxt in graph[node] :
        if nxt == parent :
            continue
        recur(nxt, node)
    
    
    
print("======================")
recur(1, 0)

print(parent)

    