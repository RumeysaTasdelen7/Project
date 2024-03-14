# from django.urls import path
# from .views import OrderListView, OrderDetailView

# urlpatterns = [
#     path('orders/', OrderListView.as_view(), name='order-list'),
#     path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
# ]

from django.urls import path
from .views import OrderAddView, OrderDeleteView, OrderDetailView, OrderUpdateView, OrderListView


urlpatterns = [
    path("admin/<int:pk>/add/", OrderAddView.as_view(), name="order_add"),
    path("visitors/<int:pk>/", OrderDetailView.as_view(), name="order_detail"),
    path("visitors/all/", OrderListView.as_view(), name="order_all"),
    path("visitors/pages/", OrderListView.as_view(), name="order_all_pages"),
    path("admin/<int:pk>/auth/", OrderDeleteView.as_view(), name="order_delete"),
    path("admin/auth/", OrderUpdateView.as_view(), name="order_update"),
]