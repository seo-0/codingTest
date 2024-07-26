#정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 2개의 수를 뽑아 더해 만들 수 있는 모든 수를 배열에 
# 오름차순으로 담아 반환하는 solution( ) 함수를 완성하세요.


def solution(numbers):

    answer =[]
    
    for i in range(len(numbers)):
        for j in range(1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
            # answer(list) += numbers[i] + numbers[j](int) -> 오답(자료형 다름)

    answer = sorted(set(answer))
    return answer
