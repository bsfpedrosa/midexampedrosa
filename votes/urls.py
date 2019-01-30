from django.urls import path
from . import views

app_name = 'votes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:candidate_id>/', views.detail, name='candidate_detail'),
    path('<int:candidate_id>/update', views.update, name='update'),
    path('Ccreate/', views.create, name = 'candidate_create'),
    path('Pcreate/', views.create, name = 'position_create'),
    path('<int:candidate_id>/vote', views.vote, name='vote'),
]
