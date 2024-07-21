from collections import deque

def solution(maps):
    # 출발점, 레버, 도착점 위치 초기화
    start, lever, end = None, None, None
    
    # 맵을 순회하며 출발점, 레버, 도착점 위치 찾기
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)
    
    # 출발점, 레버, 도착점 중 하나라도 없으면 -1 반환
    if not start or not lever or not end:
        return -1
    
    # 출발점에서 레버까지 최단 거리 계산
    dist1 = bfs(start, lever, maps)
    if dist1 == -1:
        return -1
    
    # 레버에서 도착점까지 최단 거리 계산
    dist2 = bfs(lever, end, maps)
    if dist2 == -1:
        return -1
    
    # 총 거리를 반환 (출발점 -> 레버 -> 도착점)
    return dist1 + dist2

def bfs(start, goal, maps):
    rows, cols = len(maps), len(maps[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # 상하좌우 방향
    queue = deque([(start[0], start[1], 0)])  # 시작점과 초기 거리 0을 큐에 삽입
    visited = set()  # 방문한 위치를 저장할 집합
    visited.add((start[0], start[1]))  # 시작점을 방문한 것으로 표시
    
    while queue:
        x, y, dist = queue.popleft()
        
        # 목표 지점에 도달하면 현재까지의 거리를 반환
        if (x, y) == goal:
            return dist
        
        # 상하좌우 방향으로 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 맵의 범위 내에 있고, 방문하지 않았으며, 벽이 아닌 경우
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and maps[nx][ny] != 'X':
                # 새로운 위치와 거리를 큐에 삽입하고 방문 표시
                queue.append((nx, ny, dist + 1))
                visited.add((nx, ny))
    
    # 목표 지점에 도달할 수 없으면 -1 반환
    return -1