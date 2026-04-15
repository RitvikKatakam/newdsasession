def buy_and_sell_stocks(prices):
    if not prices:
        return 0

    min_price = prices[0]
    min_index = 0
    max_profit = 0
    buy_day = 0
    sell_day = 0

    for i, price in enumerate(prices):
        if price - min_price > max_profit:
            max_profit = price - min_price
            buy_day = min_index
            sell_day = i
        if price < min_price:
            min_price = price
            min_index = i

    return max_profit, buy_day, sell_day

# example usage
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    profit, buy_day, sell_day = buy_and_sell_stocks(prices)
    print("Maximum profit:", profit)
    if profit > 0:
        print("Buy on day", buy_day + 1, "at price", prices[buy_day])
        print("Sell on day", sell_day + 1, "at price", prices[sell_day])
    else:
        print("No profitable buy/sell opportunity")