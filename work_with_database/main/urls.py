from django.contrib import admin
from django.urls import path
from phones import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("catalog/", views.show_catalog, name="catalog"),
    path("catalog/<slug:slug>/", views.show_product, name="phone"),
]
