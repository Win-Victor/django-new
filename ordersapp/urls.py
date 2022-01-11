from django.urls import path
from ordersapp import views as ordersapp


app_name = 'ordersapp'

urlpatterns = [
    path('', ordersapp.OrderListView.as_view(), name='list'),
    path('create/', ordersapp.OrderCreateView.as_view(), name='create'),
    path('update/<pk>/', ordersapp.UpdateView.as_view(), name='update'),
    path('read/<pk>/', ordersapp.DetailView.as_view(), name='read'),
    path('delete/<pk>/', ordersapp.DeleteView.as_view(), name='delete'),
    path('complete/<pk>/', ordersapp.complete, name='complete'),
]
