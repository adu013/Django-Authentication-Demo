from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import (
    LoginView, PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView
)
from . import views


urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path(
        'password-reset/',
        PasswordResetView.as_view(template_name='accounts/password-reset.html'),
        name='password_reset'
    ),
    path(
        'password-reset/done/',
        PasswordResetDoneView.as_view(template_name='accounts/password-reset-done.html'),
        name='password_reset_done'
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name='accounts/password-reset-confirm.html'),
        name='password_reset_confirm'
    ),
    path(
        'password-reset-complete',
        PasswordResetCompleteView.as_view(template_name='accounts/password-reset-complete.html'),
        name='password_reset_complete'
    ),
]
