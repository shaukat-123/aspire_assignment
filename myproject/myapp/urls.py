from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, BulkInsertView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('bulk_create/',BulkInsertView.as_view(), name='bulk-insert'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
