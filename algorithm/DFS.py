import sys
sys.stdin = open('DFS_input.txt', 'r')

def DFS(v):
    visit[v] = True; print(v, end = ' ')
    S.append(v)
    while S:
        for w in G[v]:
            if not visit[w]:
                visit[w] = True; print(w, end = ' ')
                S.append(w)
                v = w
                break
        else:
            v = S.pop()


V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
visit = [False] * (V + 1)
S = []

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

DFS(1)