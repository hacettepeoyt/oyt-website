from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project-list'),
    path('idea/', views.IdeaView.as_view(), name='idea'),
]
