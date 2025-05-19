import importlib
import os
import sys
import json

# Add project paths to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "autocomplete"))
)
app = importlib.import_module("autocomplete.app")

# Simulate an API Gateway event with query parameters
event = {"queryStringParameters": {"q": "fold", "limit": "5", "skip": "1"}}

# Call the lambda_handler function
response = app.lambda_handler(event, None)

# Print formatted response
print("Status Code:", response.get("statusCode"))
print("Response Body:", json.loads(response.get("body")))
