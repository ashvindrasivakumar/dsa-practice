# Problem: Best Time to Buy and Sell Stock
# Approach: Track minimum price and max profit
# Time: O(n) | Space: O(1)

def maxProfit(prices):
    min_price = float('inf')   # smallest price seen so far
    max_profit = 0             # best profit

    for price in prices:
        if price < min_price:
            min_price = price          # buy here (better price)

        profit = price - min_price     # sell today
        max_profit = max(max_profit, profit)

    return max_profit


# Example
print(maxProfit([7,1,5,3,6,4]))  # Output: 5
