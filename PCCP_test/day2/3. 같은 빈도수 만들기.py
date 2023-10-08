from collections import Counter
def solution(s):
    answer = []
    sH = Counter(s)
    maxN = float("-inf")
    for x in "abcde":
        if sH[x] > maxN:
            maxN = sH[x]

    for x in "abcde":
        answer.append(maxN-sH[x])
        
    return answer


print(solution("aaabc"))
print(solution("aabb"))
print(solution("abcde"))
print(solution("abcdeabc"))
print(solution("abbccddee"))
