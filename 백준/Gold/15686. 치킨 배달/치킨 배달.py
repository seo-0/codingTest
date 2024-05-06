from itertools import combinations

def chicken_distance(houses, chickens, m):
    min_distance = float('inf')
    for chicken_comb in combinations(chickens, m):
        current_distance = 0
        for hx, hy in houses:
            current_distance += min(abs(hx-cx) + abs(hy-cy) for cx, cy in chicken_comb)
        min_distance = min(min_distance, current_distance)
    return min_distance

# 입력
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []

# 집과 치킨집 위치 확인
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

# 치킨 거리 계산
answer = chicken_distance(houses, chickens, m)
print(answer)
