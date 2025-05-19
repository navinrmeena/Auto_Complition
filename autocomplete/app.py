import json
import os
import sys

current_dir = os.path.dirname(__file__)
json_path = os.path.join(current_dir, "products.json")

with open(json_path, "r") as f:
    PRODUCTS = json.load(f)


def search_products(products, query, limit, skip):
    q = query.lower()

    results = []
    for product in products:
        title = product["title"].lower()
        brand = product["brand"].lower()

        if q in title or q in brand:
            score = 0
            if title.startswith(q):
                score += 2
            if brand.startswith(q):
                score += 1
            product["_score"] = score
            results.append(product)

    # Sort by score descending
    results.sort(key=lambda x: x["_score"], reverse=True)
    total = len(results)
    return {"total": total, "results": results[skip : skip + limit]}


def lambda_handler(event, context):
    params = event.get("queryStringParameters") or {}
    q = params.get("q")
    limit = int(params.get("limit", 10))
    skip = int(params.get("skip", 0))

    if not q or len(q) < 2:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Query must be at least 2 characters long."}),
        }

    result = search_products(PRODUCTS, q, limit, skip)

    return {
        "statusCode": 200,
        "body": json.dumps(result),
        "headers": {"Content-Type": "application/json"},
    }
