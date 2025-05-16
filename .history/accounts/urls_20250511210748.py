from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('accounts/profile/', profile,name='profile'),
    path('update_profile/<int:id>/', update_profile, name='update_profile'),
    path('accounts/about/', about, name='about')

]
