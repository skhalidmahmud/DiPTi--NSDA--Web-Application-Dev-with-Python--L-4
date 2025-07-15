from django.urls import path
from . import views

urlpatterns = [
    path('', views.sendMailPage, name='sendMailPage'),
    path('sendMail/', views.sendMail, name='sendMail'),
    path('forgatePass/', views.forgatePass, name='forgatePass'),
]