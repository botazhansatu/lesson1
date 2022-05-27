


product = {"city": "Москва", "temperature": "20"}
print(product.get("city"))
print(product["city"])

product["temperature"]=int(product["temperature"])-5

print(product)




print(product.get("country"))
print(product.get("country","Россия"))

product["date"]="27.05.2019"

print(product)
print(len(product))
