
from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page, name="home"),
    path('image/<str:key>/', view_image, name="image"),
    path('update/<str:id>/', update_image, name='update'),
    path('delete/<str:id>/', delete_image, name='delete'),
    path('infer/<str:id>/', run_inference, name='infer'),
]