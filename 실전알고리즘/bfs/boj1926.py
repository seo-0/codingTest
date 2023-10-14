'''
1. 아이디어
-2중 포문 -> 값이 1이면 방문 안함 => bfs 이용
-bfs 돌면서 그림개수 +1, 최댓값을 갱신

#2. 시간복잡도: (v+e)= m*n + v * 4 = 5(mn)=약100만 >> 가능
#3. 자료구조
-그래프 전체 지도: int[][] 2차원배열
-방문: bool[][]
-큐 (bfs) 사용
'''

import sys
input= sys.stdin.readline
 
n, m= map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)] #2차원 배열
visitNum= [[False] * m for _ in range(n)] # 방문횟수

cnt =0
maxValue= 0

dy=[0, 1, 0, -1]
dx=[1, 0, -1, 0]

def bfs(y,x):
    rs=1
    q= [(y,x)]
    while q:
        ey, ex= q.pop()
        for k in range(4):
            ny= ey + dy[k]
            nx= ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx]==1 and visitNum[ny][nx]== False:
                    rs+=1
                    visitNum = True
                    q.append((ny, nx))
    return rs

for j in range(n):
    for i in range(m):
        if map[j][i] ==1 and visitNum[j][i] == False:
            visitNum[j][i]==True
            # 전체 그림갯수 +1
            cnt+=1
            maxValue = max(maxValue, bfs(j,i))

print(visitNum)
print(maxValue)