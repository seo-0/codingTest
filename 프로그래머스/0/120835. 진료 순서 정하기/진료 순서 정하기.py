def solution(emergency):
    answer = [0] * (len(emergency))
    count = 0
    emergencyC= emergency.copy()
    # max= max(emergency)
    # 1. 최대값 구하기 - 1번 매칭
    # 1-1 최대값 인덱스에 정답 인덱스 삽입
    # 2. 나머지 중에서 최대값 -2번
    # 3. 나머지 중에서 --반복
    
    for i in emergency:
        maxValue = max(emergencyC) #최대값 추출
        i = emergency.index(maxValue)#최대값 인덱스 추출
        #순위 카운트
        count += 1
        answer[i] = count  # 해당 인덱스에 순위 삽입
        emergencyC.remove(maxValue) #제거 후 다음 값 순회
        
    return answer