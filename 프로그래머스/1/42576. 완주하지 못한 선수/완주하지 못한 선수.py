def solution(participant, completion):
    # 10의 4승이라서 시간복잡도 O(N^2) 안됨
    for people in participant:
        if people in completion:
            completion.remove(people) # 제거의 시간복잡도 O(N)임 따라서 최종 -> N^2이라서 안됨
        else:
            return people