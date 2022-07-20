from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('yarns/', views.yarns_index, name='index'),
path('yarns/<int:yarn_id>/', views.yarns_detail, name='detail'),
path('yarns/create/', views.YarnCreate.as_view(), name='yarns_create'),
path('yarns/<int:pk>/update/', views.YarnUpdate.as_view(), name='yarns_update'),
path('yarns/<int:pk>/delete/', views.YarnDelete.as_view(), name='yarns_delete'),
path('yarns/<int:yarn_id>/add_production/', views.add_production, name='add_production')
]
