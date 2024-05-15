def solution(phone_book):
# 폰북의 요소들 중 앞에 겹치는게 있으면 false 반환
# 해시 자료구조 사용
    
    phone_set = set(phone_book) # 해시셋에 저장(중복 허용X)
    
    for phone in phone_book:
        for i in range(1, len(phone)):
            if phone[:i] in phone_set:
                return False
    return True
    
    