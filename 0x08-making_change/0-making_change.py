#!/usr/bin/python3
"""
Task: Change comes from within
Given a pile of coins of different values,
determine the fewest number of coins needed to
meet a given amount total
"""


def makeChange(coins, total):
    # Create a list to store the minimum number of coins needed for each amount from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins needed to make 0 amount

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the minimum number of coins is still infinity, return -1
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
