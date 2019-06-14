from django.urls import path
from . import views

app_name = 'rank'

urlpatterns = [
    path('', views.RankView.as_view(), name='rank'),
    path('add_rank/', views.add_rank, name='add_rank'),
    path('edit_rank/', views.edit_rank, name='edit_rank'),
    path('delete_rank/', views.delete_rank, name='delete_rank'),
]
