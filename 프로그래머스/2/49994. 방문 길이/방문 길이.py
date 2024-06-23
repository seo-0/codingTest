def solution(dirs):
    # 현재 위치
    x, y = 0, 0
    
    # 이동 경로를 저장할 집합 (중복 경로를 피하기 위해)
    visited = set()
    
    # 각 방향에 대한 이동 변화
    moves = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    
    for direction in dirs:
        # 현재 위치
        curr_x, curr_y = x, y
        
        # 이동할 위치
        move_x, move_y = moves[direction]
        new_x, new_y = curr_x + move_x, curr_y + move_y
        
        # 이동할 위치가 경계를 벗어나지 않는지 확인
        if -5 <= new_x <= 5 and -5 <= new_y <= 5:
            # 경로를 양방향으로 저장 (출발->도착, 도착->출발)
            visited.add((curr_x, curr_y, new_x, new_y))
            visited.add((new_x, new_y, curr_x, curr_y))
            
            # 새로운 위치로 이동
            x, y = new_x, new_y
    
    # 경로의 수를 반환 (양방향으로 저장했으므로 /2)
    return len(visited) // 2
