class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #initialize min price to infinity
        min_price = float('inf')

        #initialize max profit to 0
        max_profit = 0

        #loop thru prices
        for current_price in prices:
            if current_price < min_price:
                #update min_price to current price if lower than current
                min_price = current_price

            #calculate potential profit if sell that day
            potential_profit = current_price - min_price

            #update max profit if calculated profit is higher than current max
            if potential_profit > max_profit:
                max_profit = potential_profit

        return max_profit