def solution(numbers, target):
    def dfs(index, currentSum):
        if index == len(numbers):
            return 1 if target == currentSum else 0
        else:
            return dfs(index+1, currentSum + numbers[index]) + dfs(index+1, currentSum - numbers[index]) 
    

    return dfs(0,0)








