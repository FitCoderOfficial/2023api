from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register("products", views.ProductsViewSet)
router.register("categories", views.CategoriesViewSet)
router.register("carts", views.CartViewSet)
router.register("banner", views.BannerViewSet)
products_router = routers.NestedDefaultRouter(router, "products", lookup="product")
products_router.register("reviews", views.ReviewViewSet, basename="product-reviews")



urlpatterns = [
    path("", include(router.urls)),
    path("", include(products_router.urls)),
]