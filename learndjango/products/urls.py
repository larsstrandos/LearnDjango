from django.urls import path
from products.views import (
    product_lookup_view,
    product_delete_view,
    product_list_view
)

app_name = 'products'
urlpatterns = [
    path('<int:id>/', product_lookup_view, name="product-detail"),
    path('<int:id>/delete/', product_delete_view, name="product-delete"),
    path('', product_list_view, name="product-list"),
]