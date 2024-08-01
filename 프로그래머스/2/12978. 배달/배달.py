import heapq

def solution(N, road, K):
    # 그래프를 인접 리스트로 표현, 거리 배열을 무한대로 초기화
    graph = [[] for _ in range(N + 1)]
    distance = [float('inf')] * (N + 1)
    
    # 도로 정보를 기반으로 그래프 구축
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    def dijkstra(start):
        queue = []
        heapq.heappush(queue, (0, start))  # 시작 노드를 우선순위 큐에 추가
        distance[start] = 0  # 시작 노드의 거리는 0으로 설정
        
        while queue:
            dist, now = heapq.heappop(queue)  # 가장 짧은 거리를 가진 노드를 꺼냄
            
            if distance[now] < dist:  # 이미 처리된 노드라면 무시
                continue
            
            for i in graph[now]:  # 현재 노드와 연결된 노드들을 확인
                cost = dist + i[1]
                
                if cost < distance[i[0]]:  # 더 짧은 경로를 찾았다면 거리 배열 갱신
                    distance[i[0]] = cost
                    heapq.heappush(queue, (cost, i[0]))  # 새롭게 갱신된 거리와 노드를 큐에 추가
    
    dijkstra(1)  # 1번 마을에서 시작하여 다익스트라 알고리즘 수행
    
    # 거리 배열에서 거리가 K 이하인 마을의 수를 세어 반환
    return len([d for d in distance if d <= K])

# 예제 사용
N = 5
road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
K = 3
print(solution(N, road, K))  # 출력: 4