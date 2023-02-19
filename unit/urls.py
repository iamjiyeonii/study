from django.urls import path
from . import views


app_name = 'unit'

urlpatterns = [
    path('', views.function_test, name='function_test'),
]