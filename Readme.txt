# Stock Portfolio Tracker with Business Analysis

## Project Overview

**Stock Portfolio Tracker with Business Analysis** is a Python-based application that helps users manage and analyze their stock investments.

The application allows users to add stocks, view their portfolio, analyze current stock prices, calculate investment value, profit or loss, return percentage, and classify stock performance.

The project uses **CSV file handling** to store portfolio data and the **yfinance** library to retrieve current market prices.

---

## Features

### 1. Add Stock

Users can add a stock by entering:

* Stock Symbol
* Quantity
* Buy Price

The information is stored in `portfolio.csv`.

Example:

```text
TCS.NS,10,3500
```

---

### 2. View Portfolio

Users can view their stored stocks with:

* Stock Name
* Stock Quantity
* Stock Price

Example:

```text
----- Portfolio -----

Stock Name     : TCS.NS
Stock Quantity : 10
Stock Price    : ₹3500
```

---

### 3. Portfolio Analysis

The application uses `yfinance` to retrieve the latest available stock price.

It calculates:

* Total Investment
* Current Portfolio Value
* Profit/Loss
* Return Percentage
* Highest Price
* Lowest Price
* Average Price

---

### 4. Profit/Loss Status

Each stock is classified based on its profit or loss.

```text
Profit > 0  → Profit
Profit < 0  → Loss
Profit = 0  → No Profit No Loss
```

---

### 5. Performance Category

The project classifies stocks based on their return percentage.

| Return Percentage | Performance    |
| ----------------- | -------------- |
| 15% or above      | High Performer |
| 5% to below 15%   | Good Performer |
| 0% to below 5%    | Stable         |
| Below 0%          | Loss Making    |

These categories are simple business-analysis rules defined within the project.

---

### 6. Business Analysis

The project provides a basic business view of the portfolio.

It identifies:

* Number of profitable stocks
* Number of loss-making stocks
* Highest current stock price
* Lowest current stock price
* Average current stock price
* Overall portfolio profit/loss
* Overall portfolio return

This helps convert raw stock data into useful business information.

---

### 7. Delete Stock

Users can delete a stock by entering its stock symbol.

Example:

```text
Enter Stock Symbol to delete: INFY.NS

Stock deleted successfully.
```

---

## Technologies Used

* **Python**
* **CSV**
* **yfinance**
* **Pandas**
* **File Handling**
* **Conditional Statements**
* **Loops**
* **Functions**

---

## Python Libraries

The project mainly uses:

```python
import csv
import yfinance as yf
```

Install `yfinance` using:

```bash
pip install yfinance
```

---

## Project Structure

```text
StockPortfolio-Tracker/
│
├── stock_portfolio.py
├── portfolio.csv
└── README.md
```

### `stock_portfolio.py`

Contains the complete Python application.

### `portfolio.csv`

Stores stock information such as:

```text
Stock Symbol, Quantity, Buy Price
```

### `README.md`

Contains project documentation and instructions.

---

## How to Run the Project

### Step 1: Install Python

Make sure Python is installed on your computer.

Check the Python version:

```bash
python --version
```

---

### Step 2: Install Required Library

Run:

```bash
pip install yfinance
```

---

### Step 3: Run the Python Program

Run:

```bash
python stock_portfolio.py
```

---

## Main Menu

After running the program, the following menu appears:

```text
===== Stock Portfolio Tracker =====
1. Add Stock
2. View Portfolio
3. Portfolio Analysis
4. Delete Stock
5. Exit
```

---

## Example

### Add Stock

```text
Enter Stock Symbol (e.g. TCS.NS): TCS.NS
Enter Quantity: 10
Enter Buy Price: 3500

Stock Added Successfully
```

### Portfolio Analysis

The application can display:

```text
----- Stock Analysis -----

Stock: TCS.NS
Buy Price: ₹3500.00
Current Price: ₹3900.00
Current Value: ₹39000.00
Profit/Loss: ₹4000.00
Return Percentage: 11.43%
Status: Profit
Performance: Good Performer
```

---

## Business Analysis Example

```text
----- Business Analysis -----

Profitable Stocks: 3
Loss Making Stocks: 1
Highest Price: ₹3900.00
Lowest Price: ₹1500.00
Average Price: ₹2700.00
```

This gives the user a quick summary of portfolio performance.

---

## Key Calculations

### Investment

```text
Investment = Quantity × Buy Price
```

### Current Value

```text
Current Value = Quantity × Current Price
```

### Profit/Loss

```text
Profit/Loss = Current Value − Investment
```

### Return Percentage

```text
Return % = (Profit/Loss ÷ Investment) × 100
```

---

## Learning Outcomes

Through this project, I practiced:

* Python programming
* Functions
* Loops
* Conditional statements
* CSV file handling
* Reading and writing files
* Working with external data using `yfinance`
* Financial calculations
* Data analysis
* Business analysis
* Basic portfolio performance classification

---

## Future Enhancements

The project can be improved further by adding:

* Pandas-based data analysis
* Stock-wise comparison charts
* Profit/Loss visualization
* Investment distribution charts
* Portfolio dashboard
* Date-wise portfolio tracking
* Data export to Excel
* Search and update stock functionality
* Better validation for invalid stock symbols
* Risk analysis
* Sector-wise portfolio analysis

---


