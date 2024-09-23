#!/usr/bin/python3
"""
Task: Change comes from within
Given a pile of coins of different values,
determine the fewest number of coins needed to
meet a given amount total
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.
    Return: fewest number of coins needed to meet total
        - If total is 0 or less, return 0
        - If total cannot be met by any number of coins you have, return -1
        - Coins is a list of the values of the coins in your possession
        - The value of a coin will always be an integer greater than 0
        - You can assume you have an infinite number of each denomination of
        coin in the list
    """
    n_coins = 0
    if total <= 0:
        return n_coins
    coins.sort(reverse=True)
    while (total > 0 and coins):
        n = int(total / coins[0])
        total = total - (coins[0] * n)
        n_coins = n_coins + n
        coins.remove(coins[0])
    if total != 0:
        return -1
    return n_coins