from django.urls import path
from . import views
from .models import Note

app_name = 'note'
urlpatterns = [
    path('', views.Notelist.as_view(), name='note-list'),
    path('mix/', views.BlogViewMix.as_view(), name='blog-mix'),
    path('about/',views.index, name = 'index')
    ]
