data= input()
result=[]
value=0

#문자를 하나씩 확인하기
for x in data:
    if x.isalpha(): #알파벳인 경우 리스트에 추가 넣기
        result.append(x)
    else:  #숫자는 따로!!
        value += int(x)
#알파벳 오름차순 정렬!! sorted 랑 차이점(이미 정렬시켜둔) 뭔지 알아두기*
result.sort()

#숫자가 존재한다면 가장 뒤에 넣기
if value!=0:
    result.append(str(value))

#최종 결과 ! 리스트를 문자열로 변환하여 출력하기***쭉 나열해서 출력
print(''.join(result))

