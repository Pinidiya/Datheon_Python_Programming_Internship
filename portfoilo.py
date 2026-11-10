import csv

stock_symbols = []

with open("sp500_stocks.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        stock_symbols.append(row["Symbol"])

print("S&P 500 Dataset Loaded Successfully!")

portfolio={}

print("\n===INVESTMENT PORTFOLIO TRACKER===")
while True:
    ticker=input("\nEnter Stock Symbol: ").upper()

    if ticker not in stock_symbols:
        print("Invalid Stock Symbol! Please enter a valid S&P 500 symbol.")
        continue

    buy_price=float(input("Enter Buy Price: "))
    quantity=int(input("Enter shre quantity: "))
    currenet_price=float(input("Enter Current share price: "))

    if buy_price<=0 or quantity <= 0 or currenet_price<0:
        print("Invalied value,Please enter valid numbers.")
        continue

    portfolio[ticker]={
        "buy_price": buy_price,
        "quantity": quantity,
        "current_price": currenet_price
    }

    choice=input("\nDo you want to add another stock? (yes/no): ").lower()

    if choice !="yes":
        break

total_investment=0
total_market_value=0

results = []

for ticket,details in portfolio.items():

        buy_price=details["buy_price"]
        quantity=details["quantity"]
        current_price=details["current_price"]

        invested=buy_price * quantity
        market_value=current_price * quantity

        profit_loss=market_value-invested
        percentage=(profit_loss/invested)* 100

        total_investment += invested
        total_market_value += market_value

        results.append([
            ticket,
            buy_price,
            quantity,
            current_price,
            invested,
            market_value,
            profit_loss,
            percentage,

        ])

total_pofit_loss = total_market_value - total_investment

total_percentage =(
            (total_pofit_loss / total_investment) * 100
        )

print("\n================PORTFOILO SUMMARY=============")

print(
    f"{'Stock':<10}"
    f"{'Invested':<15}"
    f"{'Market Value':<15}"
    f"{'Profit/Loss':<15}"
    f"{'Gain/Loss %':<12}"  
        )

for row in results:
    print(

        f"{row[0]:<10}"
        f"{row[4]:<15.2f}"
        f"{row[5]:<15.2f}"
        f"{row[6]:<15.2f}"
        f"{row[7]:<12.2f}"
            )
print("---------------------------------------")
print(f"Total Investment : ${total_investment:.2f}")
print(f"Total Market Value: ${total_market_value:.2f}")
print(f"Total Profit/Loss : ${total_pofit_loss:.2f}")
print(f"Total Gain/Loss % : {total_percentage:.2f}%") 

with open("portfolio_summary.csv","w",newline="")as file:

    writer = csv.writer(file)

    writer.writerow([
        "Stock Symbol",
        "Buy Price",
        "Quantity",
        "Current Price",
        "Total Invested",
        "Market Value",
        "Profit/Loss",
        "Gain/Loss Percentage"
    ])

    writer.writerows(results)

    writer.writerow([])
    writer.writerow(["TOTAL","","","",
                     total_investment,
                     total_market_value,
                     total_pofit_loss,
                     total_percentage])
print("\nPortfolio Summary saved to portfolio_summary.csv")

