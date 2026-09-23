Project: Stock Portfolio Tracker
---------------------------*****************-----------------------------
Step 1: Create Project Folder ---> StockPortfolioTracker

Step 2: Create Python File ----> stock_portfolio.py
Step 3: Create notebook file ---> Support_run.ipynb
Step 4: Install Required Library in notebook Support_run.ipynb
pip install yfinance pandas
-------------------------------****************************--------------------
Step 5: code
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
                print(row)

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

            print("\n----- Stock Analysis -----")

            for row in reader:

                symbol = row[0]
                quantity = int(row[1])
                buy_price = float(row[2])

                stock = yf.Ticker(symbol)

                current_price = stock.history(period="1d")["Close"].iloc[-1]

                investment = quantity * buy_price
                value = quantity * current_price

                total_investment += investment
                current_value += value

                prices.append(current_price)

                print(f"\nStock: {symbol}")
                print(f"Buy Price: ₹{buy_price:.2f}")
                print(f"Current Price: ₹{current_price:.2f}")
                print(f"Current Value: ₹{value:.2f}")

            profit_loss = current_value - total_investment

            print("\n========================")
            print(f"Total Investment: ₹{total_investment:.2f}")
            print(f"Current Value: ₹{current_value:.2f}")
            print(f"Profit/Loss: ₹{profit_loss:.2f}")

            print(f"Highest Price: ₹{max(prices):.2f}")
            print(f"Lowest Price: ₹{min(prices):.2f}")
            print(f"Average Price: ₹{sum(prices)/len(prices):.2f}")

    except FileNotFoundError:
        print("No Portfolio Data Found")


# Main Menu
while True:

    print("\n===== Stock Portfolio Tracker =====")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Portfolio Analysis")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_stock()

    elif choice == "2":
        view_portfolio()

    elif choice == "3":
        portfolio_analysis()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")


--------------------------*****************************-----------------------
Step 6: Run Project
method 1:
Open Terminal:

Shell
cd StockPortfolioTracker
python stock_portfolio.py

----------------*****************************----------------------------------
 method 2:Run the .py file from Jupyter Notebook

Open your notebook and create a new cell:

%run stock_portfolio.py
Shift + Enter


