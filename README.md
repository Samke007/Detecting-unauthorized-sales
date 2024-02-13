# Detecting-unauthorized-sales
A solution to identify unauthorized sales transactions from provided datasets of product listings and actual sales records based on RESTful principles.


## Task overview
The task is to develop a REST API endpoint that processes POST requests containing two lists: one containing product listing (including product ID and authorized seller ID) and the other actual sales transactions (including product ID and seller ID). Your task is to develop an algorithm that identifies any sales transactions made by unauthorized seller.


## Prerequisites
Install Django: "pip install django"


## Testing
1. Open Terminal and navigate to skai-labs-task-2/unauthorized_sales_detection/
2. Run command: python manage.py runserver
3. Open another Terminal and run command "python send_post_request.py"
4. Check the output and see the received response based on the data defined in the send_post_request.py file
