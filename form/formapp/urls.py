from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('Regi',views.Regi,name='Regi'),
    path('view',views.view,name='view'),
    path('deleteUser/<int:id>',views.deleteUser,name='deleteuser'),
    path('editUser/<int:id>',views.editUser,name='edituser'),
    path('inserteditUser',views.inserteditUser,name='inserteditUser'),
    # path('viewpagination',views.viewpagination,name='viewpagination'),
    path('search',views.search,name='search'),
]    