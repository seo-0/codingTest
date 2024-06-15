def solution(arr1, arr2):
    #answer =[[]] #현재 빈리스트를 포함한 1X0임. 초기화 해주어야함 주의
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])): #열의개수
            for k in range(len(arr2)): #행의개수
                answer[i][j] += arr1[i][k] * arr2[k][j]
        
    return answer