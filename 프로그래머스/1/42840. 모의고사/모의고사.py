def solution(answers):
    pattern = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    score = [0] * 3
    
    # 점수 계산
    for i in range(len(answers)):
        for j in range(len(pattern)):
            if answers[i] == pattern[j][i % len(pattern[j])]:
                score[j] += 1
    
    maxScore = max(score)
    answer = []
    
    # 가장 높은 점수를 받은 사람 찾기
    for i in range(len(score)):
        if score[i] == maxScore:
            answer.append(i + 1)  # 사람 번호는 1부터 시작
    
    return sorted(answer)
