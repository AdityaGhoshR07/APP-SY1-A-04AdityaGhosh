def knapsack_bottom_up(values, weights, W):
    n = len(values)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


def knapsack_top_down(values, weights, W):
    n = len(values)
    memo = {}

    def solve(i, remaining_weight):
        if i == 0 or remaining_weight == 0:
            return 0

        state = (i, remaining_weight)
        if state in memo:
            return memo[state]

        if weights[i - 1] > remaining_weight:
            res = solve(i - 1, remaining_weight)
        else:
            include = values[i - 1] + solve(i - 1, remaining_weight - weights[i - 1])
            exclude = solve(i - 1, remaining_weight)
            res = max(include, exclude)

        memo[state] = res
        return res

    return solve(n, W)


values = [60, 100, 120]
weights = [10, 20, 30]
W = 50

print("Bottom-Up Result:", knapsack_bottom_up(values, weights, W))
print("Top-Down Result:", knapsack_top_down(values, weights, W))