def BFS(g, s, t, parent):
    visited = [False]*(len(g))
    queue=[]
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.pop(0)
        for ind, val in enumerate(g[u]):
            if visited[ind]==False and val==1 :
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
    return True if visited[t] else False

g = [[0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0]]
s = 0
t = len(g)-1
p = [-1]*(len(g))
if BFS(g,s,t,p):
    sp = [t] # path for sheep
    while p[sp[0]]!=s:
        g[p[sp[0]]][sp[0]] = 0
        g[sp[0]][p[sp[0]]] = 1
        sp = [p[sp[0]]] + sp
    g[p[sp[0]]][sp[0]] = 0
    g[sp[0]][p[sp[0]]] = 1
    sp = [s] + sp
    p = [-1]*(len(g))
    if BFS(g,s,t,p):
        wp = [t] # path for wolf
        while p[wp[0]]!=s:
            wp = [p[wp[0]]] + wp
        wp = [s] + wp
        u = sp[0]
        v = sp[1]
        while v!=t:
            if v in wp and wp[wp.index(v)+1]==u:
                i = sp.index(u)
                j = wp.index(v)
                sp = sp[:i+1] + wp[j+2:]
                wp = wp[:j+1] + sp[i+2:]
                v = sp[sp.index(u)+1]
            else:
                u = v
                v = sp[sp.index(v)+1]
        print(sp)
        print(wp)
    else:
        print("There is no two edge-disjoint paths from s to t.")
else:
    print("There is no two edge-disjoint paths from s to t.")