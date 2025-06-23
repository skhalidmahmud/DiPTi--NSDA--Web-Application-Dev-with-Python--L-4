from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', news, name='news_home'),
    path('add/', addNews, name='add_news'),
    path('view/<int:id>/', viewNews, name='view_news'),
    path('edit/<int:id>/', editNews, name='edit_news'),
    path('delete/<int:id>/', deleteNews, name='delete_news'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)