from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path('tours/<int:tour_id>/', views.tours, name = 'tours')
]

handler404 = views.page_not_found