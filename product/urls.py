from rest_framework import routers

from product.views.ProductViewSet import ProductViewSet
from product.views.ProductCategoryViewSet import ProductCategoryViewSet
from product.views.UserOrderSummaryViewSet import UserOrderSummaryViewSet

router = routers.SimpleRouter()

router.register(r'categories', ProductCategoryViewSet, base_name='categories')
router.register(r'products', ProductViewSet, base_name='product')
router.register(r'ordersummary',UserOrderSummaryViewSet, base_name='orser_summary')

urlpatterns = router.urls
