from collections import deque

def solution(cards1, cards2, goal):
    cards1= deque(cards1)    
    cards2= deque(cards2)
    goal= deque(goal)
    
# 카드1과 2에서 순차적으로 goal과 같으면 pop
    for i in range(len(goal)):
        if cards1 and cards1[0] == goal[0]:
            cards1.popleft()
            goal.popleft()
        elif cards2 and cards2[0] == goal[0]:
            cards2.popleft()
            goal.popleft()
        else:
            break
            
    if not goal:
        return "Yes"
    else:
        return "No"
    
    
    
    
    return answer