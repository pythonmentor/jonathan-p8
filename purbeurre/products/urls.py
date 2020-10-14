from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "products"

urlpatterns = [
    # ex : /products/search/
    path('search/', views.search, name="search"),
    path('<int:product_id>/detail/', views.detail, name='detail'),
    # path("<int:product_id>/favorite/>", views.favorite, name="favorite"),
    path('favorite/', views.favorite, name="favorite"),
]