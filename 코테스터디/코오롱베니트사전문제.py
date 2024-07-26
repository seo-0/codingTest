# def solution(v):

#     x = [x[0] for x in v]
#     y = [y[1] for y in v]

#     if x.count(x) and y.count(y)!= 2:
#         answerX, answerY = x, y

        
#     return [answerX, answerY]

def solution(v):
    x = [point[0] for point in v]
    y = [point[1] for point in v]

    # 네 번째 점의 x 좌표를 찾습니다
    if x.count(x[0]) != 2:
        answerX = x[0]
    elif x.count(x[1]) != 2:
        answerX = x[1]
    else:
        answerX = x[2]

    # 네 번째 점의 y 좌표를 찾습니다
    if y.count(y[0]) != 2:
        answerY = y[0]
    elif y.count(y[1]) != 2:
        answerY = y[1]
    else:
        answerY = y[2]

    return [answerX, answerY]

# 테스트
v = [[1, 4], [3, 4], [3, 10]]
print(solution(v))  # [1, 10]