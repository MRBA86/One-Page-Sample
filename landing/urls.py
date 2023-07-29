from django.urls import include, path
from landing.views import *
app_name = 'landing'

urlpatterns = [
  
    path('', index_view, name = 'index')
]