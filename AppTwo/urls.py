from django.urls import path
from . import views

app_name = 'AppTwo'

urlpatterns = [
    path('relate/', views.relative, name='relative' ),
    path('other/', views.other, name='other'),
]