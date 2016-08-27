from rest_framework import routers

from product.views.ProductCategoryViewSet import ProductCategoryViewSet

router = routers.DefaultRouter()

router.register(r'categories', ProductCategoryViewSet)

urlpatterns = router.urls
