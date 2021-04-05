from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (IndexView, ProductView, ProductDeleteView, ProductUpdateView, ProductCreateView, CartAddProductView)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('<int:pk>/', ProjectView.as_view(), name='project'),
    path('<int:pk>/product', ProductView.as_view(), name='product'),
    path('add/', ProductCreateView.as_view(), name='product-add'),
    # path('<int:pk>/update/project', ProjectUpdateView.as_view(), name='project-update'),
    # path('<int:pk>/add/', TaskCreate.as_view(), name='task_add'),
    path('<int:pk>/update', ProductUpdateView.as_view(), name='product-update'),
    path('<int:pk>/delete', ProductDeleteView.as_view(), name='product-delete'),
    path('<int:pk>/add/cart', CartAddProductView.as_view(), name='cart-add')


    # path('<int:pk>/delete/project', ProjectDeleteView.as_view(), name='project-delete'),

]