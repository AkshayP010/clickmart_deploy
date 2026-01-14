from django.urls import path
from users import views as UserViews
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from products import views as ProductViews
from carts import views as cartview
from orders import views as OrderViews

urlpatterns = [
    path('register/', UserViews.RegisterView.as_view()),
    
    
    path('token/', TokenObtainPairView.as_view(), name='tokan_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('profile/', UserViews.ProfileView.as_view()),
    
    path('products/', ProductViews.ProductListView.as_view()),
    path('products/<int:pk>/', ProductViews.ProductDetailView.as_view()),
    
    
    path('cart/', cartview.CartView.as_view()),
    path('cart/add/', cartview.AddToCartView.as_view()),
    
    path('cart/items/<int:item_id>/',cartview.ManageCartItemView.as_view()),
    
    path('orders/', OrderViews.OrderListView.as_view()),

    path('orders/place/',OrderViews.PlaceOrderView.as_view()),
    
    path('orders/<int:pk>/',OrderViews.OrderDetailView.as_view()),
     
     
    
]