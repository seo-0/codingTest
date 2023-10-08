from collections import Counter
def solution(s):
    answer = -1
    sH = Counter(s)
    
    for i in range(len(s)):
        if sH[s[i]] == 1:
            return i+1;
    
    return answer


print(solution("statitsics"))
print(solution("aabb"))
print(solution("stringshowtime"))
print(solution("abcdeabcdfg"))


