from django.urls import path
from . import views

urlpatterns=[
    path('mult/', views.multiplication.as_view(), name='multiplication'),
]