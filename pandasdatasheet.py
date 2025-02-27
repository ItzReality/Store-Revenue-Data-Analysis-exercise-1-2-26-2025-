import pandas as pd

# Load the dataset
df = pd.read_csv('store_sales.csv')

# Calculate total sales by store
total_sales_by_store = df.groupby('Store_Location')['Total_Sales'].sum()
print(total_sales_by_store)

#Compute the mean of the Price column
average_price = df['Price'].mean()
print(f"Average Price: {average_price:.2f}")

#Group by Payment_Method and calculate total sales for each method.
payment_method_sales = df.groupby('Payment_Method')['Total_Sales'].sum()
print(payment_method_sales)

#Transaction Count by Payment Method
transaction_count_by_payment = df.groupby(['Store_Location', 'Payment_Method'])[
    'Transaction_ID'].count()
print(transaction_count_by_payment)

#Quantity Sold by Payment Method
quantity_by_payment = df.groupby(['Store_Location', 'Payment_Method'])[
    'Quantity'].sum()
print(quantity_by_payment)
