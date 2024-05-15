from django.urls import path, include
from account.views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, SendPasswordRestEmailView
urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name='register'),
    path("login/", UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changrpassword'),
    path('send-reset-password-email/', SendPasswordRestEmailView.as_view(), name='send-reset-password-email'),
]