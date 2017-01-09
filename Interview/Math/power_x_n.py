class Solution():
    def power_x_n(self, x, n):
        if n < 0 and n != -n:
            return 1.0 / self.power_x_n(x, -n)
        if n == 0:
            return 1
        v = self.power_x_n(x, n / 2)
        if n % 2 == 0:
            return v * v
        else:
            return v * v * x

S = Solution()
print S.power_x_n(2, -2)