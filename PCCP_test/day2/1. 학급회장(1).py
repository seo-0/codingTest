from collections import defaultdict
def solution(s):
    answer = ""
    sH = defaultdict(int)
    for c in s:
        sH[c] += 1
    
    maxC = 0
    for key in sH:
        if sH[key] > maxC:
            maxC = sH[key]
            answer = key
    
    return answer


print(solution("BACBACCACCBDEDE"))
print(solution("AAAAABBCCDDDD"))
print(solution("AABBCCDDEEABCB"))


