from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', index, name='index'),
    path('accounts/profile/', profile,name='profile'),
    path('update_profile/<int:id>/', update_profile, name='update_profile'),
    path('accounts/about/', about, name='about')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])