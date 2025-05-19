import json
import random

brands = [
    "Apple",
    "Samsung",
    "OnePlus",
    "Xiaomi",
    "Realme",
    "Sony",
    "LG",
    "Motorola",
    "Nokia",
    "Asus",
]
categories = [
    "Smartphone",
    "Tablet",
    "Laptop",
    "Smartwatch",
    "Headphone",
    "TV",
    "Monitor",
    "Camera",
    "Speaker",
]
titles_prefix = [
    "Pro",
    "Max",
    "Ultra",
    "Lite",
    "Mini",
    "Plus",
    "Air",
    "Neo",
    "Edge",
    "Fold",
]

products = []

for i in range(1, 101):
    brand = random.choice(brands)
    category = random.choice(categories)
    model = f"{random.randint(1, 999)}{random.choice(titles_prefix)}"
    title = f"{brand} {category} {model}"
    price = round(random.uniform(100, 2000), 2)

    product = {
        "id": i,
        "title": title,
        "brand": brand,
        "category": category,
        "price": price,
    }
    products.append(product)

with open("./autocomplete/products.json", "w") as f:
    json.dump(products, f, indent=2)

print(" Generated 100 sample products in products.json")
