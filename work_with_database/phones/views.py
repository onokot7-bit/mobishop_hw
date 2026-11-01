from django.shortcuts import get_object_or_404, redirect, render
from phones.models import Phone


def index(request):
    return redirect("catalog")


def show_catalog(request):
    sort = request.GET.get("sort", "name")
    if sort == "min_price":
        phones = Phone.objects.order_by("price")
    elif sort == "max_price":
        phones = Phone.objects.order_by("-price")
    else:
        phones = Phone.objects.order_by("name")
    return render(request, "catalog.html", {"phones": phones})


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, "product.html", {"phone": phone})
