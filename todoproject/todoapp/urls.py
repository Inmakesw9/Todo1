from django.urls import path,include
from . import views

urlpatterns = [

    path('', views.add, name='add'),
    # path('details', views.details, name='details'),
    path('delete<int:taskid>/', views.delete, name='delete'),
    path('update<int:taskid>/', views.update, name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.Taskdetailview.as_view(),name='cbvdetail'),
    path('cbvdelete/<int:pk>/', views.Taskdeleteview.as_view(), name='cbvdelete')

]
