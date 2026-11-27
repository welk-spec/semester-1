
import pandas


data = pandas.read_csv("orders_export.csv")

orders = data[data['customer'] == 'Amara Okafor']
print(f"Orders for Amara Okafor: {len(orders)}")