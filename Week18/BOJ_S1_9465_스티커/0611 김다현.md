import sys
input = sys.stdin.readline

t= int(input())

for _ in range(t):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]
    #처음에는 한칸 건너뛸 수 없으니 무조건 대각선
    if n>1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    for i in range(2,n):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1],dp[0][i-2])
    
    print(max(dp[0][n-1],dp[1][n-1])) #0행, 1행 둘중에 최댓값 선택
        