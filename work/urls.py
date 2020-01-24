from django.urls import path
from . import views

urlpatterns = [
    path('',views.listview.as_view() ,name='listview'),
    path('addwork/',views.createview.as_view(),name='addwork'),
    path('editwork/<int:pk>/',views.updateview.as_view(),name='update'),
    path('detail/<int:pk>/',views.detailview.as_view(),name='detail'),
     path('delete/<int:pk>/',views.deleteview.as_view(),name='delete'),
     path('search/', views.search,name='search')
]

