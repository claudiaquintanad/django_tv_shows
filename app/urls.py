from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.all_shows),
    path('shows/new', views.render_add),
    path('shows/create', views.addshow),
    path('shows/<int:val>/edit', views.editshow),
    path('shows/edit', views.edit),
    path('shows/<int:val>', views.oneshow),
    path('shows/<int:val>/delete', views.delete),
]
