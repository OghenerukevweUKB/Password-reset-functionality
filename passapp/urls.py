from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='passapp/reset_password.html'), name='reset_password'),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='passapp/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='passapp/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='passapp/password_reset_complete.html'), name='password_reset_complete'),
]
