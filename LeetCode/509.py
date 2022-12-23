# 509. Fibonacci Number

## Tabulation(bottom-up)
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        # dp: contains results of subproblems
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        

## Memoization(top-down)
class Solution:
    def fib(self, n: int) -> int:
        # dp: contains results of subproblems
        dp = [0] * (n+1)
        def get_fib(k):
            # checking: if dp[k] exists, return it
            if dp[k]:
                return dp[k]
            elif k <= 1:
                dp[k] = k
                return k
            else:
                dp[k] = get_fib(k-1) + get_fib(k-2)
                return dp[k]
        return get_fib(n)