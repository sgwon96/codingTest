def solution(money):
    def linear_solution(money):
        dp = [money[0], money[0]]
        for i in range(2, len(money)):
            dp.append(max(dp[i - 1], dp[i - 2] + money[i]))
        return max(dp)

    return max(linear_solution(money[1:]), linear_solution(money[:-1]), linear_solution(money[2:]))