import os
import pprint


def main():
    lst1 = [7, 1, 5, 3, 6, 4]
    lst2 = [7, 6, 3, 4, 11, 6]
    lst3 = [2, 3, 10, 6, 4, 8, 1]
    p1 = maxprofit(lst3)

def maxprofit(lst):

    (profit, cost) = (0, float('inf'))

    for price in lst:
        cost = min(cost, price)
        print("Cost is {}".format(cost))
        current_profit = price - cost
        profit = max(profit, current_profit)
        print("Profit is {}".format(profit))
    return profit

if __name__ == '__main__':
    #print("hello")
    main()


