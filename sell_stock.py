

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp[k][i] = max(dp[k][i-1], prices[i]
        # - prices[j] + dp[k-1][j-1])
        if not len(prices):
            return 0
        dp = [[0 for i in range(len(prices))] for i in
             range(3)]
        for k in range(1, 3):
            maxSoFar = float('-inf')
            for i in range(1, len(prices)):
                maxSoFar = max(maxSoFar, dp[k-1][i-1] 
                               - prices[i-1])
                dp[k][i] = max(dp[k][i-1], 
                               prices[i]+maxSoFar)
        return dp[-1][-1]



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp[k][i] = max(dp[k][i-1], prices[i]
        # - prices[j] + dp[k-1][j-1])
        if not len(prices):
            return 0
        
        dp = [0 for i in range(3)]
        maxSoFar = [float('-inf') for i in range(3)]
        
        for i in range( len(prices)):
            for k in range(1, 3):
                maxSoFar[k] = max(maxSoFar[k], 
                                  dp[k-1] - prices[i] )
                dp[k] = max(dp[k], 
                               prices[i]+maxSoFar[k])
                
        return dp[-1]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = float("inf")
        buy2 = float("inf")
        sell1 = 0
        sell2 = 0
        for i in range(len(prices)):
            buy1 = min(buy1, prices[i])
            sell1 = max(sell1, prices[i]- buy1)
            buy2 = min(buy2, prices[i]-sell1)
            sell2 = max(sell2, prices[i]- buy2)
        return sell2




class Solution:
    
    def quickSolve(self,prices):
        profit =0
        for i in range(1, len(prices)):
            if prices[i]> prices[i-1]:
                profit+= prices[i]-prices[i-1]
        return profit
    
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not len(prices):
            return 0
        
        if k>=len(prices)//2:
             return self.quickSolve(prices)
            
        even = [0 for i in prices]
        odd = [0 for i in prices]
        
        
        for t in range(1, k+1):
            maxSoFar = float('-inf')
            if t%2==1:
                current = odd
                previous = even
            else:
                current = even
                previous = odd
                
            for i in range(1, len(prices)):
                maxSoFar = max(maxSoFar, previous[i-1] - prices[i-1])
                current[i]= max(current[i-1], prices[i]+maxSoFar)
        
        return even[-1] if k%2==0 else odd[-1]