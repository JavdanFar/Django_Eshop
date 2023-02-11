from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import login_user, register, log_out, user_account_main_page, edit_user_profile, password_reset_request

urlpatterns = [
    path('login/', login_user),

    path('register/', register),
    path('logout/', log_out),
    path('user/', user_account_main_page),
    path('user/edit', edit_user_profile),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('password_reset/', password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset/password_reset_complete.html'),
         name='password_reset_complete'),
]
