from django.urls import path
from . import views

app_name = "leeds"
urlpatterns = [
    path('all/', views.leed_list),
]