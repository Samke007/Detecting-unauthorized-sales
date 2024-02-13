import requests
import json

# Define the URL of the endpoint
url = 'http://localhost:8000/api/detect_unauthorized_sales/'

# Define the JSON data to send in the POST request
data = {
    "productListings": [{"productID": "123", "authorizedSellerID": "A1"},
                        {"productID": "456", "authorizedSellerID": "A2"},
                        {"productID": "789", "authorizedSellerID": "A3"},
                        {"productID": "101", "authorizedSellerID": "A4"}],
    "salesTransactions": [{"productID": "123", "sellerID": "B2"},
                          {"productID": "456", "sellerID": "A2"},
                         {"productID": "789", "sellerID": "A3"},
                         {"productID": "101", "sellerID": "B4"}]
}

print(data)
# Convert the data to JSON format
json_data = json.dumps(data)

# Define the headers for the request and send it as POST request
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json_data, headers=headers)

# Print the response
print(f'\nResponse: {response.json()}')
