from rest_framework import routers

from product.views.ProductViewSet import ProductViewSet
from product.views.ProductCategoryViewSet import ProductCategoryViewSet
from product.views.UserOrderViewSet import UserOrderViewSet

router = routers.SimpleRouter()

router.register(r'categories', ProductCategoryViewSet, base_name='categories')
router.register(r'products', ProductViewSet, base_name='product')
router.register(r'userorder', UserOrderViewSet, base_name='user_order')

urlpatterns = router.urls
