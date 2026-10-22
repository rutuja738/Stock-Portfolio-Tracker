
import csv
import yfinance as yf

FILE_NAME = "portfolio.csv"


# Add Stock
def add_stock():
    symbol = input("Enter Stock Symbol (e.g. TCS.NS): ").upper()
    quantity = int(input("Enter Quantity: "))
    buy_price = float(input("Enter Buy Price: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([symbol, quantity, buy_price])

    print("Stock Added Successfully")


# View Portfolio
def view_portfolio():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\n----- Portfolio -----")

            for row in reader:
                stock_name = row[0]
                stock_quantity = row[1]
                stock_price = row[2]

                print("\nStock Name     :", stock_name)
                print("Stock Quantity :", stock_quantity)
                print("Stock Price    : ₹", stock_price)
                print("-----------------------------")
                
                

    except FileNotFoundError:
        print("No Portfolio Data Found")



# Portfolio Analysis
def portfolio_analysis():

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            total_investment = 0
            current_value = 0

            prices = []

            # New variables
            profit_count = 0
            loss_count = 0

            print("\n----- Stock Analysis -----")

            for row in reader:

                symbol = row[0]
                quantity = int(row[1])
                buy_price = float(row[2])

                stock = yf.Ticker(symbol)

                current_price = stock.history(
                    period="1d"
                )["Close"].iloc[-1]

                investment = quantity * buy_price
                value = quantity * current_price

                total_investment += investment
                current_value += value

                prices.append(current_price)

                # Profit or Loss
                profit = value - investment

                # Return Percentage
                return_percentage = (profit / investment) * 100

                # Profit/Loss Status
                if profit > 0:
                    status = "Profit"
                    profit_count += 1

                elif profit < 0:
                    status = "Loss"
                    loss_count += 1

                else:
                    status = "No Profit No Loss"

                # Performance Category
                if return_percentage >= 15:
                    category = "High Performer"

                elif return_percentage >= 5:
                    category = "Good Performer"

                elif return_percentage >= 0:
                    category = "Stable"

                else:
                    category = "Loss Making"

                # Display stock analysis
                print(f"\nStock: {symbol}")
                print(f"Buy Price: ₹{buy_price:.2f}")
                print(f"Current Price: ₹{current_price:.2f}")
                print(f"Current Value: ₹{value:.2f}")
                print(f"Profit/Loss: ₹{profit:.2f}")
                print(f"Return Percentage: {return_percentage:.2f}%")
                print(f"Status: {status}")
                print(f"Performance: {category}")

            # Overall portfolio calculation
            profit_loss = current_value - total_investment

            overall_return = (
                profit_loss / total_investment
            ) * 100

          
            # Business Analysis
            print("\n----- Business Analysis -----")
            print(f"Profitable Stocks: {profit_count}")
            print(f"Loss Making Stocks: {loss_count}")

            print(f"Highest Price: ₹{max(prices):.2f}")
            print(f"Lowest Price: ₹{min(prices):.2f}")
            print(f"Average Price: ₹{sum(prices)/len(prices):.2f}")

    except FileNotFoundError:
        print("No Portfolio Data Found")

# Delete Stock
def delete_stock():

    symbol_to_delete = input(
        "Enter Stock Symbol to delete: "
    ).upper()

    try:
        with open(FILE_NAME, "r") as file:
            rows = list(csv.reader(file))

        found = False
        new_rows = []

        for row in rows:

            if row[0].upper() == symbol_to_delete:
                found = True
            else:
                new_rows.append(row)

        if found:

            with open(FILE_NAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(new_rows)

            print("Stock deleted successfully.")

        else:
            print("Stock not found.")

    except FileNotFoundError:
        print("No Portfolio Data Found")
        
# Main Menu
while True:

    print("\n===== Stock Portfolio Tracker =====")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Portfolio Analysis")
    print("4. Delete Stock")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_stock()

    elif choice == "2":
        view_portfolio()

    elif choice == "3":
        portfolio_analysis()
        
    elif choice == "4":
         delete_stock()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")