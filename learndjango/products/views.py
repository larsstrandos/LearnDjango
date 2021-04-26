from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm
from .models import Product

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset,
    }
    return render(request, "products/product_list.html", context)

def product_lookup_view(request, id):
    #obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    context = {
        "object": obj,
    }
    return render(request, "products/product_detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    #POST request
    if request.method == "POST":
        #Confirming delete
        obj.delete()
        return redirect("../../")
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)