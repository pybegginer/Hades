from django.contrib import admin
from django.urls import path

from core.erp.views.category.views import CategoryListView, CreateCategoryView

#app
app_name = 'erp'
urlpatterns = [
    path('category/list', CategoryListView.as_view(), name='category_list'),
    path('category/create', CreateCategoryView.as_view(), name='category_create'),

]