product = {
    'name':"RICE",
    'price':200,
    'quantity':3
}

product2 = {}
product2['name'] = "CARROT"
product2['price'] = 400
product2['quantity'] = 2

print(product2['name'] , product2['price'] , product2['quantity'])
print(product.get('Quantity')) # prints None if key not found
print(product.get('Quantity',"N/A")) # prints N/A if key not found

print("KEYS: ", product2.keys())
print("VALUES: ", product2.values())
