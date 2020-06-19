from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login, PasswordChangeView, \
    PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView


app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('logout_then_login', logout_then_login, name='logout_then_login'),
]
