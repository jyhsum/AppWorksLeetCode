class Solution:
    # time: O(N)
    # space: O(N)
    def dp_solution(self, n):
        dp = [0]*(n + 1)
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    # time: O(N)
    # space: O(1)
    def dp_constant_sapce(self, n):
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(2, n):
            tmp = b
            b = a + b
            a = tmp
        return b
    
    def list_all_steps(self, n):
        steps = []
        def dfs(cur_sum, cur_combination, m):
            print(cur_sum)
            print(cur_combination)
            if cur_sum == n:
                steps.append(cur_combination)
                return
            if cur_sum > n:
                return
            for i in range(m, n+1):
                dfs(cur_sum + i, cur_combination + [i], i)
        dfs(0, [], 1)
        return steps

n = 4
steps = Solution().list_all_steps(n)
