from urllib.request import urlopen
import json

total_revenue = 0.0
url='https://shopicruit.myshopify.com/admin/orders.json?page=1&access_token=c32313df0d0ef512ca64d5b336a0d7c6'

response = urlopen(url)
data = response.read().decode("utf-8")
jdata = json.loads(data)
orders=jdata['orders']
for item in orders:
    total_revenue+=float(item["subtotal_price"])
print(total_revenue)