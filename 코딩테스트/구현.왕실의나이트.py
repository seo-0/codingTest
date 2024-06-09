input_data= input()
row= int(input_data[1])
column= int(ord(input_data[0]))- int(ord('a'))+1

#말이 이동할 수 있는 8가지 스텝 정의!
steps=[(-2,-1), (-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

#8가지 방향에 대해 각 위치로 이동이 가능한지 확인!
result=0
for step in steps:
    #이동하고자 하는 위치 확인
    next_row= row+step[0]
    next_column= column+step[1]

    #해당 위치로 이동이 가능하다면 cnt 증가! 
    # 위치 체크를 다음 열과행이 있는지 체크를 해야하기때문에
    #1보다 크거나 8보다 작거나 같은 조건안에 있다면 결과값 카운트 해주는것임!
    if next_row >=1 and next_row<=8 and next_column>=1 and next_column<=8:
        result +=1

print(result)