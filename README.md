# Detecting-unauthorized-sales
A solution to identify unauthorized sales transactions from provided datasets of product listings and actual sales records based on RESTful principles.


## Task overview
The task is to develop a REST API endpoint that processes POST requests containing two lists: one containing product listing (including product ID and authorized seller ID) and the other actual sales transactions (including product ID and seller ID). Your task is to develop an algorithm that identifies any sales transactions made by unauthorized seller.


## Project Setup:
- The project is structured using Django's framework, which provides a well-defined architecture for web applications.
-  Inside the project directory (unauthorized_sales_detection), there's a separate app called sales_detection. This app contains the models, views, and URLs related to unauthorized sales detection.


## API Endpoint:
- The core functionality is implemented in the detect_unauthorized_sales view.
- This view is decorated with @csrf_exempt to allow handling POST requests without requiring CSRF tokens. This is appropriate for APIs that are consumed by clients that may not provide CSRF tokens, such as JavaScript frontends or external services.
- The view expects a POST request with JSON data containing lists of product listings and sales transactions.
- It retrieves the data from the request body using json.loads(request.body).
- It then iterates through the sales transactions and checks if each transaction is authorized by querying the ProductListing model.
- If a sales transaction is unauthorized, it adds it to the unauthorized_sales list.
- Finally, it returns a JSON response containing the unauthorized sales found in the input data.


## Prerequisites
Install Django: "pip install django"


## Testing
1. Open Terminal and navigate to skai-labs-task-2/unauthorized_sales_detection/
2. Run command: python manage.py runserver
3. Open another Terminal and run command "python send_post_request.py"
4. Check the output and see the received response based on the data defined in the send_post_request.py file
