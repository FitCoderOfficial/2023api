
from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("products", views.ProductsViewSet)
router.register("categories", views.CategoriesViewSet)

urlpatterns = router.urls

# urlpatterns = [
    # path("products", views.ApiProducts.as_view()),
    # path("products/<str:pk>", views.ApiProduct.as_view()),
    # path("categories", views.ApiCategories.as_view()),
    # path("categories/<str:pk>", views.ApiCategory.as_view())
# ]