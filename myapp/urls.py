from django.urls import path
from django.contrib.auth import views as auth_views
from myapp import views



urlpatterns = [
    path('',views.Home,name='index'),
    # path('login',views.Loginpage,name="login"),
    path('loginpage',views.Loginpage,name="loginpage"),
    # path('accounts/loginpage',views.Loginpage,name="loginpage"),
    path('dashboard',views.DashboardPage,name="dashboard"),
    path('course/<int:id>',views.Course,name='course'),
    path('logoutPage',views.logoutPage,name="logoutPage"),
    path('registerpage',views.register,name="registerpage"),
    path('search/',views.searchitem,name="search"),
    path('pay', views.app_create, name='app_create'),
    path('payment1/charge/<int:id>', views.app_charge, name='app_charge'),
    path('payment1/<int:id>', views.payment1, name='payment1'),
    path('loginpage2/',views.Loginpage2,name="loginpage2"),
    path('bill/<int:id>',views.Bill,name="bill"),
    path('addtocart/<int:id>',views.Addtocart, name='addtocart'),
    path('viewcart',views.ViewCart, name='viewcart'),
    
    
    
    
    
    



#reset password urls

path('password_reset/',auth_views.PasswordResetView.
as_view(),name='password_reset'),

path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),

path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]