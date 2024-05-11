def solution(participant, completion):
    #해시테이블을 어떻게 적용?
    hash = {}
    for p in participant:
        if p in hash:
            hash[p] += 1
        else:
            hash[p] = 1
    
    for c in completion:
        if c in hash:
            hash[c] -= 1
            
    for p in hash:
        if hash[p] > 0: # 완주하지 못한 사람 추출
            return p
            
    