from django.urls import path
from products.views import (product_create_view, dynamic_lookup_view, product_delete_view,
                            product_list_view)

app_name = 'products'
urlpatterns = [
    path('create/', product_create_view),
    path('<int:my_id>/', dynamic_lookup_view, name='product'),
    path('<int:my_id>/delete', product_delete_view, name='product-delete'),
    path('', product_list_view, name='products'),
]
