import json
import os

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

    results.sort(key=lambda x: x["_score"], reverse=True)
    total = len(results)
    return {"total": total, "results": results[skip : skip + limit]}


def lambda_handler(event, context):
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type",
    }

    if event.get("httpMethod") == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps({"message": "CORS preflight successful"}),
        }

    params = event.get("queryStringParameters") or {}
    q = params.get("q")
    limit = int(params.get("limit", 10))
    skip = int(params.get("skip", 0))

    if not q or len(q) < 2:
        return {
            "statusCode": 400,
            "headers": headers,
            "body": json.dumps({"error": "Query must be at least 2 characters long."}),
        }

    result = search_products(PRODUCTS, q, limit, skip)

    return {
        "statusCode": 200,
        "headers": headers,
        "body": json.dumps(result),
    }
