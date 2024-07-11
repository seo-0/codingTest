def solution(s):
    def is_valid(string): #괄호가 유효한지, 짝이 맞는지 체크하는 함수
        stack =[]
        mapping = {')': '(', '}': '{', ']': '['} #매우중요 -> 딕셔너리 구조로, 닫는 괄호를 열린 괄호에 매핑 시키는 것**
        for element in string:
        # 시프트한 괄호를 스택에 넣고, 그걸 반복했을 때 쌍이 맞으면 -> pop
        # 스택에 아무것도 없으면 올바른 문자열
            if element in mapping.values(): #딕셔너리의 벨류들 [, {, (
                stack.append(element)
            elif element in mapping: #딕셔너리의 키 들(닫는 괄호)
                #스택이 비어있거나 최상단 스택이 딕셔너리의 값과 일치하지 않으면 유효X
                if not stack or stack[-1] != mapping[element]: 
                    return False
                stack.pop() #여는 괄호만 pop, 닫는 괄호는 유효성 검사만
        return not stack #stack이 비어있다면 true, 아니면 false -> 비어있다는 것은 짝이 맞았다는 증거이므로!
    cnt = 0
    for i in range(len(s)):
        newstring = s[i:] + s[:i] #i+1이 아닌가?
        if is_valid(newstring):
            cnt += 1
    return cnt            
            
