from django.urls import path
from . import views
app_name='movieapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('allmovie',views.AllMovies,name='allmovie'),
    path('moviedetail/<int:id>/', views.movieDetail, name='moviedetail'),
    path('addmovie/',views.addmovie,name='addmovie'),
    path('updatemovie/<int:id>/', views.updatemovie, name='updatemovie'),
    path('deletemovie/<int:id>/', views.deletemovie, name='deletemovie')
]