from django.urls import path, re_path, include


from .views import UserRegisterView, LoginUserView, LogoutUserView
app_name = "users_app"

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', LoginUserView.as_view(), name='user-login'),
    path('logout/', LogoutUserView.as_view(), name='user-logout'),
]