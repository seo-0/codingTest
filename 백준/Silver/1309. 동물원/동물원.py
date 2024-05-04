def solve(n):
    # dp 배열 초기화
    dp = [[0] * 3 for _ in range(n + 1)]
    dp[1][0] = 1
    dp[1][1] = 1
    dp[1][2] = 1

    # 다이나믹 프로그래밍을 이용한 계산
    for i in range(2, n + 1):
        dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
        dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
        dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901

    # 결과값 계산
    return (dp[n][0] + dp[n][1] + dp[n][2]) % 9901

# 입력 예시
n = int(input())
print(solve(n))
