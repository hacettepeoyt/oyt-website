from django.urls import path

from event import views

urlpatterns = [
    path('', views.EventListView.as_view(), name='event-list')
]
