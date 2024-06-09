def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)): #1이라고 해버리면 자기 자신이랑도 더하는거라 안됨!
            ans = numbers[i] + numbers[j] 
            answer.append(ans)
              
    answer = sorted(set(answer))
    return answer