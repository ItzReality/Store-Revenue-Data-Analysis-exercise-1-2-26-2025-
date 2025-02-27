import pandas as pd

# Load the dataset
df = pd.read_csv('store_sales.csv')

# Calculate total sales by store
total_sales_by_store = df.groupby('Store_Location')['Total_Sales'].sum()
print(total_sales_by_store)


average_price = df['Price'].mean()
print(f"Average Price: {average_price:.2f}")


payment_method_sales = df.groupby('Payment_Method')['Total_Sales'].sum()
print(payment_method_sales)


transaction_count_by_payment = df.groupby(['Store_Location', 'Payment_Method'])[
    'Transaction_ID'].count()
print(transaction_count_by_payment)


quantity_by_payment = df.groupby(['Store_Location', 'Payment_Method'])[
    'Quantity'].sum()
print(quantity_by_payment)
