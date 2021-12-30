import math
import sys


def trade_turkey(prices, k):
    """"Find the optimal way to buy and sell turkeys to maximize
    the total profit.

    Args:
        prices: a list of turkey prices, where prices[i] is the price
        of a turkey on day i.
        k: the maximum number of turkeys you can buy

    Returns:
        a list of up to k non-overlapping trades that gives you the
        max total profit, where each trade is of format (buy_index, sell_index)
    """
    n = len(prices)
    if n <= 1: return []

    mem = {}

    def helper(i,t,k):
        if k == 0 or i == n-1:
            if t == 0:
                mem[(i,0,k)] = (0,None)
                return 0
            else:
                max_price = max(prices[i:])
                index = len(prices) - prices[::-1].index(max_price)
                for j in range(i,index):
                    mem[(j, t, k)] = (max_price, (j+1, t, k))
                mem[(index-1,t,k)] = (max_price,(index,0,k))
                mem[(index,0,k)] = (max_price,None)
                return max_price

        if (i,t,k) in mem:
            revenue,child = mem[(i,t,k)]
            return revenue

        if t == 0:
            # buying
            option1 = -prices[i] + helper(i + 1, 1, k - 1)
            # not doing anything
            option2 = helper(i + 1, 0, k)

            if option1 > option2:
                mem[(i, t, k)] = (option1, (i + 1, 1,k-1))
                return option1
            else:
                child = (i + 1, 0, k)
                mem[(i, t, k)] = (option2, (i + 1, 0, k))
                return option2

        else:
            # selling
            option1 = prices[i] + helper(i + 1, 0, k)
            # not doing anything
            option2 = helper(i + 1, 1, k)

            if option1 > option2:
                mem[(i, t, k)] = (option1, (i + 1, 0,k))
                return option1
            else:
                mem[(i, t, k)] = (option2, (i + 1, 1,k))
                return option2

    revenue = helper(0,0,k)

    state = (0,0,k)
    actions = []

    while state is not None:
        state = mem[state][1]
        if state is None:
            break
        actions.append(state[1])
    trades = []

    i,j = 0,1
    while i < len(actions):
        if actions[i] == 1:
            while j < len(actions):
                if actions[j] == 0:
                    trades.append((i,j))
                    break
                j += 1
            i = j + 1
            j = i
        else:
            i += 1
            j = i


    return trades
