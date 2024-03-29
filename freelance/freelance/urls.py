from django.urls import path
from views import(
        MainPageView,
        ExecutorListView,
        ExecutorDetailView,
        ServiceListView,
        ServiceDetailView,
        OrderListView,
        OrderDetailView,
        CustomerListView,
        CustomerDetailView,
    
)

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('executors/', ExecutorListView.as_view(), name='executor-list'),
    path('executors/<int:pk>/', ExecutorDetailView.as_view(), name='executor-detail'),
]