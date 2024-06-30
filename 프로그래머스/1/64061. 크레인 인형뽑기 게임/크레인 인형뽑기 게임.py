def solution(board, moves):
    # 1. 선언: 인형 담을 바구니 선언
    basket = []
    # 2. 선언: 인형이 같으면 터져서 사라지는 개수 셀 정답 배열 =result!
    result = 0
    # 3. moves에 따라서 board 수를 basket으로 옮기기
    for move in moves:
        #1,5,3...에서 뽑은 원소 넣을 배열 board[row][column]
        column = move -1 #인덱스는 -1 해줘야함! *빼먹음 주의
        # 해당 열(column)에서 가장 위에 있는 인형을 찾는 과정
        for row in range(len(board)):
            if board[row][column] != 0: # 0이 아니면 인형이 있는 것
                doll = board[row][column]
                board[row][column] = 0 # 제거했으니까 0으로!
                #basket.append(doll) -> ** 여기에 바로 추가하는게 아니라! 같은지 다른지 확인하고 같으면 제거 해야하니깐 추가로직이 필요해서 아래에 조건문 넣어야함!!!
                #바구니에 인형 추가하고, 연속된지 확인
                if basket and basket[-1] == doll: #종류가 같으면
                    basket.pop() #종류가 같아서 터트려지고 사라짐
                    result += 2
                else:
                    basket.append(doll)
                break #얘가 있고 없고 차이가 매우 중요! 가장 위의 인형을 찾았으므로 다음 Move로 넘어가는 역할임!     
          #  basket = board[min()][move] -> 이게 아니라 반복문으로 요소에 접근해야함 한번에 최소값으로 접근하는게 아님!
    return result