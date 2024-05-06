from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from .models import CategoryModel, ProductModel

the_user = get_user_model()


# Create your views here.
def home_view(request):
    categories = CategoryModel.objects.all()
    products = ProductModel.objects.all()
    return render(
        request,
        'home.html',
        {
            'products': products,
            'categories': categories
        }
    )


def product_detail_view(request, slug):
    product = get_object_or_404(ProductModel, slug=slug, in_stock=True)
    return render(request, 'product.html', {'product': product})


def category_detail_view(request, slug):
    category = get_object_or_404(CategoryModel, slug=slug)
    products = ProductModel.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'products': products})
