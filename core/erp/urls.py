from django.contrib import admin
from django.urls import path

from core.erp.views import my_first_view, my_second_view
#app
app_name = 'erp'
urlpatterns = [
    path('uno/', my_first_view, name='Template1'),
    path('dos/', my_second_view, name='Template2'),
]