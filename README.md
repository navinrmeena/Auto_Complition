# 🔍 Product Search API (with Autocomplete Support)

This project is a serverless Product Search API implemented as an AWS Lambda function. It allows users to search through a product catalog using a simple query interface with pagination. The search functionality matches the query against both the product title and brand and ranks results using a basic scoring system.

- The Lambda function is written in Python and reads from a products.json file containing product data. It includes logic to:

- Parse query parameters from incoming HTTP requests
  Perform case-insensitive substring matching on product titles and brands
  Score results based on match priority (e.g., if the query appears at the start of the title)
- Return a paginated list of search results
  Handle CORS preflight requests for browser compatibility

---

## 📦 Features

- Search products by `title` or `brand`
- Case-insensitive matching
- Scoring based on prefix matches
- Pagination support (`limit` and `skip`)
- CORS support for browser-based clients

---

## 🧪 Test in Postman

You can quickly test this API via Postman:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/solar-trinity-238607/public/request/t852551/autocomplete-clinikally-api?action=share&creator=28554965&ctx=documentation)

## 🚀 API Endpoint (Deployed on AWS)

```http
GET https://mwmy5yiar8.execute-api.ap-south-1.amazonaws.com/Prod/like/products/search?q=phone&limit=5&skip=0
```

## Reqest

```json
{
  "httpMethod": "GET",
  "queryStringParameters": {
    "q": "phone",
    "limit": "10",
    "skip": "0"
  }
}
```

## Response

```json
{
  "total": 5,

"results":[
      {
          "id": 2,
          "title": "Xiaomi Laptop 401Fold",
          "brand": "Xiaomi",
          "category": "Laptop",
          "price": 602.09,
          "_score": 0
      },
    ....
]
}

```

## 🧪 Local Testing

Clone the Repository

```bash
git clone <your-repo-url>
cd <repo-folder>

```

Install Python (if needed)
Ensure you have Python 3 installed.

### Run Local Test

#### You can test the API locally using the test file present in the root directory:

```bash
python test/test.py

```

## Deployment using AWS SAM

This project is deployed using the AWS Serverless Application Model (SAM), which simplifies the process of building and deploying serverless applications.

1. Defined the Lambda function and its API Gateway endpoint using the template.yaml file.
2. Built the project using sam build, which packaged the function and its dependencies.
3. Deployed the project to AWS using sam deploy, which created the Lambda function, attached it to an API Gateway, and enabled public access.

The API is now live and can be consumed via HTTP requests. It also includes CORS configuration, so it can be accessed from web-based clients (such as React Native Web or browsers) without CORS errors.
