# Store-Revenue-Data-Analysis-exercise-1-2-26-2025-
After completing the first module in the google Data Analytics certificate combining my prior knowledge this was my first exercise 2/26/2025 



Proposed Problem:
You are a data analyst at a retail company, and you’ve been given a dataset containing customer transactions. Your goal is to analyze sales performance, identify trends, and provide insights. However, before you can perform any analysis, you need to clean the data.

Dataset Overview:
The dataset contains the following columns:

Transaction_ID: Unique identifier for each transaction.
Customer_ID: Unique identifier for each customer.
Transaction_Date: Date the transaction occurred.
Product_ID: Identifier for the product purchased.
Product_Name: Name of the product.
Price: Price of the product.
Quantity: Number of items purchased.
Total_Sales: Total price of the transaction (Price * Quantity).
Payment_Method: The method used to make the payment (e.g., Cash, Credit Card, Debit Card).
Store_Location: The store where the transaction took place (e.g., "Store_A", "Store_B").




1. Total Sales Calculation:
The first step was to calculate total sales for both stores to understand how much revenue each store generated.


Results:

Store A: $394.80
Store B: $184.92
Total Sales (Both Stores): $579.72



2. Average Price Calculation:
Next, I calculated the average price of products across all transactions.


Results:

Average Price across both stores: $16.18 (rounded to $16.2)


Store Comparison - Why Store A Excels:
Upon further investigation, it was observed that Store A was performing better due to significantly higher sales in cash payments.

Store A’s cash sales: $189.90
Store B’s cash sales: $79.92
Difference in Cash Sales: $109.98 more in Store A.
This significant difference in cash sales suggests that Store A might have:

Larger transactions when paid in cash.
A larger customer base that prefers cash payments.

this information was obtained via:

4. Payment Method Analysis:
To better understand how payment methods impacted sales, I used groupby(see py file) to break down the sales by payment method across both stores.

Results:

Cash was the highest contributor to Store A’s sales, followed by Credit Cards.
Store A significantly outperformed Store B in cash payments, contributing $109.98 more to its total sales.



5. Further Analysis
Transaction Count and Quantity:
To gain deeper insights, I also analyzed the number of transactions and the total quantity sold by payment method.

This additional analysis helped reveal that Store A had a higher transaction volume and quantity sold for cash payments.

Insights & Business Implications:
Key Insights:
Store A’s success is largely driven by its cash transactions, which totaled $189.90, significantly outperforming Store B’s cash sales of $79.92.
Despite Credit Cards being the second-highest payment method, the dominance of cash in Store A points to the possibility of higher-value transactions or more frequent cash-paying customers.
Store B, while performing well with credit card payments, does not generate as much revenue from cash transactions, which may indicate smaller transactions or a different customer demographic.
Business Implications:
Cash payments in Store A suggest that this store may benefit from cash-based promotions or targeted marketing that encourages customers to make larger purchases with cash.
Store B could consider strategies to increase cash transactions or focus on boosting credit card purchases with promotions or loyalty programs.
Further analysis on customer demographics or seasonal trends could provide additional insights into why Store A has more cash transactions.


Conclusion:
This analysis highlights the critical role that payment methods, especially cash, play in determining a store’s total sales. By exploring payment method trends and grouping by multiple factors, we can gain actionable insights into a store’s performance, which could guide strategic decisions for improving sales in both Store A and Store B.


Tools Used:
Pandas: For data manipulation, cleaning, and analysis.
Python: For performing calculations and running the analysis.
CSV File/Excel: The dataset used for the analysis was stored in CSV format for easy processing.
