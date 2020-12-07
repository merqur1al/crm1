from . import views

from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html',
                                              email_template_name='users/passsword_reset_email.html',
                                              success_url=reverse_lazy('users:password_reset_done')),
         name='password_reset'),
    path('password_reset_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_sent.html'),
         name='password_reset_done'),
    path('password_reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',
                                                     success_url=reverse_lazy('users:password_reset_complete')),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete')
]