# Stock Portfolio Tracker

prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 140,
    "AMZN": 160
}

stock = input("Enter stock name: ").upper()
qty = int(input("Enter quantity: "))

if stock in prices:
    total = prices[stock] * qty
    print("Stock Price =", prices[stock])
    print("Total Investment Value =", total)

    # Save result in txt file
    file = open("portfolio.txt", "w")
    file.write("Stock Name: " + stock + "\n")
    file.write("Quantity: " + str(qty) + "\n")
    file.write("Price: " + str(prices[stock]) + "\n")
    file.write("Total Value: " + str(total))
    file.close()

    print("Data saved in portfolio.txt")

else:
    print("Stock not found")
    