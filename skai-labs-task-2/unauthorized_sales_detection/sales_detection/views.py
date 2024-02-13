from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductListing, SalesTransaction
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def detect_unauthorized_sales(request) :
    if request.method == 'POST':
        data = json.loads(request.body)
        product_listings = data.get('productListings', [])
        sales_transactions = data.get('salesTransactions', [])

        unauthorized_sales = list()
        for sales_transaction in sales_transactions:
            product_id = sales_transaction.get('productID')
            seller_id = sales_transaction.get('sellerID')

            if not any(pl.get('productID') == product_id and pl.get('authorizedSellerID') == seller_id for pl in product_listings):
                unauthorized_sales.append({
                    'productID': product_id,
                    'unauthorizedSellerID': [seller_id]
                })
        return JsonResponse({'unauthorizedSales': unauthorized_sales}, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
