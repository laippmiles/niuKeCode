class Solution:
    # s 源字符串
    def cutTheRope(self, length):
        if length < 2:
            return 0
        elif length == 2:
            return 1
        elif length == 3:
            return 2

        ans = {}
        ans[0] = 0
        ans[1] = 1
        ans[2] = 2
        ans[3] = 3
        #前三个初值不是解法，事实上从1-3往下剪乘积只会变得更小了
        #从3以后，f(n)的求法便是f(n) = max(f(i)*f(n-i))
        #从4开始求相应的f(n)，只到length为止

        for i in range(4,length+1):
            max_a = 0
            for j in range(1,i//2 + 1):
                a = ans[j] * ans[i-j]
                if max_a < a:
                    max_a = a
            ans[i] = max_a

        return ans[length]

a = Solution()
print(a.cutTheRope(50))