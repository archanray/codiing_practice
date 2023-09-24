class Solution():
    def maxProfit1T(self, prices):
        """
        :type prices: list[int]
        :rtype: int
        """
        if not prices:
            return 0
        smallest_tracker = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] <= smallest_tracker:
                smallest_tracker = prices[i]
            profit = max(profit, prices[i]-smallest_tracker)
        return profit

    def maxProfit2T(self, prices):
        """
        dynamic programming
        compute max profit in 2 transactions
        """
        if not prices:
            return 0

        # init variables
        b1, b2, p1, p2 = float("inf"), float("inf"), 0, 0

        for i in range(len(prices)):
            b1 = min(b1, prices[i])
            p1 = max(p1, prices[i]-b1)

            b2 = min(b2, prices[i]-p1)
            p2 = max(p2, prices[i]-b2)
            print("2T",p2)
        return p2

    def maxProfitKT(self, k, prices):
        """
        dynamic programming
        compute max profit in k transactions
        """
        if not prices:
            return 0

        # init variables
        b = []
        for i in range(k):
            b.append(float("inf"))
        p = []
        for i in range(k):
            p.append(0)

        for i in range(len(prices)):
            b[0] = min(b[0], prices[i])
            p[0] = max(p[0], prices[i]-b[0])

            for j in range(1,k):
                b[j] = min(b[j], prices[i]-p[j-1])
                p[j] = max(p[j], prices[i]-b[j])
                # print("KT",p[j])
        return p[-1]

q = Solution()
# print(q.maxProfit2T([3,3,5,0,0,3,1,4]))
# print(q.maxProfitKT(2,[3,3,5,0,0,3,1,4]))
print(q.maxProfitKT(2, [2,4,1]))
print(q.maxProfitKT(2,[3,2,6,5,0,3]))