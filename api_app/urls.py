from django.urls import path
from api_app import views

urlpatterns = [
    path('', views.books_list),
    path('<int:pk>', views.books_detail),
]