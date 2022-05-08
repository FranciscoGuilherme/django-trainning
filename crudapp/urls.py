from django.urls import path

from . import views

urlpatterns = [
    path('rules/', views.BusinessList.as_view()),
]
