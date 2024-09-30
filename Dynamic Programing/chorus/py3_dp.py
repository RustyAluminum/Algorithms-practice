def lengthOfLIS(lst):
    dp = []
    for i in range(len(lst)):
        dp.append(1)
        for j in range(i):
            if lst[i] > lst[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp # 每人左边可以站的人数

while True:
    try:
        n, heights = int(input()), list(map(int, input().split()))
        # dp1:每人左边可以站的人数，dp2:每人右边可以站的人数
        dp1, dp2 = lengthOfLIS(heights), lengthOfLIS(heights[::-1])[::-1]
        res = []
        for i in range(len(dp1)):
            res.append(dp1[i] + dp2[i] - 1)
        print(n-max(res))
    except:
        break
