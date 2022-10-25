from django.urls import path,include


from app.views import LatesProductsList
from app import views


urlpatterns = [
    path('latest-products/',LatesProductsList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<slug:category_slug/',views.CategoryDetail.as_view())
]
