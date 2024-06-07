# def solution(arr):
#     #그냥 set만 쓰면 집합{} 자료형이 되어버림
#     answer = list(dict.fromkeys(arr)) #출력이 리스트라 리스트로 마지막 변환 필수
#    => 이 풀이가 틀린 이유는 전체 원소들에 대해 중복을 체크해버리기 때문 1이 처음에 나오고 뒤에 1이 또있으면 이걸 합쳐서 하나로 간주해버림
#     return answer
def solution(arr):
    if not arr:
        return []
    
    answer=[]
    cnt = 0
    
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i-1]:
            answer.append(arr[i])
            cnt +=1
            
    return answer