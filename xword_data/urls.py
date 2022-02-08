from django.urls import path
from . import views

urlpatterns = [
    path('drill/<int:pk>', views.drill, name='drill'),
    path('answer/<int:pk>', views.answer, name='answer')
]
