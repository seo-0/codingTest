input_list= input("숫자를 공백으로 구분해서 입력하세요: ").split()
input_list= [int(item) for item in input_list]

#o(N^2)풀이
def func2(arr, N):
    for i in range(N):
        for j in range(i+1, N):
            if arr[i]+arr[j] == 100:
                return 1
    return 0

result= func2(input_list, len(input_list))

if result == 1:
    print("합이 100인 두 수가 있습니다.")
else:
    print("합이 100인 두 수가 없습니다.")

    
#o(N)인 풀이도 존재 