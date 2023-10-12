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
for i in range(n):
    for j in range(m):
        if map[i][j] ==1 and visitNum[i][j] ==False:
            #전체 그림 갯수 +1
            #Bfs > 그림크기 구해주고
            #최댓값 갱신